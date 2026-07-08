import re

from filters.date_filter import deteksi_tahun, deteksi_bulan
from filters.location_filter import ekstrak_lokasi
from services.sitaba_service import normalisasi_bencana


def deteksi_jenis_bencana(pertanyaan):
    q = pertanyaan.lower()

    jenis_map = {
        "tanah longsor": "longsor",
        "longsor": "longsor",
        "banjir": "banjir",
        "gempa bumi": "gempa",
        "gempabumi": "gempa",
        "gempa": "gempa",
        "kekeringan": "kekeringan",
        "erupsi": "erupsi",
        "gunung api": "erupsi",
        "cuaca ekstrem": "cuaca ekstrim",
        "cuaca ekstrim": "cuaca ekstrim",
        "kebakaran": "kebakaran",
        "abrasi": "abrasi",
    }

    for keyword, nilai in jenis_map.items():
        if keyword in q:
            return nilai

    return None


def bersihkan_nama_lokasi(teks):
    if not teks:
        return None

    teks = teks.upper().strip()

    stopwords = [
        "YANG", "TERKENA", "TERDAMPAK", "BENCANA", "ADA", "APAKAH",
        "DI", "TERJADI", "LONGSOR", "BANJIR", "GEMPA", "KEKERINGAN",
        "ERUPSI", "KEBAKARAN", "ABRASI", "CUACA", "EKSTREM", "EKSTRIM",
        "TAHUN", "BULAN", "SAAT", "INI", "SEKARANG"
    ]

    kata_bersih = []

    for kata in teks.split():
        if kata in stopwords:
            break
        kata_bersih.append(kata)

    hasil = " ".join(kata_bersih).strip()
    return hasil or None


def deteksi_lokasi_manual(pertanyaan):
    q = pertanyaan.upper()

    lokasi_manual = {
        "provinsi": None,
        "kota": [],
        "kecamatan": [],
        "kelurahan": [],
        "jalan": []
    }

    pola_map = {
        "provinsi": r"\bPROVINSI\s+([A-Z\s]+)",
        "kota": r"\b(?:KOTA|KABUPATEN|KAB\.|KAB)\s+([A-Z\s]+)",
        "kecamatan": r"\b(?:KECAMATAN|KEC\.|KEC)\s+([A-Z\s]+)",
        "kelurahan": r"\b(?:KELURAHAN|DESA|KEL\.|KEL)\s+([A-Z\s]+)",
        "jalan": r"\b(?:JALAN|JL\.|JL)\s+([A-Z0-9\s]+)"
    }

    for tipe, pola in pola_map.items():
        match = re.search(pola, q)

        if match:
            nama = bersihkan_nama_lokasi(match.group(1))

            if nama:
                if tipe == "provinsi":
                    lokasi_manual["provinsi"] = nama
                else:
                    lokasi_manual[tipe].append(nama)

    return lokasi_manual


def gabungkan_list_lokasi(lokasi_awal, lokasi_manual):
    hasil = lokasi_awal or []

    for item in lokasi_manual:
        if item and item not in hasil:
            hasil.append(item)

    return hasil


def cocok_lokasi(target_list, data_lokasi):
    if not target_list:
        return True

    data_lokasi = (data_lokasi or "").upper().strip()

    for target in target_list:
        target = (target or "").upper().strip()

        if not target:
            continue

        if target == data_lokasi:
            return True

        if target in data_lokasi:
            return True

        if data_lokasi in target:
            return True

    return False


def ada_filter_lokasi(filter_info):
    if not filter_info:
        return False

    return bool(
        filter_info.get("provinsi")
        or filter_info.get("kota")
        or filter_info.get("kecamatan")
        or filter_info.get("kelurahan")
        or filter_info.get("jalan")
    )

def normalisasi_provinsi_dicari(value):
    if not value:
        return None

    teks = str(value).upper().strip()

    alias = {
        "JABAR": "JAWA BARAT",
        "JAWA BARAT": "JAWA BARAT",
        "JATIM": "JAWA TIMUR",
        "JAWA TIMUR": "JAWA TIMUR",
        "JATENG": "JAWA TENGAH",
        "JAWA TENGAH": "JAWA TENGAH",
        "DKI": "DKI JAKARTA",
        "JAKARTA": "DKI JAKARTA",
    }

    return alias.get(teks, teks)


def filter_bencana(daftar, pertanyaan):
    tahun = deteksi_tahun(pertanyaan)
    bulan_angka, bulan_nama = deteksi_bulan(pertanyaan)

    lokasi = ekstrak_lokasi(pertanyaan, daftar) or {}
    lokasi_manual = deteksi_lokasi_manual(pertanyaan)

    jenis_dicari = deteksi_jenis_bencana(pertanyaan)

    provinsi_dicari = lokasi.get("provinsi") or lokasi_manual.get("provinsi")
    
    kota_dicari = gabungkan_list_lokasi(
        lokasi.get("kota") or [],
        lokasi_manual.get("kota") or []
    )
    kecamatan_dicari = gabungkan_list_lokasi(
        lokasi.get("kecamatan") or [],
        lokasi_manual.get("kecamatan") or []
    )
    kelurahan_dicari = gabungkan_list_lokasi(
        lokasi.get("kelurahan") or [],
        lokasi_manual.get("kelurahan") or []
    )
    jalan_dicari = gabungkan_list_lokasi(
        lokasi.get("jalan") or [],
        lokasi_manual.get("jalan") or []
    )

    hasil = []

    for item in daftar:
        data = normalisasi_bencana(item)

        tanggal = data.get("tanggal") or ""
        jenis_data = (data.get("jenis") or "").lower()
        nama_data = (data.get("nama") or "").lower()

        provinsi_data = (data.get("provinsi") or "").upper().strip()
        kota_data = (data.get("kota") or "").upper().strip()
        kecamatan_data = (data.get("kecamatan") or "").upper().strip()
        kelurahan_data = (data.get("kelurahan") or "").upper().strip()
        jalan_data = (data.get("road") or "").upper().strip()

        if provinsi_dicari and provinsi_data != provinsi_dicari:
            continue

        if not cocok_lokasi(kota_dicari, kota_data):
            continue

        if not cocok_lokasi(kecamatan_dicari, kecamatan_data):
            continue

        if not cocok_lokasi(kelurahan_dicari, kelurahan_data):
            continue

        if not cocok_lokasi(jalan_dicari, jalan_data):
            continue

        if tahun and tahun not in tanggal:
            continue

        if bulan_angka and f"-{bulan_angka}-" not in tanggal:
            continue

        if jenis_dicari:
            if jenis_dicari not in jenis_data and jenis_dicari not in nama_data:
                continue

        hasil.append(data)

    filter_info = {
        "tahun": tahun,
        "bulan_angka": bulan_angka,
        "bulan_nama": bulan_nama,
        "provinsi": provinsi_dicari,
        "kota": kota_dicari,
        "kecamatan": kecamatan_dicari,
        "kelurahan": kelurahan_dicari,
        "jalan": jalan_dicari,
        "jenis": jenis_dicari,
        "ada_filter_lokasi": ada_filter_lokasi({
            "provinsi": provinsi_dicari,
            "kota": kota_dicari,
            "kecamatan": kecamatan_dicari,
            "kelurahan": kelurahan_dicari,
            "jalan": jalan_dicari,
        })
    }

    print("====================================")
    print("PERTANYAAN :", pertanyaan)
    print("LOKASI OTOMATIS :", lokasi)
    print("LOKASI MANUAL :", lokasi_manual)
    print("FILTER INFO :", filter_info)
    print("JUMLAH HASIL :", len(hasil))
    print("====================================")

    return hasil, filter_info
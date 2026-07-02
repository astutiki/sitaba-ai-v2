from filters.date_filter import deteksi_tahun, deteksi_bulan
from filters.location_filter import ekstrak_lokasi
from services.sitaba_service import normalisasi_bencana


def deteksi_jenis_bencana(pertanyaan):
    q = pertanyaan.lower()

    jenis_map = {
        "banjir": "banjir",
        "longsor": "longsor",
        "tanah longsor": "longsor",
        "gempa": "gempa",
        "gempabumi": "gempa",
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


def filter_bencana(daftar, pertanyaan):
    tahun = deteksi_tahun(pertanyaan)
    bulan_angka, bulan_nama = deteksi_bulan(pertanyaan)
    lokasi = ekstrak_lokasi(pertanyaan, daftar)
    jenis_dicari = deteksi_jenis_bencana(pertanyaan)

    provinsi_dicari = lokasi.get("provinsi")
    kota_dicari = lokasi.get("kota") or []
    kecamatan_dicari = lokasi.get("kecamatan") or []
    kelurahan_dicari = lokasi.get("kelurahan") or []
    jalan_dicari = lokasi.get("jalan") or []

    hasil = []

    for item in daftar:
        data = normalisasi_bencana(item)

        tanggal = data.get("tanggal") or ""
        jenis_data = (data.get("jenis") or "").lower()
        nama_data = (data.get("nama") or "").lower()

        provinsi_data = (data.get("provinsi") or "").upper()
        kota_data = (data.get("kota") or "").upper()
        kecamatan_data = (data.get("kecamatan") or "").upper()
        kelurahan_data = (data.get("kelurahan") or "").upper()
        jalan_data = (data.get("road") or data.get("jalan") or "").upper()

        if provinsi_dicari and provinsi_data != provinsi_dicari:
            continue

        if kota_dicari and kota_data not in kota_dicari:
            continue

        if kecamatan_dicari and kecamatan_data not in kecamatan_dicari:
            continue

        if kelurahan_dicari and kelurahan_data not in kelurahan_dicari:
            continue

        if jalan_dicari and jalan_data not in jalan_dicari:
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
    }

    return hasil, filter_info
import re

from filters.date_filter import (
    deteksi_tahun,
    deteksi_bulan,
)

from filters.location_filter import ekstrak_lokasi
from services.sitaba_service import normalisasi_bencana


def deteksi_jenis_bencana(pertanyaan):
    q = pertanyaan.lower()

    jenis_map = {
        "banjir": "banjir",
        "tanah longsor": "longsor",
        "longsor": "longsor",
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


def deteksi_rentang_tahun(pertanyaan):
    """
    Mendeteksi satu tahun atau rentang tahun.

    Contoh:
    - "Statistik 2022"       -> tahun=2022
    - "Statistik 2022-2026"  -> 2022 sampai 2026
    - "2022 sampai 2026"     -> 2022 sampai 2026
    """

    tahun_ditemukan = re.findall(
        r"\b(20\d{2})\b",
        pertanyaan,
    )

    if len(tahun_ditemukan) >= 2:
        tahun_awal = int(tahun_ditemukan[0])
        tahun_akhir = int(tahun_ditemukan[1])

        if tahun_awal > tahun_akhir:
            tahun_awal, tahun_akhir = (
                tahun_akhir,
                tahun_awal,
            )

        return {
            "rentang_tahun": True,
            "tahun_awal": tahun_awal,
            "tahun_akhir": tahun_akhir,
            "tahun": None,
        }

    if len(tahun_ditemukan) == 1:
        return {
            "rentang_tahun": False,
            "tahun_awal": None,
            "tahun_akhir": None,
            "tahun": tahun_ditemukan[0],
        }

    return {
        "rentang_tahun": False,
        "tahun_awal": None,
        "tahun_akhir": None,
        "tahun": None,
    }


def filter_bencana(daftar, pertanyaan):
    # Deteksi tahun lama tetap digunakan sebagai cadangan.
    tahun_lama = deteksi_tahun(pertanyaan)

    # Tambahan baru untuk rentang tahun.
    info_tahun = deteksi_rentang_tahun(
        pertanyaan
    )

    tahun = (
        info_tahun.get("tahun")
        or tahun_lama
    )

    rentang_tahun = info_tahun.get(
        "rentang_tahun",
        False,
    )

    tahun_awal = info_tahun.get(
        "tahun_awal"
    )

    tahun_akhir = info_tahun.get(
        "tahun_akhir"
    )

    bulan_angka, bulan_nama = deteksi_bulan(
        pertanyaan
    )

    lokasi = ekstrak_lokasi(
        pertanyaan,
        daftar,
    )

    jenis_dicari = deteksi_jenis_bencana(
        pertanyaan
    )

    provinsi_dicari = lokasi.get("provinsi")
    kota_dicari = lokasi.get("kota") or []
    kecamatan_dicari = (
        lokasi.get("kecamatan") or []
    )
    kelurahan_dicari = (
        lokasi.get("kelurahan") or []
    )
    jalan_dicari = lokasi.get("jalan") or []

    hasil = []

    for item in daftar:
        data = normalisasi_bencana(item)

        tanggal = str(
            data.get("tanggal") or ""
        )

        jenis_data = str(
            data.get("jenis") or ""
        ).lower()

        nama_data = str(
            data.get("nama") or ""
        ).lower()

        provinsi_data = str(
            data.get("provinsi") or ""
        ).upper()

        kota_data = str(
            data.get("kota") or ""
        ).upper()

        kecamatan_data = str(
            data.get("kecamatan") or ""
        ).upper()

        kelurahan_data = str(
            data.get("kelurahan") or ""
        ).upper()

        jalan_data = str(
            data.get("road")
            or data.get("jalan")
            or ""
        ).upper()

        # =============================================
        # FILTER LOKASI LAMA
        # =============================================

        if (
            provinsi_dicari
            and provinsi_data != provinsi_dicari
        ):
            continue

        if kota_dicari:
            cocok_kota = False

            for kota_target in kota_dicari:
                if (
                    kota_target in kota_data
                    or kota_data in kota_target
                ):
                    cocok_kota = True
                    break

            if not cocok_kota:
                continue

        if (
            kecamatan_dicari
            and kecamatan_data
            not in kecamatan_dicari
        ):
            continue

        if (
            kelurahan_dicari
            and kelurahan_data
            not in kelurahan_dicari
        ):
            continue

        if (
            jalan_dicari
            and jalan_data not in jalan_dicari
        ):
            continue

        # =============================================
        # FILTER TAHUN
        # =============================================

        tahun_data = tanggal[:4]

        if rentang_tahun:
            if not tahun_data.isdigit():
                continue

            tahun_data_int = int(tahun_data)

            if not (
                tahun_awal
                <= tahun_data_int
                <= tahun_akhir
            ):
                continue

        elif tahun:
            # Fungsi tahun tunggal lama tetap berjalan.
            if str(tahun) not in tanggal:
                continue

        # =============================================
        # FILTER BULAN LAMA
        # =============================================

        if (
            bulan_angka
            and f"-{bulan_angka}-"
            not in tanggal
        ):
            continue

        # =============================================
        # FILTER JENIS BENCANA LAMA
        # =============================================

        if jenis_dicari:
            cocok_jenis = (
                jenis_dicari in jenis_data
                or jenis_dicari in nama_data
            )

            if not cocok_jenis:
                continue

        hasil.append(data)

    filter_info = {
        "tahun": (
            None
            if rentang_tahun
            else tahun
        ),
        "rentang_tahun": rentang_tahun,
        "tahun_awal": tahun_awal,
        "tahun_akhir": tahun_akhir,
        "bulan_angka": bulan_angka,
        "bulan_nama": bulan_nama,
        "provinsi": provinsi_dicari,
        "kota": kota_dicari,
        "kecamatan": kecamatan_dicari,
        "kelurahan": kelurahan_dicari,
        "jalan": jalan_dicari,
        "jenis": jenis_dicari,
        "ada_filter_lokasi": bool(
            provinsi_dicari
            or kota_dicari
            or kecamatan_dicari
            or kelurahan_dicari
            or jalan_dicari
        ),
    }

    return hasil, filter_info
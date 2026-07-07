"""
location_filter.py
Filter lokasi: provinsi, kabupaten/kota, kecamatan, kelurahan, jalan.
"""

import re

PROVINSI_MAP = {
    "aceh": "ACEH",
    "sumatera utara": "SUMATERA UTARA",
    "sumut": "SUMATERA UTARA",
    "sumatera barat": "SUMATERA BARAT",
    "sumbar": "SUMATERA BARAT",
    "riau": "RIAU",
    "kepulauan riau": "KEPULAUAN RIAU",
    "kepri": "KEPULAUAN RIAU",
    "jambi": "JAMBI",
    "sumatera selatan": "SUMATERA SELATAN",
    "sumsel": "SUMATERA SELATAN",
    "kepulauan bangka belitung": "KEPULAUAN BANGKA BELITUNG",
    "bangka belitung": "KEPULAUAN BANGKA BELITUNG",
    "bengkulu": "BENGKULU",
    "lampung": "LAMPUNG",

    "dki jakarta": "DKI JAKARTA",
    "jakarta": "DKI JAKARTA",
    "dki": "DKI JAKARTA",
    "banten": "BANTEN",
    "jawa barat": "JAWA BARAT",
    "jabar": "JAWA BARAT",
    "jawa tengah": "JAWA TENGAH",
    "jateng": "JAWA TENGAH",
    "jawa timur": "JAWA TIMUR",
    "jatim": "JAWA TIMUR",
    "di yogyakarta": "DI YOGYAKARTA",
    "yogyakarta": "DI YOGYAKARTA",
    "diy": "DI YOGYAKARTA",
    "jogja": "DI YOGYAKARTA",
    "jogya": "DI YOGYAKARTA",
    "yogya" :"DI YOGYAKARTA",

    "bali": "BALI",
    "nusa tenggara barat": "NUSA TENGGARA BARAT",
    "ntb": "NUSA TENGGARA BARAT",
    "nusa tenggara timur": "NUSA TENGGARA TIMUR",
    "ntt": "NUSA TENGGARA TIMUR",

    "kalimantan barat": "KALIMANTAN BARAT",
    "kalbar": "KALIMANTAN BARAT",
    "kalimantan tengah": "KALIMANTAN TENGAH",
    "kalteng": "KALIMANTAN TENGAH",
    "kalimantan selatan": "KALIMANTAN SELATAN",
    "kalsel": "KALIMANTAN SELATAN",
    "kalimantan timur": "KALIMANTAN TIMUR",
    "kaltim": "KALIMANTAN TIMUR",
    "kalimantan utara": "KALIMANTAN UTARA",
    "kaltara": "KALIMANTAN UTARA",
    "kalut": "KALIMANTAN UTARA",

    "sulawesi utara": "SULAWESI UTARA",
    "sulut": "SULAWESI UTARA",
    "gorontalo": "GORONTALO",
    "sulawesi tengah": "SULAWESI TENGAH",
    "sulteng": "SULAWESI TENGAH",
    "sulawesi barat": "SULAWESI BARAT",
    "sulbar": "SULAWESI BARAT",
    "sulawesi selatan": "SULAWESI SELATAN",
    "sulsel": "SULAWESI SELATAN",
    "sulawesi tenggara": "SULAWESI TENGGARA",
    "sultra": "SULAWESI TENGGARA",

    "maluku utara": "MALUKU UTARA",
    "malut": "MALUKU UTARA",
    "maluku": "MALUKU",

    "papua barat daya": "PAPUA BARAT DAYA",
    "pbd": "PAPUA BARAT DAYA",
    "papua pegunungan": "PAPUA PEGUNUNGAN",
    "papeg": "PAPUA PEGUNUNGAN",
    "papua tengah": "PAPUA TENGAH",
    "pateng": "PAPUA TENGAH",
    "papua selatan": "PAPUA SELATAN",
    "pasel": "PAPUA SELATAN",
    "papua barat": "PAPUA BARAT",
    "pabar": "PAPUA BARAT",
    "papua": "PAPUA",
}

KOTA_ALIAS = {
    "tapteng": "KABUPATEN TAPANULI TENGAH",
    "tapanuli tengah": "KABUPATEN TAPANULI TENGAH",
    "taput": "KABUPATEN TAPANULI UTARA",
    "tapanuli utara": "KABUPATEN TAPANULI UTARA",
    "tapsel": "KABUPATEN TAPANULI SELATAN",
    "tapanuli selatan": "KABUPATEN TAPANULI SELATAN",
    "jakpus": "KOTA ADMINISTRASI JAKARTA PUSAT",
    "jakbar": "KOTA ADMINISTRASI JAKARTA BARAT",
    "jaksel": "KOTA ADMINISTRASI JAKARTA SELATAN",
    "jaktim": "KOTA ADMINISTRASI JAKARTA TIMUR",
    "jakut": "KOTA ADMINISTRASI JAKARTA UTARA",
}


def _contains_word(text, keyword):
    pattern = r"\b" + re.escape(keyword.lower()) + r"\b"
    return re.search(pattern, text.lower()) is not None


def ambil_provinsi_dari_pertanyaan(pertanyaan):
    q = pertanyaan.lower()

    for keyword, provinsi in sorted(PROVINSI_MAP.items(), key=lambda x: len(x[0]), reverse=True):
        if _contains_word(q, keyword):
            return provinsi

    return None


def ambil_kota_dari_pertanyaan(pertanyaan, daftar):
    q = pertanyaan.lower()
    hasil = []
    sudah = set()

    for alias, nama_resmi in KOTA_ALIAS.items():
        if _contains_word(q, alias):
            hasil.append(nama_resmi)
            sudah.add(nama_resmi)

    for item in daftar:
        kota = (
            item.get("kota")
            or item.get("city")
            or item.get("kabupaten")
            or item.get("kabupaten_kota")
            or ""
        ).strip()

        if not kota:
            continue

        kota_upper = kota.upper()
        kota_lower = kota.lower()

        nama_bersih = (
            kota_lower
            .replace("kabupaten ", "")
            .replace("kab. ", "")
            .replace("kab ", "")
            .replace("kota administrasi ", "")
            .replace("kota ", "")
            .replace("kot. ", "")
            .strip()
        )

        pola = [
            kota_lower,
            nama_bersih,
            f"kabupaten {nama_bersih}",
            f"kab. {nama_bersih}",
            f"kab {nama_bersih}",
            f"kota {nama_bersih}",
            f"kota administrasi {nama_bersih}",
        ]

        for p in pola:
            if p and _contains_word(q, p):
                if kota_upper not in sudah:
                    hasil.append(kota_upper)
                    sudah.add(kota_upper)
                break

    return hasil


def ambil_kecamatan_dari_pertanyaan(pertanyaan, daftar):
    q = pertanyaan.lower()
    hasil = []
    sudah = set()

    for item in daftar:
        kec = (item.get("kecamatan") or item.get("district") or "").strip()
        if not kec:
            continue

        kec_upper = kec.upper()
        kec_lower = kec.lower()

        if kec_upper not in sudah and _contains_word(q, kec_lower):
            hasil.append(kec_upper)
            sudah.add(kec_upper)

    return hasil


def ambil_kelurahan_dari_pertanyaan(pertanyaan, daftar):
    q = pertanyaan.lower()
    hasil = []
    sudah = set()

    for item in daftar:
        kel = (item.get("kelurahan") or item.get("ward") or item.get("desa") or "").strip()
        if not kel:
            continue

        kel_upper = kel.upper()
        kel_lower = kel.lower()

        if kel_upper not in sudah and _contains_word(q, kel_lower):
            hasil.append(kel_upper)
            sudah.add(kel_upper)

    return hasil


def ambil_ruas_jalan_dari_pertanyaan(pertanyaan, daftar):
    q = pertanyaan.lower()
    hasil = []
    sudah = set()

    for item in daftar:
        jalan = (item.get("road") or item.get("jalan") or "").strip()
        if not jalan:
            continue

        jalan_upper = jalan.upper()
        jalan_lower = jalan.lower()

        if jalan_upper not in sudah and jalan_lower in q:
            hasil.append(jalan_upper)
            sudah.add(jalan_upper)

    return hasil


def ekstrak_lokasi(pertanyaan, daftar):
    return {
        "provinsi": ambil_provinsi_dari_pertanyaan(pertanyaan),
        "kota": ambil_kota_dari_pertanyaan(pertanyaan, daftar),
        "kecamatan": ambil_kecamatan_dari_pertanyaan(pertanyaan, daftar),
        "kelurahan": ambil_kelurahan_dari_pertanyaan(pertanyaan, daftar),
        "jalan": ambil_ruas_jalan_dari_pertanyaan(pertanyaan, daftar),
    }
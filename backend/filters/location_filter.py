"""
location_filter.py
Semua fungsi yang berhubungan dengan lokasi berada di sini.
"""

# ===========================
# Mapping Provinsi
# ===========================

PROVINSI_MAP = {

    # SUMATERA
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
    "bangka belitung": "KEPULAUAN BANGKA BELITUNG",
    "bengkulu": "BENGKULU",
    "lampung": "LAMPUNG",

    # JAWA
    "jakarta": "DKI JAKARTA",
    "dki": "DKI JAKARTA",
    "dki jakarta": "DKI JAKARTA",
    "banten": "BANTEN",
    "jawa barat": "JAWA BARAT",
    "jabar": "JAWA BARAT",
    "jawa tengah": "JAWA TENGAH",
    "jateng": "JAWA TENGAH",
    "jawa timur": "JAWA TIMUR",
    "jatim": "JAWA TIMUR",
    "jogja": "DI YOGYAKARTA",
    "jogya": "DI YOGYAKARTA",
    "yogyakarta": "DI YOGYAKARTA",
    "di yogyakarta": "DI YOGYAKARTA",
    "diy": "DI YOGYAKARTA",

    # BALI & NUSA TENGGARA
    "bali": "BALI",
    "ntb": "NUSA TENGGARA BARAT",
    "nusa tenggara barat": "NUSA TENGGARA BARAT",
    "ntt": "NUSA TENGGARA TIMUR",
    "nusa tenggara timur": "NUSA TENGGARA TIMUR",

    # KALIMANTAN
    "kalimantan barat": "KALIMANTAN BARAT",
    "kalbar": "KALIMANTAN BARAT",
    "kalimantan tengah": "KALIMANTAN TENGAH",
    "kalteng": "KALIMANTAN TENGAH",
    "kalimantan selatan": "KALIMANTAN SELATAN",
    "kalsel": "KALIMANTAN SELATAN",
    "kalimantan timur": "KALIMANTAN TIMUR",
    "kaltim": "KALIMANTAN TIMUR",
    "kalimantan utara": "KALIMANTAN UTARA",
    "kalut": "KALIMANTAN UTARA",

    # SULAWESI
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

    # MALUKU
    "maluku": "MALUKU",
    "maluku utara": "MALUKU UTARA",
    "malut": "MALUKU UTARA",

    # PAPUA
    "papua": "PAPUA",
    "papua barat": "PAPUA BARAT",
    "pabar": "PAPUA BARAT",
    "papua selatan": "PAPUA SELATAN", 
    "pasel": "PAPUA SELATAN",
    "papua tengah": "PAPUA TENGAH",
    "pateng": "PAPUA TENGAH",
    "papua pegunungan": "PAPUA PEGUNUNGAN",
    "papeg": "PAPUA PEGUNUNGAN",
    "papua barat daya": "PAPUA BARAT DAYA",
    "pbd": "PAPUA BARAT DAYA",
    "pabadi": "PAPUA BARAT DAYA",
    "Pabdang": "PAPUA BARAT DAYA",
}

# ===========================
# Provinsi
# ===========================

def ambil_provinsi_dari_pertanyaan(pertanyaan):

    q = pertanyaan.lower()

    for keyword, provinsi in PROVINSI_MAP.items():

        if keyword in q:
            return provinsi

    return None


# ===========================
# Kota / Kabupaten
# ===========================

def ambil_kota_dari_pertanyaan(pertanyaan, daftar):

    pertanyaan = pertanyaan.lower()

    kota_ditemukan = []

    sudah_ada = set()

    for item in daftar:

        kota = (item.get("city") or "").strip()

        if not kota:
            continue

        kota_upper = kota.upper()

        if kota_upper in sudah_ada:
            continue

        kota_lower = kota.lower()

        variasi = [

            kota_lower,

            kota_lower.replace("kabupaten ", ""),

            kota_lower.replace("kab. ", ""),

            kota_lower.replace("kab ", ""),

            kota_lower.replace("kota ", ""),

            kota_lower.replace("kot. ", ""),

        ]

        for nama in variasi:

            nama = nama.strip()

            if nama and nama in pertanyaan:

                kota_ditemukan.append(kota_upper)

                sudah_ada.add(kota_upper)

                break

    return kota_ditemukan


# ===========================
# Kecamatan
# ===========================

def ambil_kecamatan_dari_pertanyaan(pertanyaan, daftar):

    pertanyaan = pertanyaan.lower()

    hasil = []

    sudah = set()

    for item in daftar:

        kec = (item.get("district") or "").strip()

        if not kec:
            continue

        kec_upper = kec.upper()

        if kec_upper in sudah:
            continue

        if kec.lower() in pertanyaan:

            hasil.append(kec_upper)

            sudah.add(kec_upper)

    return hasil


# ===========================
# Kelurahan
# ===========================

def ambil_kelurahan_dari_pertanyaan(pertanyaan, daftar):

    pertanyaan = pertanyaan.lower()

    hasil = []

    sudah = set()

    for item in daftar:

        kel = (item.get("ward") or "").strip()

        if not kel:
            continue

        kel_upper = kel.upper()

        if kel_upper in sudah:
            continue

        if kel.lower() in pertanyaan:

            hasil.append(kel_upper)

            sudah.add(kel_upper)

    return hasil


# ===========================
# Jalan
# ===========================

def ambil_ruas_jalan_dari_pertanyaan(pertanyaan, daftar):

    pertanyaan = pertanyaan.lower()

    hasil = []

    sudah = set()

    for item in daftar:

        jalan = (item.get("road") or "").strip()

        if not jalan:
            continue

        jalan_upper = jalan.upper()

        if jalan_upper in sudah:
            continue

        if jalan.lower() in pertanyaan:

            hasil.append(jalan_upper)

            sudah.add(jalan_upper)

    return hasil


# ===========================
# Semua Lokasi
# ===========================

def ekstrak_lokasi(pertanyaan, daftar):

    return {

        "provinsi": ambil_provinsi_dari_pertanyaan(
            pertanyaan
        ),

        "kota": ambil_kota_dari_pertanyaan(
            pertanyaan,
            daftar
        ),

        "kecamatan": ambil_kecamatan_dari_pertanyaan(
            pertanyaan,
            daftar
        ),

        "kelurahan": ambil_kelurahan_dari_pertanyaan(
            pertanyaan,
            daftar
        ),

        "jalan": ambil_ruas_jalan_dari_pertanyaan(
            pertanyaan,
            daftar
        ),

    }
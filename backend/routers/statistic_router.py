"""
Statistics Router
AI SINTA - SITABA

Router untuk statistik kebencanaan.
"""

from services.sitaba_service import (
    get_bencana_terkini,
    ambil_list_bencana,
)

from filters.disaster_filter import filter_bencana

from formatter.statistics_formatter import (
    format_statistik_bencana,
)


# ==========================================================
# Statistik Semua
# ==========================================================

def proses_statistik(pertanyaan: str):

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil, filter_info = filter_bencana(
        daftar,
        pertanyaan
    )

    return format_statistik_bencana(
        hasil,
        filter_info
    )


# ==========================================================
# Statistik Jenis Bencana
# ==========================================================

def statistik_jenis_bencana(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Provinsi
# ==========================================================

def statistik_provinsi(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Kabupaten/Kota
# ==========================================================

def statistik_kota(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Tahun
# ==========================================================

def statistik_tahun(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Bulan
# ==========================================================

def statistik_bulan(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Infrastruktur
# ==========================================================

def statistik_infrastruktur(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Jalan
# ==========================================================

def statistik_jalan(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Personel
# ==========================================================

def statistik_personel(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Material
# ==========================================================

def statistik_material(pertanyaan: str):

    return proses_statistik(pertanyaan)


# ==========================================================
# Statistik Alat
# ==========================================================

def statistik_alat(pertanyaan: str):

    return proses_statistik(pertanyaan)
"""
Disaster Router
Menghubungkan API SITABA, filter bencana, dan formatter jawaban bencana.
"""

from services.sitaba_service import get_bencana_terkini, ambil_list_bencana
from filters.disaster_filter import filter_bencana
from formatter.disaster_formatter import format_jawaban_bencana
from formatter.statistics_formatter import format_statistik_bencana
from formatter.infrastructure_formatter import format_infrastruktur_dari_bencana


def proses_data_bencana(pertanyaan: str):
    data_api = get_bencana_terkini()
    daftar = ambil_list_bencana(data_api)

    hasil, filter_info = filter_bencana(
        daftar,
        pertanyaan
    )

    return format_jawaban_bencana(
        hasil,
        filter_info
    )


def proses_statistik_bencana(pertanyaan: str):
    data_api = get_bencana_terkini()
    daftar = ambil_list_bencana(data_api)

    hasil, filter_info = filter_bencana(
        daftar,
        pertanyaan
    )

    return format_statistik_bencana(
        hasil,
        filter_info
    )


def proses_infrastruktur_bencana(pertanyaan: str):
    data_api = get_bencana_terkini()
    daftar = ambil_list_bencana(data_api)

    hasil, filter_info = filter_bencana(
        daftar,
        pertanyaan
    )

    return format_infrastruktur_dari_bencana(
        hasil
    )
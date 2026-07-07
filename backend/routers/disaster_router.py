"""
Disaster Router
Menghubungkan API SITABA, filter bencana, dan formatter jawaban bencana.
"""

from services.sitaba_service import get_bencana_terkini, ambil_list_bencana
from filters.disaster_filter import filter_bencana
from formatter.disaster_formatter import format_jawaban_bencana
from formatter.statistics_formatter import format_statistik_bencana
from formatter.infrastructure_formatter import format_infrastruktur_dari_bencana


def ambil_nama_wilayah(filter_info):
    if not filter_info:
        return "wilayah yang diminta"

    if filter_info.get("kecamatan"):
        return "Kecamatan " + ", ".join(filter_info.get("kecamatan"))

    if filter_info.get("kelurahan"):
        return "Kelurahan/Desa " + ", ".join(filter_info.get("kelurahan"))

    if filter_info.get("kota"):
        return "Kabupaten/Kota " + ", ".join(filter_info.get("kota"))

    if filter_info.get("provinsi"):
        return "Provinsi " + filter_info.get("provinsi")

    if filter_info.get("jalan"):
        return "Jalan " + ", ".join(filter_info.get("jalan"))

    return "wilayah yang diminta"


def jawaban_tidak_ada_bencana(filter_info):
    wilayah = ambil_nama_wilayah(filter_info)

    return {
        "reply": (
            f"Tidak terdapat kejadian bencana yang tercatat di {wilayah} "
            f"berdasarkan data SITABA saat ini."
        ),
        "attachments": []
    }


def perlu_jawab_tidak_ada_bencana(hasil, filter_info):
    if not filter_info:
        return False

    ada_filter_lokasi = filter_info.get("ada_filter_lokasi", False)

    if ada_filter_lokasi and not hasil:
        return True

    return False


def proses_data_bencana(pertanyaan: str):
    data_api = get_bencana_terkini()
    daftar = ambil_list_bencana(data_api)

    hasil, filter_info = filter_bencana(daftar, pertanyaan)

    if perlu_jawab_tidak_ada_bencana(hasil, filter_info):
        return jawaban_tidak_ada_bencana(filter_info)

    return format_jawaban_bencana(hasil, filter_info)


def proses_statistik_bencana(pertanyaan: str):
    data_api = get_bencana_terkini()
    daftar = ambil_list_bencana(data_api)

    hasil, filter_info = filter_bencana(daftar, pertanyaan)

    if perlu_jawab_tidak_ada_bencana(hasil, filter_info):
        return jawaban_tidak_ada_bencana(filter_info)

    return format_statistik_bencana(hasil, filter_info)


def proses_infrastruktur_bencana(pertanyaan: str):
    data_api = get_bencana_terkini()
    daftar = ambil_list_bencana(data_api)

    hasil, filter_info = filter_bencana(daftar, pertanyaan)

    if perlu_jawab_tidak_ada_bencana(hasil, filter_info):
        return jawaban_tidak_ada_bencana(filter_info)

    return format_infrastruktur_dari_bencana(hasil)
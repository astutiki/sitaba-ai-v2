"""
Resource Router
AI SINTA - SITABA
"""

from services.sitaba_service import get_personel, get_alat, get_material
from formatter.resource_formatter import format_resource
from filters.location_filter import ekstrak_lokasi


def filter_resource_by_location(data_list, pertanyaan):
    lokasi = ekstrak_lokasi(pertanyaan, data_list)

    provinsi_dicari = lokasi.get("provinsi")
    kota_dicari = lokasi.get("kota") or []

    hasil = []

    for item in data_list:
        provinsi_data = (
            item.get("province")
            or item.get("provinsi")
            or ""
        ).upper()

        kota_data = (
            item.get("city")
            or item.get("kota")
            or ""
        ).upper()

        if provinsi_dicari and provinsi_data != provinsi_dicari:
            continue

        if kota_dicari:
            cocok_kota = False

            for kota_target in kota_dicari:
                if kota_target in kota_data or kota_data in kota_target:
                    cocok_kota = True
                    break

            if not cocok_kota:
                continue

        hasil.append(item)

    return hasil


def proses_personel(pertanyaan):
    data = get_personel()

    if not data:
        return "Data personel belum tersedia."

    hasil = filter_resource_by_location(data, pertanyaan)

    if not hasil:
        return "Data personel sesuai lokasi yang diminta belum tersedia."

    return format_resource(hasil, "Personel")


def proses_alat(pertanyaan):
    data = get_alat()

    if not data:
        return "Data alat belum tersedia."

    hasil = filter_resource_by_location(data, pertanyaan)

    if not hasil:
        return "Data alat sesuai lokasi yang diminta belum tersedia."

    return format_resource(hasil, "Alat")


def proses_material(pertanyaan):
    data = get_material()

    if not data:
        return "Data material/bahan belum tersedia."

    hasil = filter_resource_by_location(data, pertanyaan)

    if not hasil:
        return "Data material/bahan sesuai lokasi yang diminta belum tersedia."

    return format_resource(hasil, "Material/Bahan")


def proses_resource(pertanyaan: str):
    q = pertanyaan.lower()

    jawaban = []

    if "personel" in q:
        jawaban.append(proses_personel(pertanyaan))

    if (
        "alat" in q
        or "alat berat" in q
        or "excavator" in q
        or "dump truck" in q
        or "pompa" in q
        or "genset" in q
    ):
        jawaban.append(proses_alat(pertanyaan))

    if (
        "bahan" in q
        or "material" in q
        or "logistik" in q
    ):
        jawaban.append(proses_material(pertanyaan))

    if jawaban:
        return "\n\n".join(jawaban)

    return (
        "Silakan sebutkan jenis sumber daya yang ingin dicari, "
        "misalnya personel, alat, bahan, material, atau logistik."
    )
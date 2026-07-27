"""
Resource Router
AI SINTA - SITABA
"""

import re

from services.sitaba_service import (
    get_personel,
    get_alat,
    get_material,
)

from services.sitaba_public_service import cari_aset

from filters.location_filter import ekstrak_lokasi

from formatters.resource_formatter import (
    format_resource,
    format_aset_sitaba,
)


def normalisasi_pencarian_aset(value) -> str:
    """
    Menyamakan huruf, tanda baca, dan spasi agar pencarian
    unit kerja/aset tidak sensitif terhadap koma dan kapital.
    """

    teks = str(value or "").casefold()

    teks = re.sub(
        r"[^\w\s]",
        " ",
        teks,
    )

    return " ".join(teks.split())


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
                if (
                    kota_target in kota_data
                    or kota_data in kota_target
                ):
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

    hasil = filter_resource_by_location(
        data,
        pertanyaan,
    )

    if not hasil:
        return (
            "Data personel sesuai lokasi yang diminta "
            "belum tersedia."
        )

    return format_resource(
        hasil,
        "Personel",
    )


def proses_alat(pertanyaan):
    data = get_alat()

    if not data:
        return "Data alat belum tersedia."

    hasil = filter_resource_by_location(
        data,
        pertanyaan,
    )

    if not hasil:
        return (
            "Data alat sesuai lokasi yang diminta "
            "belum tersedia."
        )

    return format_resource(
        hasil,
        "Alat",
    )


def proses_material(pertanyaan):
    data = get_material()

    if not data:
        return "Data material/bahan belum tersedia."

    hasil = filter_resource_by_location(
        data,
        pertanyaan,
    )

    if not hasil:
        return (
            "Data material/bahan sesuai lokasi yang "
            "diminta belum tersedia."
        )

    return format_resource(
        hasil,
        "Material/Bahan",
    )


def proses_aset_sitaba(user_message: str):
    """
    Pencarian aset SITABA berdasarkan:

    1. Jenis, kelas, atau model aset.
    2. Unit kerja (unker).
    3. Unit organisasi (unor).
    4. Gabungan jenis aset dan unit kerja.

    Berlaku dinamis untuk seluruh balai di Indonesia.
    """

    q = normalisasi_pencarian_aset(user_message)

    kata_pembuang = [
        "ada berapa",
        "berapa jumlah",
        "berapa banyak",
        "berapa",
        "jumlah",
        "tolong tampilkan",
        "tolong sebutkan",
        "tampilkan",
        "sebutkan",
        "daftar",
        "data",
        "apa saja",
        "jenis apa saja",
        "yang tersedia",
        "tersedia",
        "di sitaba",
        "pada sitaba",
        "sitaba",
        "aset",
        "asset",
    ]

    teks_bersih = q

    for kata in kata_pembuang:
        teks_bersih = teks_bersih.replace(
            kata,
            " ",
        )

    teks_bersih = " ".join(
        teks_bersih.split()
    )

    keyword_aset = None
    keyword_unit = None

    # Contoh:
    # "aset di Balai Besar Wilayah Sungai Brantas"
    # menjadi:
    # keyword_aset = None
    # keyword_unit = "balai besar wilayah sungai brantas"
    if teks_bersih.startswith("di "):
        keyword_unit = (
            teks_bersih[3:].strip()
            or None
        )

    # Contoh:
    # "pompa di Balai Besar Wilayah Sungai Brantas"
    # menjadi:
    # keyword_aset = "pompa"
    # keyword_unit = "balai besar wilayah sungai brantas"
    elif " di " in teks_bersih:
        bagian_aset, bagian_unit = teks_bersih.split(
            " di ",
            1,
        )

        keyword_aset = (
            bagian_aset.strip()
            or None
        )

        keyword_unit = (
            bagian_unit.strip()
            or None
        )

    # Contoh:
    # "mobil toilet"
    # "pompa portable"
    # "kendaraan pelayanan khusus"
    else:
        keyword_aset = (
            teks_bersih
            or None
        )

    print("KEYWORD ASET:", keyword_aset)
    print("KEYWORD UNIT:", keyword_unit)

    # Jika jenis aset kosong, ambil seluruh aset.
    # Jika jenis aset ada, cari jenis aset terlebih dahulu.
    hasil_api = cari_aset(
        keyword=keyword_aset,
    )

    if hasil_api.get("success"):
        data_aset = hasil_api.get(
            "data",
            [],
        )

        if keyword_unit:
            unit_dicari = (
                normalisasi_pencarian_aset(
                    keyword_unit
                )
            )

            kata_unit_dicari = (
                unit_dicari.split()
            )

            hasil_filter_unit = []

            for item in data_aset:
                teks_unit_data = (
                    normalisasi_pencarian_aset(
                        " ".join(
                            [
                                str(
                                    item.get(
                                        "unker"
                                    )
                                    or ""
                                ),
                                str(
                                    item.get(
                                        "unor"
                                    )
                                    or ""
                                ),
                            ]
                        )
                    )
                )

                cocok_frasa = (
                    unit_dicari
                    in teks_unit_data
                )

                cocok_semua_kata = all(
                    kata in teks_unit_data
                    for kata in kata_unit_dicari
                )

                if (
                    cocok_frasa
                    or cocok_semua_kata
                ):
                    hasil_filter_unit.append(
                        item
                    )

            data_aset = hasil_filter_unit

        hasil_api["data"] = data_aset
        hasil_api["count"] = len(
            data_aset
        )

    print(
        "HASIL API ASET:",
        hasil_api.get("success"),
        hasil_api.get("status_code"),
        hasil_api.get("error"),
        hasil_api.get("count"),
    )

    if keyword_aset and keyword_unit:
        keyword_tampilan = (
            f"{keyword_aset} di {keyword_unit}"
        )

    elif keyword_unit:
        keyword_tampilan = (
            f"unit kerja {keyword_unit}"
        )

    else:
        keyword_tampilan = keyword_aset

    return {
        "reply": format_aset_sitaba(
            hasil_api,
            keyword=keyword_tampilan,
        ),
        "attachments": [],
        "source": (
            "SITABA API Public - list-assets"
        ),
        "data": hasil_api.get(
            "data",
            [],
        ),
    }


def proses_resource(user_message: str):
    q = normalisasi_pencarian_aset(
        user_message
    )

    asset_keywords = [
        "aset",
        "asset",
        "mobil toilet",
        "toilet",
        "pompa",
        "pompa portable",
        "pompa alkon",
        "kendaraan pelayanan khusus",
        "balai",
        "bbws",
        "bws",
        "unit kerja",
        "unit organisasi",
        "direktorat jenderal",
        "ditjen",
    ]

    # Jalur API aset baru diperiksa terlebih dahulu.
    if any(
        keyword in q
        for keyword in asset_keywords
    ):
        return proses_aset_sitaba(
            user_message
        )

    # Fungsi lama tetap dipertahankan.
    jawaban = []

    if "personel" in q:
        jawaban.append(
            proses_personel(
                user_message
            )
        )

    if (
        "alat" in q
        or "alat berat" in q
        or "excavator" in q
        or "dump truck" in q
        or "genset" in q
    ):
        jawaban.append(
            proses_alat(
                user_message
            )
        )

    if (
        "bahan" in q
        or "material" in q
        or "logistik" in q
    ):
        jawaban.append(
            proses_material(
                user_message
            )
        )

    if jawaban:
        return "\n\n".join(
            jawaban
        )

    return (
        "Silakan sebutkan jenis sumber daya yang ingin dicari, "
        "misalnya personel, alat, bahan, material, logistik, "
        "atau aset SITABA."
    )
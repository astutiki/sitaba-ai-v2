from typing import Any, Optional

import requests

from config import (
    SITABA_NEW_DISASTER_API,
    SITABA_ASSET_API,
    SITABA_EARTHQUAKE_API,
)


DEFAULT_TIMEOUT = 30


def ekstrak_list_data(payload: Any) -> list[dict]:
    """
    Mengambil daftar data dari berbagai kemungkinan struktur JSON API.
    """

    if isinstance(payload, list):
        return [
            item
            for item in payload
            if isinstance(item, dict)
        ]

    if not isinstance(payload, dict):
        return []

    kandidat_keys = [
        "data",
        "result",
        "results",
        "items",
        "records",
        "assets",
        "earthquakes",
        "gempa",
        "disasters",
        "bencana",
    ]

    for key in kandidat_keys:
        value = payload.get(key)

        if isinstance(value, list):
            return [
                item
                for item in value
                if isinstance(item, dict)
            ]

        if isinstance(value, dict):
            nested_candidates = [
                value.get("data"),
                value.get("items"),
                value.get("results"),
                value.get("records"),
            ]

            for nested_data in nested_candidates:
                if isinstance(nested_data, list):
                    return [
                        item
                        for item in nested_data
                        if isinstance(item, dict)
                    ]

    return []


def request_api_get(
    url: str,
    params: Optional[dict] = None,
) -> dict:
    """
    Fungsi GET umum untuk API SITABA.

    Fungsi selalu mengembalikan dictionary agar error API
    tidak menyebabkan aplikasi langsung crash.
    """

    headers = {
        "Accept": "application/json",
        "User-Agent": "SITABA-AI/1.0",
    }

    try:
        response = requests.get(
            url,
            params=params or {},
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        payload = response.json()
        data = ekstrak_list_data(payload)

        return {
            "success": True,
            "status_code": response.status_code,
            "payload": payload,
            "data": data,
            "count": len(data),
            "error": None,
        }

    except requests.Timeout:
        return {
            "success": False,
            "status_code": None,
            "payload": None,
            "data": [],
            "count": 0,
            "error": (
                "Permintaan ke API SITABA mengalami timeout."
            ),
        }

    except requests.RequestException as error:
        status_code = None
        response_text = None

        if error.response is not None:
            status_code = error.response.status_code
            response_text = error.response.text

        return {
            "success": False,
            "status_code": status_code,
            "payload": None,
            "data": [],
            "count": 0,
            "error": str(error),
            "response_text": response_text,
        }

    except ValueError:
        return {
            "success": False,
            "status_code": None,
            "payload": None,
            "data": [],
            "count": 0,
            "error": (
                "Respons API SITABA bukan JSON yang valid."
            ),
        }


def request_api_get_with_trailing_slash(
    url: str,
    params: Optional[dict] = None,
) -> dict:
    """
    Memanggil endpoint utama.

    Jika mendapat status 404, fungsi mencoba kembali dengan
    trailing slash.
    """

    hasil = request_api_get(
        url,
        params=params,
    )

    if (
        not hasil.get("success")
        and hasil.get("status_code") == 404
        and not url.endswith("/")
    ):
        hasil = request_api_get(
            f"{url}/",
            params=params,
        )

    return hasil


# =========================================================
# PENGAMBILAN DATA API
# =========================================================


def ambil_semua_bencana(
    params: Optional[dict] = None,
) -> dict:
    """
    Mengambil data kejadian bencana umum dari API SITABA.
    """

    return request_api_get_with_trailing_slash(
        SITABA_NEW_DISASTER_API,
        params=params,
    )


def ambil_semua_aset(
    params: Optional[dict] = None,
) -> dict:
    """
    Mengambil data aset atau sumber daya dari API SITABA.
    """

    return request_api_get_with_trailing_slash(
        SITABA_ASSET_API,
        params=params,
    )


def ambil_semua_gempa(
    params: Optional[dict] = None,
) -> dict:
    """
    Mengambil data gempa bumi dari API SITABA.
    """

    return request_api_get_with_trailing_slash(
        SITABA_EARTHQUAKE_API,
        params=params,
    )


# =========================================================
# FUNGSI PENCARIAN UMUM
# =========================================================


def normalisasi_teks(value: Any) -> str:
    """
    Mengubah nilai menjadi teks lowercase yang aman dicari.
    """

    if value is None:
        return ""

    return str(value).strip().casefold()


def flatten_values(value: Any) -> list[str]:
    """
    Mengubah dictionary atau list bertingkat menjadi kumpulan teks.
    """

    hasil: list[str] = []

    if isinstance(value, dict):
        for child_value in value.values():
            hasil.extend(
                flatten_values(child_value)
            )

    elif isinstance(value, list):
        for child_value in value:
            hasil.extend(
                flatten_values(child_value)
            )

    elif isinstance(
        value,
        (str, int, float, bool),
    ):
        hasil.append(str(value))

    return hasil


def buat_searchable_text(item: dict) -> str:
    """
    Menggabungkan seluruh nilai item menjadi satu teks pencarian.
    """

    return " ".join(
        flatten_values(item)
    ).casefold()


def filter_data_api(
    data: list[dict],
    keyword: Optional[str] = None,
    provinsi: Optional[str] = None,
    kota: Optional[str] = None,
    tahun: Optional[str] = None,
) -> list[dict]:
    """
    Memfilter data API berdasarkan keyword, provinsi, kota, dan tahun.
    """

    keyword_normal = normalisasi_teks(keyword)
    provinsi_normal = normalisasi_teks(provinsi)
    kota_normal = normalisasi_teks(kota)
    tahun_normal = normalisasi_teks(tahun)

    hasil: list[dict] = []

    for item in data:
        if not isinstance(item, dict):
            continue

        searchable_text = buat_searchable_text(
            item
        )

        kondisi_keyword = (
            not keyword_normal
            or keyword_normal in searchable_text
        )

        kondisi_provinsi = (
            not provinsi_normal
            or provinsi_normal in searchable_text
        )

        kondisi_kota = (
            not kota_normal
            or kota_normal in searchable_text
        )

        kondisi_tahun = (
            not tahun_normal
            or tahun_normal in searchable_text
        )

        if (
            kondisi_keyword
            and kondisi_provinsi
            and kondisi_kota
            and kondisi_tahun
        ):
            hasil.append(item)

    return hasil


def terapkan_filter(
    response: dict,
    keyword: Optional[str] = None,
    provinsi: Optional[str] = None,
    kota: Optional[str] = None,
    tahun: Optional[str] = None,
) -> dict:
    """
    Menerapkan filter ke hasil API dengan format respons yang konsisten.
    """

    if not response.get("success"):
        return response

    data = response.get("data", [])

    hasil_filter = filter_data_api(
        data=data,
        keyword=keyword,
        provinsi=provinsi,
        kota=kota,
        tahun=tahun,
    )

    response["data"] = hasil_filter
    response["count"] = len(hasil_filter)

    return response


# =========================================================
# PENCARIAN BENCANA
# =========================================================


def cari_bencana(
    keyword: Optional[str] = None,
    provinsi: Optional[str] = None,
    kota: Optional[str] = None,
    tahun: Optional[str] = None,
) -> dict:
    """
    Mencari data bencana umum pada API new-disaster.
    """

    response = ambil_semua_bencana()

    return terapkan_filter(
        response=response,
        keyword=keyword,
        provinsi=provinsi,
        kota=kota,
        tahun=tahun,
    )


# =========================================================
# PENCARIAN ASET
# =========================================================


def cari_aset(
    keyword: Optional[str] = None,
    provinsi: Optional[str] = None,
    kota: Optional[str] = None,
) -> dict:
    """
    Mencari data aset atau sumber daya SITABA.
    """

    response = ambil_semua_aset()

    return terapkan_filter(
        response=response,
        keyword=keyword,
        provinsi=provinsi,
        kota=kota,
    )


# =========================================================
# PENCARIAN GEMPA
# =========================================================


def cari_gempa(
    keyword: Optional[str] = None,
    provinsi: Optional[str] = None,
    kota: Optional[str] = None,
    tahun: Optional[str] = None,
) -> dict:
    """
    Mencari data gempa bumi SITABA.
    """

    response = ambil_semua_gempa()

    return terapkan_filter(
        response=response,
        keyword=keyword,
        provinsi=provinsi,
        kota=kota,
        tahun=tahun,
    )
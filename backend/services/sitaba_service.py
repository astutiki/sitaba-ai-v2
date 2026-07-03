import requests
from config import SITABA_NEW_DISASTER_API

def get_bencana_terkini():
    try:
        response = requests.get(SITABA_NEW_DISASTER_API, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("ERROR API SITABA:", e)
        return None


def ambil_list_bencana(data):
    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for key in ["data", "result", "results", "items", "records"]:
            if key in data and isinstance(data[key], list):
                return data[key]

        for value in data.values():
            if isinstance(value, list):
                return value

    return []


def normalisasi_bencana(item):
    return {
        "jenis": item.get("category") or item.get("child_category") or "Jenis bencana tidak tersedia",
        "sub_jenis": item.get("child_category") or "",
        "tanggal": item.get("report_date") or item.get("date_time") or "",
        "provinsi": item.get("province") or "",
        "kota": item.get("city") or "",
        "kecamatan": item.get("district") or "",
        "kelurahan": item.get("ward") or "",
        "lokasi": item.get("location") or "",
        "nama": item.get("name") or "",
        "status": item.get("status") or "",
        "current_status": item.get("current_status") or "",
        "damage": item.get("damage") or "",
        "cause": item.get("cause") or "",
        "needs": item.get("needs") or "",
        "road": item.get("road") or "",
        "infrastructure": item.get("infrastructure") or [],
        "disaster_handling": item.get("disaster_handling") or [],
        "disaster_pic": item.get("disaster_pic") or {},
    }

SITABA_PERSONEL_API = "https://sitaba.pu.go.id/api-public/noauth/list-assets"
SITABA_ALAT_API = "https://sitaba.pu.go.id/api-public/noauth/list-assets"
SITABA_MATERIAL_API = "https://sitaba.pu.go.id/api-public/noauth/list-assets/"
SITABA_ASSETS_API = "https://sitaba.pu.go.id/api-public/noauth/list-assets"



def get_api_data(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            for key in ["data", "result", "results", "items", "records"]:
                if key in data and isinstance(data[key], list):
                    return data[key]

        return []

    except Exception as e:
        print("ERROR API:", e)
        return []


def get_personel():
    return get_api_data(SITABA_PERSONEL_API)


def get_alat():
    return get_api_data(SITABA_ALAT_API)


def get_material():
    return get_api_data(SITABA_MATERIAL_API)




def get_list_assets():
    return get_api_data(SITABA_ASSETS_API)


def get_personel():
    data = get_list_assets()

    hasil = []
    for item in data:
        tipe = (
            item.get("type")
            or item.get("category")
            or item.get("asset_type")
            or item.get("jenis")
            or ""
        ).lower()

        if "personel" in tipe or "personil" in tipe:
            hasil.append(item)

    return hasil


def get_alat():
    data = get_list_assets()

    hasil = []
    for item in data:
        tipe = (
            item.get("type")
            or item.get("category")
            or item.get("asset_type")
            or item.get("jenis")
            or ""
        ).lower()

        if "alat" in tipe:
            hasil.append(item)

    return hasil


def get_material():
    data = get_list_assets()

    hasil = []
    for item in data:
        tipe = (
            item.get("type")
            or item.get("category")
            or item.get("asset_type")
            or item.get("jenis")
            or ""
        ).lower()

        if "bahan" in tipe or "material" in tipe or "logistik" in tipe:
            hasil.append(item)

    return hasil
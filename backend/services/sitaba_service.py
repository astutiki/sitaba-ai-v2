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

SITABA_ASSETS_API = "https://sitaba.pu.go.id/api-public/noauth/list-assets"


def get_list_assets():
    return get_api_data(SITABA_ASSETS_API)


def asset_text(item):
    return " ".join([
        str(item.get("type", "")),
        str(item.get("category", "")),
        str(item.get("asset_type", "")),
        str(item.get("jenis", "")),
        str(item.get("name", "")),
        str(item.get("nama", "")),
        str(item.get("description", "")),
        str(item.get("keterangan", "")),
    ]).lower()


def get_personel():
    data = get_list_assets()
    return [
        item for item in data
        if "personel" in asset_text(item) or "personil" in asset_text(item)
    ]


def get_alat():
    data = get_list_assets()
    return [
        item for item in data
        if (
            "alat" in asset_text(item)
            or "excavator" in asset_text(item)
            or "dump truck" in asset_text(item)
            or "pompa" in asset_text(item)
            or "genset" in asset_text(item)
        )
    ]


def get_material():
    data = get_list_assets()
    return [
        item for item in data
        if (
            "bahan" in asset_text(item)
            or "material" in asset_text(item)
            or "logistik" in asset_text(item)
            or "bronjong" in asset_text(item)
            or "karung" in asset_text(item)
            or "terpal" in asset_text(item)
        )
    ]


def debug_assets():
    try:
        response = requests.get(SITABA_ASSETS_API, timeout=30)
        return {
            "status_code": response.status_code,
            "text": response.text[:1000]
        }
    except Exception as e:
        return {"error": str(e)}
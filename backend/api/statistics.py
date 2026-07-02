"""
Statistic API
AI SINTA
"""

from fastapi import APIRouter
from datetime import datetime
from collections import Counter

from services.sitaba_service import (
    get_bencana_terkini,
    ambil_list_bencana,
)

from filters.disaster_filter import filter_bencana

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"]
)


# =====================================================
# SUMMARY
# =====================================================

@router.get("/summary")
def summary():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    return {

        "success": True,

        "total_bencana": len(daftar),

        "timestamp": datetime.now().isoformat()

    }


# =====================================================
# ALL
# =====================================================

@router.get("/all")
def all_statistics():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    jenis = Counter()

    provinsi = Counter()

    kota = Counter()

    for item in daftar:

        jenis[item.get("disaster_type", "-")] += 1

        provinsi[item.get("province", "-")] += 1

        kota[item.get("city", "-")] += 1

    return {

        "success": True,

        "total": len(daftar),

        "jenis_bencana": dict(jenis),

        "provinsi": dict(provinsi),

        "kota": dict(kota)

    }


# =====================================================
# PROVINSI
# =====================================================

@router.get("/province")
def province_statistics():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil = Counter()

    for item in daftar:

        hasil[item.get("province", "-")] += 1

    return {

        "success": True,

        "province": dict(hasil)

    }


# =====================================================
# KOTA
# =====================================================

@router.get("/city")
def city_statistics():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil = Counter()

    for item in daftar:

        hasil[item.get("city", "-")] += 1

    return {

        "success": True,

        "city": dict(hasil)

    }


# =====================================================
# JENIS
# =====================================================

@router.get("/disaster-type")
def disaster_type_statistics():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil = Counter()

    for item in daftar:

        hasil[item.get("disaster_type", "-")] += 1

    return {

        "success": True,

        "data": dict(hasil)

    }


# =====================================================
# FILTER
# =====================================================

@router.get("/filter")
def statistic_filter(question: str):

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil, filter_info = filter_bencana(
        daftar,
        question
    )

    return {

        "success": True,

        "filter": filter_info,

        "total": len(hasil),

        "data": hasil

    }


# =====================================================
# TOP 10 PROVINSI
# =====================================================

@router.get("/top-province")
def top_province():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil = Counter()

    for item in daftar:

        hasil[item.get("province", "-")] += 1

    return {

        "success": True,

        "data": hasil.most_common(10)

    }


# =====================================================
# TOP 10 BENCANA
# =====================================================

@router.get("/top-disaster")
def top_disaster():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    hasil = Counter()

    for item in daftar:

        hasil[item.get("disaster_type", "-")] += 1

    return {

        "success": True,

        "data": hasil.most_common(10)

    }


# =====================================================
# DASHBOARD
# =====================================================

@router.get("/dashboard")
def dashboard():

    data = get_bencana_terkini()

    daftar = ambil_list_bencana(data)

    provinsi = Counter()

    jenis = Counter()

    kota = Counter()

    for item in daftar:

        provinsi[item.get("province", "-")] += 1

        kota[item.get("city", "-")] += 1

        jenis[item.get("disaster_type", "-")] += 1

    return {

        "success": True,

        "summary": {

            "total_bencana": len(daftar),

            "total_provinsi": len(provinsi),

            "total_kota": len(kota),

            "total_jenis": len(jenis)

        },

        "top_province": provinsi.most_common(10),

        "top_city": kota.most_common(10),

        "top_disaster": jenis.most_common(10),

        "generated_at": datetime.now().isoformat()

    }
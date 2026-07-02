"""
Resource Router
AI SINTA - SITABA

Router untuk data sumber daya:
- Personel
- Alat
- Material
- Logistik
"""

from services.sitaba_service import (
    get_personel,
    get_alat,
    get_material,
)

from formatter.resource_formatter import format_resource


# =====================================================
# PERSONEL
# =====================================================

def proses_personel():

    data = get_personel()

    if not data:

        return "Data personel belum tersedia."

    return format_resource(
        data,
        "Personel"
    )


# =====================================================
# ALAT
# =====================================================

def proses_alat():

    data = get_alat()

    if not data:

        return "Data alat belum tersedia."

    return format_resource(
        data,
        "Alat"
    )


# =====================================================
# MATERIAL
# =====================================================

def proses_material():

    data = get_material()

    if not data:

        return "Data material belum tersedia."

    return format_resource(
        data,
        "Material"
    )


# =================================================
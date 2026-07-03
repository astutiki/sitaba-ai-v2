import re
from datetime import datetime, timedelta

BULAN = {
    "januari": "01",
    "februari": "02",
    "maret": "03",
    "april": "04",
    "mei": "05",
    "juni": "06",
    "juli": "07",
    "agustus": "08",
    "september": "09",
    "oktober": "10",
    "november": "11",
    "desember": "12",
}


def deteksi_tahun(text: str):
    text = text.lower()

    hasil = re.search(r"(20\d{2})", text)

    if hasil:
        return hasil.group(1)

    if "tahun lalu" in text:
        return str(datetime.now().year - 1)

    if "tahun ini" in text:
        return str(datetime.now().year)

    return None


def deteksi_bulan(text: str):
    text = text.lower()

    for nama, angka in BULAN.items():
        if nama in text:
            return angka, nama.capitalize()

    return None, None


def deteksi_hari(text: str):
    text = text.lower()
    hari_ini = datetime.now()

    if "hari ini" in text:
        return hari_ini.strftime("%Y-%m-%d")

    if "kemarin" in text:
        return (hari_ini - timedelta(days=1)).strftime("%Y-%m-%d")

    if "besok" in text:
        return (hari_ini + timedelta(days=1)).strftime("%Y-%m-%d")

    return None
from collections import Counter
import re
from html import unescape

def clean_html(raw_text):
    if not raw_text:
        return ""

    text = str(raw_text)
    text = unescape(text)

    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)

    text = text.replace("&nbsp;", " ")
    text = text.replace("ulli", "\n- ")
    text = text.replace("/lili", "\n- ")
    text = text.replace("/li", "")
    text = text.replace("/ul", "")
    text = text.replace("/p", "")

    text = re.sub(r"\s+\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()


def clean_value(value):
    cleaned = clean_html(value)
    return cleaned if cleaned else "-"


def format_jawaban_bencana(hasil, filter_info):

    if not hasil:
        keterangan = []

        if filter_info.get("provinsi"):
            keterangan.append(filter_info["provinsi"])

        if filter_info.get("kota"):
            keterangan.append(", ".join(filter_info["kota"]))

        if filter_info.get("kecamatan"):
            keterangan.append(", ".join(filter_info["kecamatan"]))

        if filter_info.get("bulan_nama"):
            keterangan.append(filter_info["bulan_nama"])

        if filter_info.get("tahun"):
            keterangan.append(str(filter_info["tahun"]))

        lokasi = " ".join(keterangan).strip()

        if lokasi:
            return f"Tidak ditemukan data bencana untuk {lokasi}."

        return "Tidak ditemukan data bencana."

    counter_jenis = Counter()
    counter_provinsi = Counter()
    counter_kota = Counter()
    counter_status = Counter()

    kerusakan = []
    jalan = []

    for item in hasil:
        jenis = clean_value(item.get("jenis"))
        provinsi = clean_value(item.get("provinsi"))
        kota = clean_value(item.get("kota"))
        status = clean_value(item.get("current_status"))
        damage = clean_value(item.get("damage"))
        road = clean_value(item.get("road"))

        if jenis != "-":
            counter_jenis[jenis] += 1

        if provinsi != "-":
            counter_provinsi[provinsi] += 1

        if kota != "-":
            counter_kota[kota] += 1

        if status != "-":
            counter_status[status] += 1

        if damage != "-":
            kerusakan.append(damage)

        if road != "-":
            jalan.append(road)

    teks = ""
    teks += "📍 INFORMASI BENCANA SITABA\n\n"
    teks += f"Total kejadian : {len(hasil)}\n\n"

    if counter_jenis:
        teks += "📌 Jenis Bencana\n"
        for nama, jumlah in counter_jenis.most_common():
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    if counter_provinsi:
        teks += "🗺 Sebaran Provinsi\n"
        for nama, jumlah in counter_provinsi.most_common():
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    if counter_kota:
        teks += "🏙 Kabupaten / Kota\n"
        for nama, jumlah in counter_kota.most_common():
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    if counter_status:
        teks += "🚧 Status Penanganan\n"
        for nama, jumlah in counter_status.most_common():
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    if kerusakan:
        teks += "🏚 Kondisi Kerusakan\n"
        sudah = set()

        for item in kerusakan:
            if item and item not in sudah:
                teks += f"• {item}\n"
                sudah.add(item)

        teks += "\n"

    if jalan:
        teks += "🛣 Ruas Jalan Terdampak\n"
        sudah = set()

        for item in jalan:
            if item and item not in sudah:
                teks += f"• {item}\n"
                sudah.add(item)

        teks += "\n"

    teks += "📋 Detail Kejadian\n\n"

    for i, item in enumerate(hasil[:10], start=1):
        teks += f"{i}. {clean_value(item.get('jenis'))}\n"
        teks += f"   📅 Tanggal    : {clean_value(item.get('tanggal'))}\n"
        teks += f"   📍 Provinsi   : {clean_value(item.get('provinsi'))}\n"
        teks += f"   🏙 Kota       : {clean_value(item.get('kota'))}\n"
        teks += f"   🏘 Kecamatan  : {clean_value(item.get('kecamatan'))}\n"
        teks += f"   📌 Lokasi     : {clean_value(item.get('lokasi'))}\n"

        if item.get("road"):
            teks += f"   🛣 Jalan      : {clean_value(item.get('road'))}\n"

        if item.get("damage"):
            teks += f"   🏚 Kerusakan  : {clean_value(item.get('damage'))}\n"

        if item.get("current_status"):
            teks += f"   🚧 Status     : {clean_value(item.get('current_status'))}\n"

        teks += "\n"

    teks += "──────────────────────────\n"
    teks += "Sumber : API SITABA Kementerian PU"

    return teks

from typing import Any


def ambil_field(
    item: dict,
    kandidat_field: list[str],
    default: str = "-",
) -> str:
    for field in kandidat_field:
        value = item.get(field)

        if value not in (None, "", []):
            return str(value)

    return default


def format_gempa_bumi(
    hasil_api: dict,
    filter_info: dict | None = None,
) -> str:
    filter_info = filter_info or {}

    if not hasil_api.get("success"):
        return (
            "Data gempa bumi SITABA sedang tidak dapat diakses. "
            "Silakan coba kembali."
        )

    data = hasil_api.get("data", [])

    if not data:
        lokasi = (
            filter_info.get("kota")
            or filter_info.get("provinsi")
        )

        tahun = filter_info.get("tahun")

        keterangan_filter = []

        if lokasi:
            keterangan_filter.append(
                f"di {lokasi}"
            )

        if tahun:
            keterangan_filter.append(
                f"pada tahun {tahun}"
            )

        tambahan = ""

        if keterangan_filter:
            tambahan = " " + " ".join(
                keterangan_filter
            )

        return (
            "Tidak ditemukan data gempa bumi"
            f"{tambahan} pada API SITABA."
        )

    lines = [
        "Berikut data gempa bumi dari SITABA:",
        "",
    ]

    batas_tampil = 10

    for nomor, item in enumerate(
        data[:batas_tampil],
        start=1,
    ):
        tanggal = ambil_field(
            item,
            [
                "tanggal",
                "date",
                "datetime",
                "waktu",
                "tgl_gempa",
                "created_at",
            ],
        )

        lokasi = ambil_field(
            item,
            [
                "lokasi",
                "location",
                "wilayah",
                "region",
                "keterangan",
            ],
        )

        magnitudo = ambil_field(
            item,
            [
                "magnitudo",
                "magnitude",
                "mag",
                "skala",
            ],
        )

        kedalaman = ambil_field(
            item,
            [
                "kedalaman",
                "depth",
            ],
        )

        koordinat = ambil_field(
            item,
            [
                "koordinat",
                "coordinates",
                "coordinate",
            ],
        )

        potensi = ambil_field(
            item,
            [
                "potensi",
                "potential",
                "tsunami",
                "status_tsunami",
            ],
        )

        lines.extend(
            [
                f"{nomor}. Gempa bumi",
                f"   Waktu: {tanggal}",
                f"   Lokasi: {lokasi}",
                f"   Magnitudo: {magnitudo}",
                f"   Kedalaman: {kedalaman}",
                f"   Koordinat: {koordinat}",
                f"   Potensi: {potensi}",
                "",
            ]
        )

    total = len(data)

    if total > batas_tampil:
        lines.append(
            f"Menampilkan {batas_tampil} dari "
            f"{total} data gempa bumi."
        )
    else:
        lines.append(
            f"Total ditemukan: {total} data gempa bumi."
        )

    return "\n".join(lines)
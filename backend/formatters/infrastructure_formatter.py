from collections import Counter


def format_infrastruktur(data_list):

    if not data_list:
        return "Tidak ditemukan data infrastruktur terdampak."

    counter_kategori = Counter()
    counter_nama = Counter()
    counter_unit = Counter()

    teks = "🏗 DATA INFRASTRUKTUR TERDAMPAK\n\n"
    teks += f"Total data : {len(data_list)}\n\n"

    for item in data_list:

        kategori = item.get("infrastructure_category") or item.get("category") or ""
        nama = item.get("infrastructure_name") or item.get("name") or ""
        unit = item.get("unit_name") or item.get("unit") or ""

        if kategori:
            counter_kategori[kategori] += 1

        if nama:
            counter_nama[nama] += 1

        if unit:
            counter_unit[unit] += 1

    if counter_kategori:
        teks += "📌 Kategori Infrastruktur\n"
        for nama, jumlah in counter_kategori.most_common():
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    if counter_nama:
        teks += "🏗 Nama Infrastruktur\n"
        for nama, jumlah in counter_nama.most_common(15):
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    teks += "📋 Detail Infrastruktur\n\n"

    for i, item in enumerate(data_list[:20], start=1):

        kategori = item.get("infrastructure_category") or item.get("category") or "-"
        nama = item.get("infrastructure_name") or item.get("name") or "-"
        total = item.get("total") or "-"
        detail = item.get("detail") or "-"
        unit = item.get("unit_name") or item.get("unit") or "-"

        teks += f"{i}. {nama}\n"
        teks += f"   📌 Kategori : {kategori}\n"
        teks += f"   🔢 Total    : {total} {unit}\n"
        teks += f"   📝 Detail   : {detail}\n\n"

    teks += "──────────────────────────\n"
    teks += "Sumber : API SITABA Kementerian PU"

    return teks


def ambil_infrastruktur_dari_bencana(hasil_bencana):

    infrastruktur = []

    for bencana in hasil_bencana:

        daftar = bencana.get("infrastructure") or []

        if isinstance(daftar, list):
            for item in daftar:
                infrastruktur.append(item)

    return infrastruktur


def format_infrastruktur_dari_bencana(hasil_bencana):

    infrastruktur = ambil_infrastruktur_dari_bencana(hasil_bencana)

    return format_infrastruktur(infrastruktur)
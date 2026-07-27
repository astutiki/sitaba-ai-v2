from collections import Counter


def format_berita(data_list):
    if not data_list:
        return "Tidak ditemukan data berita SITABA."

    counter_kategori = Counter()

    teks = "📰 BERITA & INFO SITABA\n\n"
    teks += f"Total berita : {len(data_list)}\n\n"

    for item in data_list:
        kategori = (
            item.get("category")
            or item.get("kategori")
            or item.get("type")
            or "Tidak diketahui"
        )
        counter_kategori[kategori] += 1

    if counter_kategori:
        teks += "📌 Kategori Berita\n"
        for nama, jumlah in counter_kategori.most_common():
            teks += f"• {nama} : {jumlah}\n"
        teks += "\n"

    teks += "📋 Daftar Berita\n\n"

    for i, item in enumerate(data_list[:20], start=1):
        judul = (
            item.get("title")
            or item.get("judul")
            or item.get("name")
            or "-"
        )

        tanggal = (
            item.get("date")
            or item.get("published_at")
            or item.get("created_at")
            or item.get("tanggal")
            or "-"
        )

        ringkasan = (
            item.get("summary")
            or item.get("excerpt")
            or item.get("description")
            or item.get("content")
            or ""
        )

        link = (
            item.get("url")
            or item.get("link")
            or item.get("slug")
            or ""
        )

        teks += f"{i}. {judul}\n"
        teks += f"   📅 Tanggal : {tanggal}\n"

        if ringkasan:
            ringkasan = str(ringkasan).replace("<p>", "").replace("</p>", "")
            teks += f"   📝 Ringkasan : {ringkasan[:250]}...\n"

        if link:
            teks += f"   🔗 Link : {link}\n"

        teks += "\n"

    teks += "──────────────────────────\n"
    teks += "Sumber : SITABA Kementerian PU"

    return teks
from collections import Counter


def format_publication(data_list, title="Publikasi SITABA"):

    if not data_list:
        return f"Tidak ditemukan data {title.lower()}."

    counter_kategori = Counter()
    counter_tahun = Counter()

    teks = f"📚 {title.upper()}\n\n"

    teks += f"Total dokumen : {len(data_list)}\n\n"

    for item in data_list:

        kategori = (
            item.get("category")
            or item.get("type")
            or item.get("jenis")
            or "Lainnya"
        )

        counter_kategori[kategori] += 1

        tanggal = (
            item.get("publish_date")
            or item.get("date")
            or item.get("created_at")
            or ""
        )

        if len(str(tanggal)) >= 4:
            tahun = str(tanggal)[:4]
            counter_tahun[tahun] += 1


    if counter_kategori:

        teks += "📌 Kategori\n"

        for nama, jumlah in counter_kategori.most_common():

            teks += f"• {nama} : {jumlah}\n"

        teks += "\n"


    if counter_tahun:

        teks += "📅 Tahun Publikasi\n"

        for tahun, jumlah in sorted(counter_tahun.items()):

            teks += f"• {tahun} : {jumlah}\n"

        teks += "\n"


    teks += "📄 Daftar Dokumen\n\n"

    for i, item in enumerate(data_list[:20], start=1):

        judul = (
            item.get("title")
            or item.get("judul")
            or item.get("name")
            or "-"
        )

        kategori = (
            item.get("category")
            or item.get("type")
            or "-"
        )

        tanggal = (
            item.get("publish_date")
            or item.get("date")
            or item.get("created_at")
            or "-"
        )

        deskripsi = (
            item.get("description")
            or item.get("summary")
            or item.get("excerpt")
            or ""
        )

        penulis = (
            item.get("author")
            or item.get("publisher")
            or ""
        )

        file_url = (
            item.get("file")
            or item.get("url")
            or item.get("download")
            or ""
        )

        teks += f"{i}. {judul}\n"

        teks += f"   📌 Kategori : {kategori}\n"

        teks += f"   📅 Tanggal  : {tanggal}\n"

        if penulis:

            teks += f"   👤 Penulis  : {penulis}\n"

        if deskripsi:

            deskripsi = str(deskripsi).replace("\n", " ")

            teks += f"   📝 Deskripsi : {deskripsi[:250]}...\n"

        if file_url:

            teks += f"   📥 File : {file_url}\n"

        teks += "\n"


    teks += "──────────────────────────\n"

    teks += "Sumber : SITABA Kementerian PU"

    return teks
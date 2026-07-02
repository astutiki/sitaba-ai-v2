from collections import Counter


def format_jawaban_bencana(hasil, filter_info):

    if not hasil:

        keterangan = []

        if filter_info.get("provinsi"):
            keterangan.append(filter_info["provinsi"])

        if filter_info.get("kota"):
            keterangan.extend(filter_info["kota"])

        if filter_info.get("kecamatan"):
            keterangan.extend(filter_info["kecamatan"])

        if filter_info.get("bulan_nama"):
            keterangan.append(filter_info["bulan_nama"])

        if filter_info.get("tahun"):
            keterangan.append(filter_info["tahun"])

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

        if item.get("jenis"):
            counter_jenis[item["jenis"]] += 1

        if item.get("provinsi"):
            counter_provinsi[item["provinsi"]] += 1

        if item.get("kota"):
            counter_kota[item["kota"]] += 1

        if item.get("current_status"):
            counter_status[item["current_status"]] += 1

        if item.get("damage"):
            kerusakan.append(item["damage"])

        if item.get("road"):
            jalan.append(item["road"])


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

        teks += f"{i}. {item.get('jenis','-')}\n"

        teks += f"   📅 Tanggal     : {item.get('tanggal','-')}\n"

        teks += f"   📍 Provinsi   : {item.get('provinsi','-')}\n"

        teks += f"   🏙 Kota       : {item.get('kota','-')}\n"

        teks += f"   🏘 Kecamatan  : {item.get('kecamatan','-')}\n"

        teks += f"   📌 Lokasi     : {item.get('lokasi','-')}\n"

        if item.get("road"):

            teks += f"   🛣 Jalan      : {item.get('road')}\n"

        if item.get("damage"):

            teks += f"   🏚 Kerusakan  : {item.get('damage')}\n"

        if item.get("current_status"):

            teks += f"   🚧 Status     : {item.get('current_status')}\n"

        teks += "\n"


    teks += "──────────────────────────\n"

    teks += "Sumber : API SITABA Kementerian PU"

    return teks
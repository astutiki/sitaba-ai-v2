from collections import Counter


def format_statistik_bencana(hasil, filter_info=None):
    filter_info = filter_info or {}

    if not hasil:
        return "Tidak ditemukan data statistik bencana sesuai filter yang diminta."

    counter_jenis = Counter()
    counter_provinsi = Counter()
    counter_kota = Counter()
    counter_bulan = Counter()
    counter_tahun = Counter()

    for item in hasil:
        jenis = item.get("jenis") or "Tidak diketahui"
        provinsi = item.get("provinsi") or "Tidak diketahui"
        kota = item.get("kota") or "Tidak diketahui"
        tanggal = item.get("tanggal") or ""

        counter_jenis[jenis] += 1
        counter_provinsi[provinsi] += 1
        counter_kota[kota] += 1

        if len(tanggal) >= 7:
            tahun = tanggal[:4]
            bulan = tanggal[5:7]
            counter_tahun[tahun] += 1
            counter_bulan[bulan] += 1

    teks = "📊 STATISTIK KEJADIAN BENCANA SITABA\n\n"
    teks += f"Total kejadian : {len(hasil)}\n\n"

    if filter_info:
        teks += "🔎 Filter yang digunakan\n"

        if filter_info.get("jenis"):
            teks += f"• Jenis bencana : {filter_info['jenis']}\n"

        if filter_info.get("provinsi"):
            teks += f"• Provinsi : {filter_info['provinsi']}\n"

        if filter_info.get("kota"):
            teks += f"• Kabupaten/Kota : {', '.join(filter_info['kota'])}\n"

        if filter_info.get("kecamatan"):
            teks += f"• Kecamatan : {', '.join(filter_info['kecamatan'])}\n"

        if filter_info.get("bulan_nama"):
            teks += f"• Bulan : {filter_info['bulan_nama']}\n"

        if filter_info.get("tahun"):
            teks += f"• Tahun : {filter_info['tahun']}\n"

        teks += "\n"

    teks += "📌 Berdasarkan Jenis Bencana\n"
    for nama, jumlah in counter_jenis.most_common():
        teks += f"• {nama} : {jumlah} kejadian\n"
    teks += "\n"

    teks += "🗺 Berdasarkan Provinsi\n"
    for nama, jumlah in counter_provinsi.most_common(10):
        teks += f"• {nama} : {jumlah} kejadian\n"
    teks += "\n"

    teks += "🏙 Berdasarkan Kabupaten/Kota\n"
    for nama, jumlah in counter_kota.most_common(10):
        teks += f"• {nama} : {jumlah} kejadian\n"
    teks += "\n"

    if counter_tahun:
        teks += "📅 Berdasarkan Tahun\n"
        for tahun, jumlah in sorted(counter_tahun.items()):
            teks += f"• {tahun} : {jumlah} kejadian\n"
        teks += "\n"

    if counter_bulan:
        teks += "🗓 Berdasarkan Bulan\n"
        nama_bulan = {
            "01": "Januari",
            "02": "Februari",
            "03": "Maret",
            "04": "April",
            "05": "Mei",
            "06": "Juni",
            "07": "Juli",
            "08": "Agustus",
            "09": "September",
            "10": "Oktober",
            "11": "November",
            "12": "Desember",
        }

        for bulan, jumlah in sorted(counter_bulan.items()):
            teks += f"• {nama_bulan.get(bulan, bulan)} : {jumlah} kejadian\n"
        teks += "\n"

    teks += "──────────────────────────\n"
    teks += "Sumber : API SITABA Kementerian PU"

    return teks
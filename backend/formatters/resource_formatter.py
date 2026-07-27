from collections import Counter


def format_resource(resource_list, resource_name="Sumber Daya"):

    if not resource_list:
        return f"Tidak ditemukan data {resource_name.lower()}."

    counter_provinsi = Counter()
    counter_kota = Counter()
    counter_status = Counter()
    counter_jenis = Counter()

    teks = f"📦 DATA {resource_name.upper()}\n\n"

    teks += f"Total data : {len(resource_list)}\n\n"

    for item in resource_list:

        provinsi = (
            item.get("province")
            or item.get("provinsi")
            or ""
        )

        kota = (
            item.get("city")
            or item.get("kota")
            or ""
        )

        status = (
            item.get("status")
            or ""
        )

        jenis = (
            item.get("category")
            or item.get("jenis")
            or item.get("type")
            or ""
        )

        if provinsi:
            counter_provinsi[provinsi] += 1

        if kota:
            counter_kota[kota] += 1

        if status:
            counter_status[status] += 1

        if jenis:
            counter_jenis[jenis] += 1


    if counter_jenis:

        teks += "📌 Jenis\n"

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

        for nama, jumlah in counter_kota.most_common(15):

            teks += f"• {nama} : {jumlah}\n"

        teks += "\n"


    if counter_status:

        teks += "🚧 Status\n"

        for nama, jumlah in counter_status.most_common():

            teks += f"• {nama} : {jumlah}\n"

        teks += "\n"


    teks += "📋 Detail Data\n\n"

    for i, item in enumerate(resource_list[:20], start=1):

        teks += f"{i}. "

        nama = (
            item.get("name")
            or item.get("nama")
            or "-"
        )

        teks += f"{nama}\n"

        jenis = (
            item.get("category")
            or item.get("jenis")
            or item.get("type")
        )

        if jenis:

            teks += f"   📌 Jenis      : {jenis}\n"

        provinsi = (
            item.get("province")
            or item.get("provinsi")
        )

        if provinsi:

            teks += f"   🗺 Provinsi   : {provinsi}\n"

        kota = (
            item.get("city")
            or item.get("kota")
        )

        if kota:

            teks += f"   🏙 Kota       : {kota}\n"

        lokasi = (
            item.get("location")
            or item.get("lokasi")
        )

        if lokasi:

            teks += f"   📍 Lokasi     : {lokasi}\n"

        jumlah = (
            item.get("quantity")
            or item.get("jumlah")
        )

        if jumlah:

            teks += f"   🔢 Jumlah     : {jumlah}\n"

        kondisi = (
            item.get("condition")
            or item.get("kondisi")
        )

        if kondisi:

            teks += f"   🛠 Kondisi    : {kondisi}\n"

        status = (
            item.get("status")
            or ""
        )

        if status:

            teks += f"   🚧 Status     : {status}\n"

        pic = (
            item.get("pic")
            or item.get("penanggung_jawab")
        )

        if pic:

            teks += f"   👤 PIC        : {pic}\n"

        kontak = (
            item.get("phone")
            or item.get("contact")
            or item.get("telepon")
        )

        if kontak:

            teks += f"   ☎ Kontak     : {kontak}\n"

        teks += "\n"

    teks += "──────────────────────────\n"

    teks += "Sumber : API SITABA Kementerian PU"

    return teks

def format_aset_sitaba(
    hasil_api: dict,
    keyword: str | None = None,
) -> str:
    """
    Formatter khusus untuk endpoint list-assets SITABA.

    Struktur field API:
    - asset_category
    - asset_class
    - asset_model
    - total
    - unker
    - unor
    """

    if not hasil_api.get("success"):
        return "Data aset SITABA sedang tidak dapat diakses."

    data = hasil_api.get("data", [])

    if not data:
        if keyword:
            return (
                "Tidak ditemukan aset SITABA yang sesuai "
                f"dengan pencarian '{keyword}'."
            )

        return "Tidak ditemukan data aset SITABA."

    total_unit = sum(
        int(item.get("total") or 0)
        for item in data
    )

    counter_kategori = Counter()
    counter_kelas = Counter()
    counter_unor = Counter()
    counter_unker = Counter()

    for item in data:
        kategori = item.get("asset_category") or "Tidak diketahui"
        kelas = item.get("asset_class") or "Tidak diketahui"
        unor = item.get("unor") or "Tidak diketahui"
        unker = item.get("unker") or "Tidak diketahui"
        jumlah = int(item.get("total") or 0)

        counter_kategori[kategori] += jumlah
        counter_kelas[kelas] += jumlah
        counter_unor[unor] += jumlah
        counter_unker[unker] += jumlah

    teks = "🚚 DATA ASET SITABA\n\n"
    teks += f"Total kelompok data : {len(data)}\n"
    teks += f"Total unit aset : {total_unit}\n\n"

    if keyword:
        teks += f"🔎 Kata pencarian : {keyword}\n\n"

    if counter_kategori:
        teks += "📌 Berdasarkan Kategori\n"
        for nama, jumlah in counter_kategori.most_common():
            teks += f"• {nama} : {jumlah} unit\n"
        teks += "\n"

    if counter_kelas:
        teks += "🧰 Berdasarkan Kelas Aset\n"
        for nama, jumlah in counter_kelas.most_common(15):
            teks += f"• {nama} : {jumlah} unit\n"
        teks += "\n"

    if counter_unor:
        teks += "🏢 Berdasarkan Unit Organisasi\n"
        for nama, jumlah in counter_unor.most_common(10):
            teks += f"• {nama} : {jumlah} unit\n"
        teks += "\n"

    teks += "📋 Detail Data\n\n"

    batas_tampil = 20

    for nomor, item in enumerate(
        data[:batas_tampil],
        start=1,
    ):
        kategori = item.get("asset_category") or "-"
        kelas = item.get("asset_class") or "-"
        model = item.get("asset_model") or "-"
        jumlah = item.get("total") or 0
        unker = item.get("unker") or "-"
        unor = item.get("unor") or "-"

        teks += f"{nomor}. {kelas}\n"
        teks += f"   📌 Kategori : {kategori}\n"
        teks += f"   🧰 Model : {model}\n"
        teks += f"   🔢 Jumlah : {jumlah}\n"
        teks += f"   🏢 Unit kerja : {unker}\n"
        teks += f"   🏛 Unit organisasi : {unor}\n\n"

    if len(data) > batas_tampil:
        teks += (
            f"Menampilkan {batas_tampil} dari "
            f"{len(data)} kelompok data aset.\n\n"
        )

    teks += "──────────────────────────\n"
    teks += "Sumber : API SITABA Kementerian PU"

    return teks
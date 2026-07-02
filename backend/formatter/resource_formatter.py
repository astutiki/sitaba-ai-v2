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
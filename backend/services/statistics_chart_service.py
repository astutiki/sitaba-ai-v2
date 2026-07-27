from collections import Counter
from typing import Any


def ubah_counter(counter: Counter) -> list[dict]:
    return [
        {
            "label": label,
            "value": jumlah,
        }
        for label, jumlah in counter.most_common()
    ]


def buat_data_chart(data_bencana: list[dict[str, Any]]) -> dict:
    jenis = Counter()
    provinsi = Counter()
    kabupaten_kota = Counter()
    bulan = Counter()
    tahun = Counter()

    for item in data_bencana:
        jenis[item.get("jenis") or "Tidak diketahui"] += 1
        provinsi[item.get("provinsi") or "Tidak diketahui"] += 1
        kabupaten_kota[item.get("kota") or "Tidak diketahui"] += 1
        bulan[str(item.get("bulan") or "Tidak diketahui")] += 1
        tahun[str(item.get("tahun") or "Tidak diketahui")] += 1

    return {
        "jenis_bencana": ubah_counter(jenis),
        "provinsi": ubah_counter(provinsi),
        "kabupaten_kota": ubah_counter(kabupaten_kota),
        "bulan": ubah_counter(bulan),
        "tahun": ubah_counter(tahun),
    }
import json
import time
import requests
from pathlib import Path

BASE_URL = "https://emsifa.github.io/api-wilayah-indonesia/api"
OUTPUT = Path("data/wilayah.json")

ALIAS_TAMBAHAN = {
    "JAWA TIMUR": ["jatim"],
    "JAWA BARAT": ["jabar"],
    "JAWA TENGAH": ["jateng"],
    "DI YOGYAKARTA": ["diy", "jogja", "yogya"],
    "DKI JAKARTA": ["jakarta", "dki"],
    "KABUPATEN TAPANULI TENGAH": ["tapteng"],
    "KABUPATEN TAPANULI UTARA": ["taput"],
    "KABUPATEN TAPANULI SELATAN": ["tapsel"],
}

def get_json(url):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()

def alias(nama):
    nama_upper = nama.upper()
    nama_lower = nama.lower()
    hasil = {nama_lower}

    hasil.update([x.lower() for x in ALIAS_TAMBAHAN.get(nama_upper, [])])

    if nama_lower.startswith("kabupaten "):
        hasil.add(nama_lower.replace("kabupaten ", "").strip())

    if nama_lower.startswith("kota "):
        hasil.add(nama_lower.replace("kota ", "").strip())

    if nama_lower.startswith("kecamatan "):
        hasil.add(nama_lower.replace("kecamatan ", "").strip())

    if nama_lower.startswith("desa "):
        hasil.add(nama_lower.replace("desa ", "").strip())

    if nama_lower.startswith("kelurahan "):
        hasil.add(nama_lower.replace("kelurahan ", "").strip())

    return sorted(hasil)

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    semua = []
    provinsi = get_json(f"{BASE_URL}/provinces.json")

    for prov in provinsi:
        prov_item = {
            "kode": prov["id"],
            "provinsi": prov["name"].upper(),
            "alias": alias(prov["name"]),
            "kabupaten_kota": []
        }

        kabupaten = get_json(f"{BASE_URL}/regencies/{prov['id']}.json")

        for kab in kabupaten:
            kab_item = {
                "kode": kab["id"],
                "nama": kab["name"].upper(),
                "alias": alias(kab["name"]),
                "kecamatan": []
            }

            kecamatan = get_json(f"{BASE_URL}/districts/{kab['id']}.json")

            for kec in kecamatan:
                kec_item = {
                    "kode": kec["id"],
                    "nama": kec["name"].upper(),
                    "alias": alias(kec["name"]),
                    "desa_kelurahan": []
                }

                desa = get_json(f"{BASE_URL}/villages/{kec['id']}.json")

                for d in desa:
                    kec_item["desa_kelurahan"].append({
                        "kode": d["id"],
                        "nama": d["name"].upper(),
                        "alias": alias(d["name"])
                    })

                kab_item["kecamatan"].append(kec_item)
                time.sleep(0.02)

            prov_item["kabupaten_kota"].append(kab_item)
            time.sleep(0.02)

        semua.append(prov_item)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(semua, f, ensure_ascii=False, indent=2)

    print(f"SELESAI: {OUTPUT.resolve()}")

if __name__ == "__main__":
    main()
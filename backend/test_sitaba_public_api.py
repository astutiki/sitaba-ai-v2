from pprint import pprint

from services.sitaba_public_service import (
    ambil_semua_aset,
    ambil_semua_gempa,
)


def test_asset():
    print("\n===== TEST API ASET =====")

    hasil = ambil_semua_aset()

    print("Success:", hasil["success"])
    print("Status code:", hasil["status_code"])
    print("Total:", len(hasil["data"]))
    print("Error:", hasil["error"])

    if hasil["data"]:
        print("Contoh aset:")
        pprint(hasil["data"][0])


def test_gempa():
    print("\n===== TEST API GEMPA =====")

    hasil = ambil_semua_gempa()

    print("Success:", hasil["success"])
    print("Status code:", hasil["status_code"])
    print("Total:", len(hasil["data"]))
    print("Error:", hasil["error"])
    print("Payload asli:")

    pprint(hasil["payload"])

    if hasil["data"]:
        print("Contoh gempa:")
        pprint(hasil["data"][0])


if __name__ == "__main__":
    test_asset()
    test_gempa()
    
"""
Knowledge Base
Kesiapsiagaan Bencana (Preparedness)
AI SINTA
"""


def jawab_kesiapsiagaan(pertanyaan):

    q = pertanyaan.lower()

    # ============================================================
    # TAS SIAGA
    # ============================================================

    if (
        "tas siaga" in q
        or "emergency kit" in q
        or "perlengkapan darurat" in q
    ):

        return """
🎒 Tas Siaga Bencana

Disarankan berisi:

📄 Dokumen penting
• KTP
• KK
• Paspor
• Surat penting

🍞 Logistik
• Air minum
• Makanan siap saji
• Biskuit energi

💊 Kesehatan
• Obat pribadi
• Kotak P3K
• Masker
• Hand sanitizer

🔦 Peralatan
• Senter
• Power bank
• Baterai cadangan
• Peluit
• Radio

👕 Lainnya
• Pakaian ganti
• Selimut
• Jas hujan
• Uang tunai secukupnya
"""

    # ============================================================
    # BANJIR
    # ============================================================

    if "banjir" in q:

        return """
🌊 Kesiapsiagaan Menghadapi Banjir

Sebelum banjir:

✅ Ketahui jalur evakuasi
✅ Simpan dokumen penting
✅ Siapkan tas siaga
✅ Pantau informasi BMKG
✅ Simpan nomor darurat
✅ Pindahkan barang berharga ke tempat tinggi
"""

    # ============================================================
    # LONGSOR
    # ============================================================

    if "longsor" in q:

        return """
⛰ Kesiapsiagaan Menghadapi Longsor

✅ Kenali daerah rawan
✅ Hindari lereng curam
✅ Pantau retakan tanah
✅ Siapkan jalur evakuasi
✅ Simpan nomor darurat
"""

    # ============================================================
    # GEMPA
    # ============================================================

    if "gempa" in q:

        return """
🌍 Kesiapsiagaan Menghadapi Gempa

✅ Ketahui titik kumpul
✅ Kencangkan lemari besar
✅ Simpan barang berat di bawah
✅ Latihan Drop-Cover-Hold On
✅ Siapkan tas siaga
"""

    # ============================================================
    # TSUNAMI
    # ============================================================

    if "tsunami" in q:

        return """
🌊 Kesiapsiagaan Tsunami

✅ Ketahui jalur evakuasi
✅ Kenali sirine tsunami
✅ Ketahui lokasi tempat tinggi
✅ Ikuti simulasi evakuasi
"""

    # ============================================================
    # ERUPSI
    # ============================================================

    if "erupsi" in q or "gunung api" in q:

        return """
🌋 Kesiapsiagaan Erupsi Gunung Api

✅ Masker
✅ Kacamata
✅ Tas siaga
✅ Pantau informasi PVMBG
✅ Ketahui radius bahaya
"""

    # ============================================================
    # CUACA EKSTRIM
    # ============================================================

    if "cuaca" in q:

        return """
🌪 Kesiapsiagaan Cuaca Ekstrem

✅ Pantau BMKG
✅ Amankan benda di luar rumah
✅ Hindari pohon besar
✅ Isi baterai HP
"""

    # ============================================================
    # KELUARGA
    # ============================================================

    if (
        "keluarga" in q
        or "anggota keluarga" in q
    ):

        return """
👨‍👩‍👧 Rencana Kesiapsiagaan Keluarga

• Tentukan titik kumpul keluarga
• Simpan nomor darurat
• Tentukan jalur evakuasi
• Latihan evakuasi bersama
• Siapkan tas siaga untuk setiap anggota keluarga
"""

    # ============================================================
    # UMUM
    # ============================================================

    if (
        "kesiapsiagaan" in q
        or "preparedness" in q
        or "persiapan" in q
        or "sebelum bencana" in q
        or "apa yang harus disiapkan" in q
    ):

        return """
🛡 Kesiapsiagaan Menghadapi Bencana

Sebelum bencana:

📍 Kenali risiko di wilayah Anda.

📱 Pantau informasi resmi BMKG, BNPB, BPBD, dan pemerintah.

🎒 Siapkan tas siaga.

📄 Amankan dokumen penting.

👨‍👩‍👧 Buat rencana evakuasi keluarga.

☎ Simpan nomor darurat.

🧭 Ketahui jalur evakuasi dan titik kumpul.

🩺 Siapkan obat-obatan pribadi.

🔋 Pastikan telepon genggam selalu memiliki daya yang cukup.
"""

    return None
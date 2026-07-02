"""
Knowledge Base
Family Disaster Preparedness Plan
AI SINTA
"""


def jawab_rencana_keluarga(pertanyaan):

    q = pertanyaan.lower()

    if (
        "rencana keluarga" not in q
        and "family plan" not in q
        and "keluarga" not in q
        and "anggota keluarga" not in q
        and "terpisah" not in q
        and "titik kumpul" not in q
    ):
        return None

    # =====================================================
    # RENCANA KELUARGA
    # =====================================================

    if (
        "rencana keluarga" in q
        or "family plan" in q
    ):

        return """
👨‍👩‍👧 Rencana Kesiapsiagaan Keluarga

Setiap keluarga disarankan memiliki rencana menghadapi bencana.

Langkah yang perlu disiapkan:

📍 Tentukan titik kumpul keluarga.

🛣 Ketahui jalur evakuasi.

📱 Simpan nomor darurat seluruh anggota keluarga.

🎒 Siapkan tas siaga untuk setiap anggota keluarga.

🏥 Ketahui lokasi rumah sakit dan posko terdekat.

📄 Simpan dokumen penting di tempat aman.

🔋 Pastikan telepon genggam selalu memiliki daya yang cukup.

📢 Lakukan simulasi evakuasi secara berkala.
"""

    # =====================================================
    # TITIK KUMPUL
    # =====================================================

    if "titik kumpul" in q:

        return """
📍 Titik Kumpul Keluarga

Pilih lokasi yang:

✅ Aman dari potensi bencana.

✅ Mudah dijangkau semua anggota keluarga.

✅ Diketahui seluruh anggota keluarga.

Contoh:

• Lapangan terbuka.
• Balai desa.
• Halaman sekolah.
• Posko evakuasi.
"""

    # =====================================================
    # KOMUNIKASI
    # =====================================================

    if (
        "komunikasi" in q
        or "terpisah" in q
    ):

        return """
📱 Rencana Komunikasi Keluarga

Jika anggota keluarga terpisah:

• Tetap tenang.
• Hubungi nomor yang telah disepakati.
• Datang ke titik kumpul.
• Gunakan SMS jika jaringan telepon sibuk.
• Ikuti informasi dari petugas.
"""

    # =====================================================
    # ANAK
    # =====================================================

    if (
        "anak" in q
    ):

        return """
🧒 Persiapan untuk Anak

• Ajarkan nomor darurat.
• Kenalkan jalur evakuasi.
• Ajarkan mengikuti guru atau orang tua.
• Siapkan makanan dan minuman.
• Siapkan pakaian ganti.
• Siapkan obat bila diperlukan.
"""

    # =====================================================
    # LANSIA
    # =====================================================

    if (
        "lansia" in q
    ):

        return """
👵 Persiapan untuk Lansia

• Siapkan obat rutin.
• Siapkan alat bantu jalan.
• Siapkan daftar riwayat penyakit.
• Dampingi saat evakuasi.
• Pastikan kebutuhan khusus terpenuhi.
"""

    # =====================================================
    # DISABILITAS
    # =====================================================

    if (
        "disabilitas" in q
        or "difabel" in q
    ):

        return """
♿ Persiapan untuk Penyandang Disabilitas

• Kenali kebutuhan khusus.
• Siapkan alat bantu.
• Tentukan pendamping evakuasi.
• Siapkan obat-obatan.
• Informasikan kondisi kepada petugas.
"""

    # =====================================================
    # HEWAN PELIHARAAN
    # =====================================================

    if (
        "hewan" in q
        or "peliharaan" in q
    ):

        return """
🐶 Persiapan Hewan Peliharaan

• Siapkan kandang atau tali.
• Siapkan makanan.
• Siapkan air minum.
• Bawa dokumen kesehatan bila ada.
• Jangan membahayakan diri saat menyelamatkan hewan.
"""

    # =====================================================
    # TAS SIAGA
    # =====================================================

    if (
        "tas siaga" in q
    ):

        return """
🎒 Tas Siaga Keluarga

Minimal berisi:

📄 Dokumen penting

💊 Obat pribadi

🥤 Air minum

🍞 Makanan siap saji

🔦 Senter

🔋 Power bank

📱 Charger

👕 Pakaian ganti

😷 Masker

🩹 Kotak P3K

💵 Uang tunai secukupnya
"""

    # =====================================================
    # SIMULASI
    # =====================================================

    if (
        "simulasi" in q
        or "latihan" in q
    ):

        return """
🚨 Simulasi Keluarga

Disarankan dilakukan minimal 2 kali dalam setahun.

Latihan meliputi:

• Jalur evakuasi.
• Titik kumpul.
• Penggunaan tas siaga.
• Komunikasi keluarga.
• Penanganan anak dan lansia.
"""

    # =====================================================
    # UMUM
    # =====================================================

    return """
👨‍👩‍👧 Family Disaster Preparedness Plan

Setiap keluarga sebaiknya memiliki rencana menghadapi bencana.

Checklist:

✅ Jalur evakuasi

✅ Titik kumpul

✅ Nomor darurat

✅ Tas siaga

✅ Dokumen penting

✅ Simulasi keluarga

✅ Daftar obat pribadi

✅ Rencana komunikasi

Tujuannya adalah agar seluruh anggota keluarga mengetahui apa yang harus dilakukan sebelum, saat, dan setelah bencana sehingga proses evakuasi dapat berlangsung lebih aman dan terkoordinasi.
"""
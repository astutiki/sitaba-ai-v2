"""
Knowledge Base
Mitigasi Bencana
AI SINTA
"""


def jawab_mitigasi(pertanyaan):

    q = pertanyaan.lower()

    # ============================================================
    # BANJIR
    # ============================================================

    if "banjir" in q:

        return """
🌊 Mitigasi Banjir

✅ Sebelum Banjir
• Bersihkan saluran air.
• Jangan membuang sampah ke sungai.
• Siapkan tas siaga bencana.
• Simpan dokumen penting di tempat aman.
• Pantau informasi cuaca dan peringatan dini.

🚨 Saat Banjir
• Matikan listrik bila aman dilakukan.
• Hindari arus banjir.
• Evakuasi ke tempat yang lebih tinggi.
• Ikuti arahan BPBD dan petugas.

🏠 Setelah Banjir
• Pastikan rumah aman sebelum masuk.
• Bersihkan lumpur menggunakan APD.
• Periksa instalasi listrik.
• Gunakan air bersih.
"""

    # ============================================================
    # LONGSOR
    # ============================================================

    if "longsor" in q:

        return """
⛰ Mitigasi Tanah Longsor

✅ Sebelum
• Hindari membangun di lereng curam.
• Tanam pohon berakar kuat.
• Buat drainase lereng.

🚨 Saat Longsor
• Segera menjauh dari lereng.
• Evakuasi ke tempat aman.
• Jangan melintasi lokasi longsor.

🏠 Setelah
• Hindari lokasi sebelum dinyatakan aman.
• Waspadai longsor susulan.
"""

    # ============================================================
    # GEMPA
    # ============================================================

    if "gempa" in q:

        return """
🌍 Mitigasi Gempa Bumi

✅ Sebelum
• Ketahui jalur evakuasi.
• Siapkan tas siaga.
• Pastikan bangunan memenuhi standar.

🚨 Saat Gempa
• Drop, Cover, Hold On.
• Lindungi kepala.
• Jangan gunakan lift.
• Setelah guncangan berhenti segera keluar.

🏠 Setelah
• Periksa kebocoran gas.
• Hindari bangunan retak.
• Ikuti informasi resmi.
"""

    # ============================================================
    # TSUNAMI
    # ============================================================

    if "tsunami" in q:

        return """
🌊 Mitigasi Tsunami

✅ Sebelum
• Ketahui jalur evakuasi.
• Kenali sirine tsunami.
• Ikuti simulasi evakuasi.

🚨 Saat
• Segera menuju tempat tinggi.
• Jangan menunggu air datang.
• Ikuti jalur evakuasi.

🏠 Setelah
• Jangan kembali sebelum dinyatakan aman.
"""

    # ============================================================
    # ERUPSI
    # ============================================================

    if "erupsi" in q or "gunung api" in q:

        return """
🌋 Mitigasi Erupsi Gunung Api

✅ Sebelum
• Pantau informasi PVMBG.
• Siapkan masker dan kacamata.

🚨 Saat
• Gunakan masker.
• Tutup pintu dan jendela.
• Evakuasi jika diperintahkan.

🏠 Setelah
• Bersihkan abu dengan masker.
• Periksa kondisi bangunan.
"""

    # ============================================================
    # KEKERINGAN
    # ============================================================

    if "kekeringan" in q:

        return """
☀ Mitigasi Kekeringan

• Hemat penggunaan air.
• Manfaatkan embung dan waduk.
• Gunakan irigasi hemat air.
• Menampung air hujan.
"""

    # ============================================================
    # CUACA EKSTRIM
    # ============================================================

    if "cuaca" in q:

        return """
🌪 Mitigasi Cuaca Ekstrem

• Hindari berteduh di bawah pohon.
• Amankan benda yang mudah terbang.
• Pantau BMKG.
• Kurangi aktivitas luar ruangan.
"""

    # ============================================================
    # KEBAKARAN
    # ============================================================

    if "kebakaran" in q:

        return """
🔥 Mitigasi Kebakaran

• Periksa instalasi listrik.
• Jangan membakar sampah sembarangan.
• Sediakan APAR.
• Hubungi Damkar bila terjadi kebakaran.
"""

    # ============================================================
    # UMUM
    # ============================================================

    if (
        "mitigasi" in q
        or "apa yang harus dilakukan" in q
        or "bagaimana menghadapi" in q
        or "cara menghadapi" in q
        or "cara mengatasi" in q
    ):

        return """
🛡 Mitigasi Umum Bencana

✅ Sebelum
• Kenali risiko bencana di wilayah Anda.
• Siapkan tas siaga.
• Simpan nomor darurat.
• Ikuti informasi BMKG, BNPB, BPBD, dan pemerintah.

🚨 Saat
• Tetap tenang.
• Ikuti arahan petugas.
• Evakuasi bila diperlukan.
• Prioritaskan keselamatan jiwa.

🏠 Setelah
• Periksa kondisi lingkungan.
• Jangan menyebarkan informasi yang belum terverifikasi.
• Laporkan kerusakan kepada instansi terkait.
"""

    return None
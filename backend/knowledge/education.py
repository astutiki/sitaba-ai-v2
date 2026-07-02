"""
Knowledge Base
Edukasi Kebencanaan
AI SINTA
"""


def jawab_edukasi_bencana(pertanyaan):

    q = pertanyaan.lower()

    if (
        "edukasi" not in q
        and "belajar" not in q
        and "materi bencana" not in q
        and "pengetahuan bencana" not in q
        and "literasi bencana" not in q
        and "anak sekolah" not in q
        and "masyarakat" not in q
    ):
        return None

    if "anak" in q or "sekolah" in q or "siswa" in q:
        return """
🎒 Edukasi Kebencanaan untuk Anak Sekolah

Materi penting:

• Mengenal jenis bencana di sekitar.
• Mengetahui jalur evakuasi sekolah.
• Mengenal titik kumpul.
• Tidak panik saat bencana.
• Mengikuti arahan guru dan petugas.
• Membawa tas siaga sederhana.
• Tidak menyebarkan informasi palsu.

Kegiatan yang disarankan:

• Simulasi evakuasi.
• Latihan Drop, Cover, Hold On.
• Pengenalan tanda bahaya.
• Permainan edukatif tentang bencana.
"""

    if "keluarga" in q:
        return """
👨‍👩‍👧 Edukasi Kebencanaan untuk Keluarga

Hal yang perlu dipahami keluarga:

• Risiko bencana di lingkungan rumah.
• Jalur evakuasi terdekat.
• Titik kumpul keluarga.
• Nomor darurat.
• Cara mematikan listrik dan gas.
• Isi tas siaga.
• Rencana komunikasi saat darurat.
"""

    if "masyarakat" in q or "warga" in q:
        return """
🏘 Edukasi Kebencanaan untuk Masyarakat

Materi yang perlu dipahami:

• Risiko bencana wilayah.
• Mitigasi lingkungan.
• Sistem peringatan dini.
• Evakuasi mandiri.
• Perlindungan kelompok rentan.
• Gotong royong penanganan darurat.
• Pelaporan kejadian bencana kepada petugas.

Kegiatan:

• Sosialisasi bencana.
• Simulasi evakuasi.
• Pembentukan relawan.
• Pembersihan saluran air.
• Penanaman pohon di area rawan longsor.
"""

    if "hoaks" in q or "hoax" in q or "informasi palsu" in q:
        return """
⚠️ Edukasi Anti-Hoaks Saat Bencana

Saat bencana, masyarakat perlu berhati-hati terhadap informasi palsu.

Yang perlu dilakukan:

• Periksa sumber informasi.
• Ikuti kanal resmi pemerintah.
• Jangan langsung menyebarkan foto/video tanpa verifikasi.
• Waspadai pesan berantai yang menimbulkan kepanikan.
• Laporkan informasi palsu kepada pihak berwenang.

Gunakan sumber resmi seperti BMKG, BNPB, BPBD, pemerintah daerah, dan kanal resmi Kementerian PU.
"""

    if "literasi" in q:
        return """
📚 Literasi Kebencanaan

Literasi kebencanaan adalah kemampuan masyarakat untuk memahami risiko bencana, mengetahui cara mengurangi risiko, serta mampu mengambil keputusan yang aman sebelum, saat, dan setelah bencana.

Literasi kebencanaan mencakup:

• Mengenal jenis bencana.
• Memahami tanda bahaya.
• Mengetahui jalur evakuasi.
• Menyiapkan tas siaga.
• Memahami informasi peringatan dini.
• Mengetahui kontak darurat.
"""

    return """
📚 Edukasi Kebencanaan

Edukasi kebencanaan bertujuan meningkatkan pengetahuan dan kesiapsiagaan masyarakat agar mampu menghadapi bencana dengan lebih aman.

Materi edukasi utama:

🌍 Mengenal Risiko
• Jenis bencana.
• Wilayah rawan.
• Tanda bahaya.

🛡 Pengurangan Risiko
• Mitigasi.
• Kesiapsiagaan.
• Perbaikan lingkungan.

🚨 Tanggap Darurat
• Evakuasi.
• Pertolongan pertama.
• Kontak darurat.

🏠 Pemulihan
• Kebersihan lingkungan.
• Pemeriksaan rumah.
• Dukungan sosial.
• Pelaporan kerusakan.

Sumber informasi sebaiknya berasal dari kanal resmi seperti BMKG, BNPB, BPBD, pemerintah daerah, dan Kementerian PU.
"""
"""
Knowledge Base
FAQ AI SINTA - SITABA
"""


def jawab_faq(pertanyaan):
    q = pertanyaan.lower()

    if (
        "faq" in q
        or "pertanyaan umum" in q
        or "contoh pertanyaan" in q
        or "bisa tanya apa" in q
    ):
        return """
❓ FAQ AI SINTA - SITABA

Berikut contoh pertanyaan yang dapat diajukan:

🌊 Data Bencana
• Bencana apa saja yang terjadi hari ini?
• Banjir di Jawa Barat ada berapa kejadian?
• Longsor di Kabupaten Tanah Datar terjadi kapan?
• Bencana tahun 2026 apa saja?

📊 Statistik
• Statistik kejadian bencana bulan Juni 2026 apa?
• Jenis bencana paling banyak apa?
• Provinsi mana yang paling banyak terdampak?

🏗 Infrastruktur
• Ruas jalan apa yang terdampak bencana?
• Infrastruktur apa yang rusak akibat banjir?
• Jembatan apa yang terdampak longsor?

📦 Sumber Daya
• Alat apa saja yang digunakan untuk penanganan bencana?
• Berapa personel yang terlibat?
• Material apa yang dibutuhkan?

🛡 Mitigasi & Kesiapsiagaan
• Bagaimana mitigasi banjir?
• Apa isi tas siaga bencana?
• Apa yang harus dilakukan saat gempa?

🚨 Evakuasi & Darurat
• Bagaimana evakuasi saat banjir?
• Nomor darurat apa yang bisa dihubungi?
• Apa yang harus dilakukan saat terjadi longsor?
"""

    if "cara menggunakan" in q or "cara pakai" in q:
        return """
📌 Cara Menggunakan AI SINTA

1. Ketik pertanyaan terkait informasi kebencanaan.
2. Gunakan kata kunci lokasi jika diperlukan, misalnya provinsi atau kabupaten/kota.
3. Gunakan kata kunci waktu jika diperlukan, misalnya tahun atau bulan.
4. AI SINTA akan mencoba mencari data dari SITABA atau knowledge base kebencanaan.

Contoh:
• Bencana di Jawa Barat tahun 2026
• Banjir di Kabupaten Bogor
• Mitigasi longsor
• Kontak darurat bencana
"""

    if "data tidak ditemukan" in q or "kenapa data tidak muncul" in q:
        return """
Data dapat tidak ditemukan karena:

• Data belum tersedia pada endpoint API SITABA yang sedang digunakan.
• Pertanyaan terlalu spesifik.
• Penulisan lokasi berbeda dengan data di SITABA.
• Data berada pada kategori lain seperti berita, publikasi, atau sumber daya.
• Data belum diperbarui pada API publik.

Silakan coba gunakan pertanyaan yang lebih umum, misalnya:
• Bencana di Jawa Barat
• Statistik bencana tahun 2026
• Banjir bulan Juni 2026
"""

    if "apakah data akurat" in q or "akurasi" in q:
        return """
AI SINTA berupaya menampilkan informasi berdasarkan data SITABA dan knowledge base kebencanaan.

Untuk angka kejadian, lokasi, tanggal, status penanganan, dan data teknis, AI SINTA hanya menampilkan data yang tersedia dari sumber resmi yang terhubung.

Jika data belum tersedia, SINTA tidak akan mengarang informasi.
"""

    return None
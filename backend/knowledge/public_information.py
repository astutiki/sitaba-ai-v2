"""
Knowledge Base
Informasi Umum SITABA dan AI SINTA
"""


def jawab_informasi_publik(pertanyaan):

    q = pertanyaan.lower()

    # =====================================================
    # APA ITU SITABA
    # =====================================================

    if (
        "apa itu sitaba" in q
        or "sitaba itu apa" in q
        or "tentang sitaba" in q
    ):

        return """
ℹ️ Tentang SITABA

SITABA adalah sistem informasi kebencanaan Kementerian Pekerjaan Umum yang digunakan untuk mendukung penyediaan informasi terkait kejadian bencana, penanganan, sumber daya, publikasi, regulasi, dan informasi pendukung kebencanaan.

Melalui SITABA, masyarakat dapat memperoleh informasi kebencanaan yang berkaitan dengan infrastruktur bidang Pekerjaan Umum.
"""

    # =====================================================
    # APA ITU SINTA
    # =====================================================

    if (
        "apa itu sinta" in q
        or "sinta itu apa" in q
        or "ai sinta" in q
        or "chatbot sinta" in q
    ):

        return """
🤖 Tentang AI SINTA

AI SINTA adalah asisten virtual untuk membantu pengguna memperoleh informasi kebencanaan yang berkaitan dengan SITABA Kementerian Pekerjaan Umum.

SINTA dapat membantu menjawab pertanyaan mengenai:
• Bencana terkini
• Statistik kejadian bencana
• Infrastruktur terdampak
• Jalan, jembatan, bendungan, dan fasilitas PU
• Sumber daya seperti personel, alat, dan material
• Publikasi dan regulasi
• Mitigasi, kesiapsiagaan, evakuasi, dan kontak darurat
"""

    # =====================================================
    # INFORMASI YANG BISA DICARI
    # =====================================================

    if (
        "informasi apa saja" in q
        or "apa saja yang bisa dicari" in q
        or "fitur sitaba" in q
        or "menu sitaba" in q
        or "bisa tanya apa" in q
        or "bisa mencari apa" in q
    ):

        return """
📌 Informasi yang dapat dicari melalui SITABA

Masyarakat dapat mencari informasi mengenai:

🌊 Data Bencana
• Bencana terkini
• Jenis bencana
• Lokasi kejadian
• Tanggal kejadian
• Status penanganan

📊 Statistik
• Jumlah kejadian bencana
• Statistik berdasarkan tahun
• Statistik berdasarkan bulan
• Statistik berdasarkan provinsi
• Statistik berdasarkan jenis bencana

🏗 Infrastruktur
• Jalan terdampak
• Jembatan terdampak
• Bendungan terdampak
• Drainase atau fasilitas PU terdampak

📦 Sumber Daya
• Personel
• Alat
• Material/Bahan
• Logistik pendukung

📚 Informasi Pendukung
• Berita kebencanaan
• Publikasi
• Regulasi
• Mitigasi
• Kesiapsiagaan
• Evakuasi
• Kontak darurat
"""

    # =====================================================
    # SUMBER DATA
    # =====================================================

    if (
        "sumber data" in q
        or "data dari mana" in q
        or "sumber informasi" in q
    ):

        return """
📚 Sumber Data

Jawaban AI SINTA dapat berasal dari:
• API SITABA Kementerian Pekerjaan Umum
• Data bencana dan infrastruktur yang tersedia pada SITABA
• Knowledge base kebencanaan yang disiapkan untuk edukasi masyarakat

Untuk data spesifik seperti angka kejadian, lokasi, tanggal, dan status penanganan, SINTA hanya menampilkan informasi yang tersedia pada sumber data SITABA.
"""

    # =====================================================
    # BATASAN AI
    # =====================================================

    if (
        "batasan" in q
        or "tidak bisa apa" in q
        or "kenapa tidak bisa jawab" in q
        or "di luar cakupan" in q
    ):

        return """
⚠️ Batasan AI SINTA

AI SINTA difokuskan untuk informasi kebencanaan yang berkaitan dengan SITABA Kementerian Pekerjaan Umum.

SINTA tidak digunakan untuk menjawab pertanyaan di luar cakupan, seperti:
• Politik
• Hiburan
• Saham/crypto
• Kesehatan pribadi
• Data pribadi
• Informasi yang tidak berkaitan dengan SITABA

Jika data tertentu belum tersedia pada API SITABA, SINTA akan menyampaikan bahwa data belum ditemukan.
"""

    # =====================================================
    # OUT OF SCOPE
    # =====================================================

    kata_out = [
        "presiden",
        "wakil presiden",
        "menteri",
        "gubernur",
        "bupati",
        "wali kota",
        "walikota",
        "pemilu",
        "politik",
        "prabowo",
        "jokowi",
        "gibran",
        "anies",
        "ganjar",
        "film",
        "musik",
        "artis",
        "sepak bola",
        "liga",
        "bitcoin",
        "crypto",
        "saham",
        "resep",
        "makanan",
        "chatgpt",
        "gemini",
        "google",
        "instagram",
        "whatsapp",
    ]

    for kata in kata_out:
        if kata in q:
            return """
Maaf, pertanyaan tersebut berada di luar cakupan AI SINTA.

AI SINTA hanya melayani informasi yang tersedia pada SITABA Kementerian Pekerjaan Umum, seperti informasi bencana, statistik, infrastruktur terdampak, sumber daya, publikasi, regulasi, mitigasi, kesiapsiagaan, evakuasi, dan kontak darurat.
"""

    return None
"""
Out of Scope Router
AI SINTA - SITABA

Digunakan untuk menolak pertanyaan yang berada
di luar ruang lingkup SITABA.
"""


OUT_SCOPE_KEYWORDS = [

    # ==========================
    # Politik
    # ==========================

    "presiden",
    "wakil presiden",
    "menteri",
    "gubernur",
    "bupati",
    "wali kota",
    "walikota",
    "pemilu",
    "politik",
    "partai",
    "dpr",
    "mpr",
    "pilkada",

    "prabowo",
    "jokowi",
    "gibran",
    "ganjar",
    "anies",
    "ridwan kamil",

    # ==========================
    # Hiburan
    # ==========================

    "film",
    "drama",
    "anime",
    "musik",
    "lagu",
    "artis",
    "aktor",
    "aktris",
    "idol",

    # ==========================
    # Olahraga
    # ==========================

    "bola",
    "sepak bola",
    "liga",
    "liga inggris",
    "liga spanyol",
    "liga champions",

    "messi",
    "ronaldo",

    # ==========================
    # Teknologi umum
    # ==========================

    "chatgpt",
    "gemini",
    "claude",
    "deepseek",

    "google",
    "facebook",
    "instagram",
    "tiktok",
    "twitter",
    "youtube",

    # ==========================
    # Finansial
    # ==========================

    "bitcoin",
    "crypto",
    "cryptocurrency",
    "ethereum",
    "dogecoin",

    "saham",
    "ihsg",
    "emas",

    # ==========================
    # Kuliner
    # ==========================

    "resep",
    "makanan",
    "masakan",
    "minuman",

    # ==========================
    # Kesehatan pribadi
    # ==========================

    "diagnosa",
    "diagnosis",
    "obat",
    "penyakit",
    "dokter",

]


def cek_out_of_scope(pertanyaan: str):

    q = pertanyaan.lower()

    for kata in OUT_SCOPE_KEYWORDS:

        if kata in q:

            return f"""
Maaf, pertanyaan tersebut berada di luar cakupan AI SINTA.

AI SINTA dirancang khusus untuk memberikan informasi yang berkaitan dengan SITABA Kementerian Pekerjaan Umum, seperti:

• Data bencana
• Statistik kebencanaan
• Infrastruktur terdampak
• Ruas jalan
• Jembatan
• Bendungan
• Personel
• Alat
• Material
• Berita
• Publikasi
• Regulasi
• Mitigasi
• Evakuasi
• Kesiapsiagaan
• Kontak darurat

Silakan ajukan pertanyaan yang berkaitan dengan informasi kebencanaan pada SITABA.
"""

    return None
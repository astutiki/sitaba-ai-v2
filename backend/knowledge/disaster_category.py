"""
Knowledge Base
Kategori dan Jenis Bencana
AI SINTA
"""


def jawab_kategori_bencana(pertanyaan):

    q = pertanyaan.lower()

    # ============================================================
    # APA SAJA JENIS BENCANA
    # ============================================================

    if (
        "jenis bencana" in q
        or "kategori bencana" in q
        or "macam bencana" in q
        or "apa saja bencana" in q
    ):

        return """
🌍 Jenis Bencana di Indonesia

Menurut Undang-Undang Nomor 24 Tahun 2007, bencana dibagi menjadi:

🌋 1. Bencana Alam
• Gempa bumi
• Tsunami
• Gunung api
• Banjir
• Banjir bandang
• Tanah longsor
• Kekeringan
• Cuaca ekstrem
• Gelombang pasang
• Abrasi
• Kebakaran hutan dan lahan

🏭 2. Bencana Non Alam
• Wabah penyakit
• Epidemi
• Pandemi
• Gagal teknologi
• Gagal modernisasi

👥 3. Bencana Sosial
• Konflik sosial
• Kerusuhan
• Teror
"""

    # ============================================================
    # HIDROMETEOROLOGI
    # ============================================================

    if (
        "hidrometeorologi" in q
        or "hidrometeorologi apa" in q
    ):

        return """
🌧 Bencana Hidrometeorologi

Bencana yang dipengaruhi kondisi cuaca, iklim, dan air.

Contohnya:

• Banjir
• Banjir Bandang
• Tanah Longsor
• Kekeringan
• Cuaca Ekstrem
• Puting Beliung
• Gelombang Pasang
• Abrasi
"""

    # ============================================================
    # GEOLOGI
    # ============================================================

    if (
        "geologi" in q
        or "bencana geologi" in q
    ):

        return """
🌋 Bencana Geologi

Bencana yang berasal dari aktivitas bumi.

Contohnya:

• Gempa bumi
• Tsunami
• Erupsi gunung api
• Tanah longsor
"""

    # ============================================================
    # NON ALAM
    # ============================================================

    if "non alam" in q:

        return """
🏭 Bencana Non Alam

Contohnya:

• Wabah penyakit
• Pandemi
• Epidemi
• Gagal teknologi
• Gagal modernisasi
"""

    # ============================================================
    # SOSIAL
    # ============================================================

    if "bencana sosial" in q:

        return """
👥 Bencana Sosial

Contohnya:

• Konflik sosial
• Kerusuhan
• Teror
"""

    # ============================================================
    # BANJIR
    # ============================================================

    if "banjir" in q:

        return """
🌊 Banjir

Kategori:
Bencana Hidrometeorologi

Penyebab:
• Curah hujan tinggi
• Sungai meluap
• Drainase buruk
• Sampah
• Rob

Dampak:
• Rumah terendam
• Jalan rusak
• Jembatan rusak
• Pengungsian
"""

    # ============================================================
    # LONGSOR
    # ============================================================

    if "longsor" in q:

        return """
⛰ Tanah Longsor

Kategori:
Bencana Hidrometeorologi / Geologi

Penyebab:
• Hujan
• Lereng curam
• Gempa
• Penebangan hutan

Dampak:
• Jalan tertutup
• Rumah tertimbun
• Korban jiwa
"""

    # ============================================================
    # GEMPA
    # ============================================================

    if "gempa" in q:

        return """
🌍 Gempa Bumi

Kategori:
Bencana Geologi

Penyebab:
• Pergeseran lempeng
• Sesar aktif
• Vulkanik

Dampak:
• Bangunan roboh
• Korban jiwa
• Tsunami
"""

    # ============================================================
    # TSUNAMI
    # ============================================================

    if "tsunami" in q:

        return """
🌊 Tsunami

Kategori:
Bencana Geologi

Penyebab:
• Gempa bawah laut
• Longsor bawah laut
• Gunung api

Dampak:
• Gelombang tinggi
• Kerusakan pesisir
• Korban jiwa
"""

    # ============================================================
    # ERUPSI
    # ============================================================

    if (
        "erupsi" in q
        or "gunung api" in q
    ):

        return """
🌋 Erupsi Gunung Api

Kategori:
Bencana Geologi

Bahaya:

• Abu vulkanik
• Lava
• Lahar
• Awan panas
• Gas vulkanik
"""

    # ============================================================
    # KEKERINGAN
    # ============================================================

    if "kekeringan" in q:

        return """
☀ Kekeringan

Kategori:
Bencana Hidrometeorologi

Penyebab:
• Kemarau panjang
• El Nino
• Curah hujan rendah

Dampak:
• Kekurangan air
• Gagal panen
"""

    # ============================================================
    # CUACA EKSTRIM
    # ============================================================

    if (
        "cuaca ekstrem" in q
        or "cuaca ekstrim" in q
    ):

        return """
🌪 Cuaca Ekstrem

Kategori:
Bencana Hidrometeorologi

Contoh:
• Angin kencang
• Puting beliung
• Hujan lebat
• Hujan es
"""

    # ============================================================
    # ABRASI
    # ============================================================

    if "abrasi" in q:

        return """
🌊 Abrasi

Kategori:
Bencana Hidrometeorologi

Penyebab:
• Gelombang laut
• Arus laut
• Hilangnya mangrove

Dampak:
• Pantai terkikis
• Permukiman rusak
"""

    return None
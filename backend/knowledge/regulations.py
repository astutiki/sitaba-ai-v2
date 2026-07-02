"""
Knowledge Base
Regulasi Kebencanaan Indonesia
AI SINTA
"""


def jawab_regulasi(pertanyaan):

    q = pertanyaan.lower()

    # ==========================================================
    # UNDANG-UNDANG 24/2007
    # ==========================================================

    if (
        "uu 24" in q
        or "undang-undang 24" in q
        or "uu penanggulangan bencana" in q
        or "dasar hukum bencana" in q
    ):

        return """
📖 Undang-Undang Nomor 24 Tahun 2007

Tentang:
Penanggulangan Bencana

Mengatur:

• Hak masyarakat
• Kewajiban pemerintah
• Tahapan penanggulangan bencana
• Mitigasi
• Kesiapsiagaan
• Tanggap darurat
• Rehabilitasi
• Rekonstruksi

UU ini merupakan dasar hukum utama penanggulangan bencana di Indonesia.
"""

    # ==========================================================
    # PP 21
    # ==========================================================

    if (
        "pp 21" in q
        or "peraturan pemerintah 21" in q
    ):

        return """
📘 PP Nomor 21 Tahun 2008

Tentang:

Penyelenggaraan Penanggulangan Bencana.

Mengatur pelaksanaan teknis dari UU Nomor 24 Tahun 2007.
"""

    # ==========================================================
    # PP 22
    # ==========================================================

    if (
        "pp 22" in q
    ):

        return """
📘 PP Nomor 22 Tahun 2008

Tentang:

Pendanaan dan Pengelolaan Bantuan Bencana.
"""

    # ==========================================================
    # PP 23
    # ==========================================================

    if (
        "pp 23" in q
    ):

        return """
📘 PP Nomor 23 Tahun 2008

Tentang:

Peran serta lembaga internasional dan lembaga asing non pemerintah
dalam penanggulangan bencana.
"""

    # ==========================================================
    # BNPB
    # ==========================================================

    if (
        "bnpb" in q
    ):

        return """
🏢 BNPB

Badan Nasional Penanggulangan Bencana.

Dibentuk berdasarkan:

UU Nomor 24 Tahun 2007.

Tugas:

• Koordinasi nasional
• Komando penanggulangan
• Kebijakan nasional
• Dukungan pemerintah daerah
"""

    # ==========================================================
    # BPBD
    # ==========================================================

    if (
        "bpbd" in q
    ):

        return """
🏢 BPBD

Badan Penanggulangan Bencana Daerah.

Tugas:

• Penanggulangan bencana daerah.
• Koordinasi lintas OPD.
• Tanggap darurat.
• Mitigasi.
• Kesiapsiagaan.
"""

    # ==========================================================
    # KEMENTERIAN PU
    # ==========================================================

    if (
        "kementerian pu" in q
        or "kementerian pekerjaan umum" in q
    ):

        return """
🏗 Kementerian Pekerjaan Umum

Berperan dalam:

• Penanganan infrastruktur terdampak.
• Jalan Nasional.
• Jembatan.
• Bendungan.
• Irigasi.
• Pengendalian banjir.
• Air minum.
• Sanitasi.

Informasi kebencanaan infrastruktur dapat diakses melalui SITABA.
"""

    # ==========================================================
    # SITABA
    # ==========================================================

    if (
        "sitaba" in q
    ):

        return """
💻 SITABA

SITABA merupakan Sistem Informasi Kebencanaan Kementerian Pekerjaan Umum.

Digunakan untuk:

• Monitoring kejadian bencana.
• Infrastruktur terdampak.
• Personel.
• Material.
• Alat.
• Publikasi.
• Regulasi.
"""

    # ==========================================================
    # MITIGASI
    # ==========================================================

    if (
        "mitigasi" in q
    ):

        return """
🛡 Mitigasi

Mitigasi merupakan bagian dari penyelenggaraan penanggulangan bencana
sebagaimana diatur dalam UU Nomor 24 Tahun 2007.

Tujuannya:

Mengurangi risiko bencana melalui pembangunan fisik,
peningkatan kapasitas masyarakat,
dan pengurangan kerentanan.
"""

    # ==========================================================
    # TANGGAP DARURAT
    # ==========================================================

    if (
        "tanggap darurat" in q
    ):

        return """
🚨 Tanggap Darurat

Tahapan penanggulangan bencana setelah bencana terjadi.

Meliputi:

• Evakuasi
• Penyelamatan
• Pelayanan kesehatan
• Logistik
• Hunian sementara
"""

    # ==========================================================
    # REHABILITASI
    # ==========================================================

    if (
        "rehabilitasi" in q
    ):

        return """
🏗 Rehabilitasi

Pemulihan pelayanan publik
dan kehidupan masyarakat
pasca bencana.
"""

    # ==========================================================
    # REKONSTRUKSI
    # ==========================================================

    if (
        "rekonstruksi" in q
    ):

        return """
🏢 Rekonstruksi

Pembangunan kembali infrastruktur,
permukiman,
dan fasilitas umum
agar lebih baik dan tangguh terhadap bencana.
"""

    # ==========================================================
    # UMUM
    # ==========================================================

    if (
        "regulasi" in q
        or "peraturan" in q
        or "dasar hukum" in q
    ):

        return """
📚 Regulasi Kebencanaan Indonesia

Regulasi utama yang berkaitan dengan kebencanaan antara lain:

📖 UU Nomor 24 Tahun 2007
Tentang Penanggulangan Bencana.

📘 PP Nomor 21 Tahun 2008
Penyelenggaraan Penanggulangan Bencana.

📘 PP Nomor 22 Tahun 2008
Pendanaan dan Pengelolaan Bantuan Bencana.

📘 PP Nomor 23 Tahun 2008
Peran Lembaga Internasional.

Selain itu terdapat berbagai peraturan pemerintah, peraturan menteri, dan pedoman teknis yang mengatur penyelenggaraan penanggulangan bencana sesuai kewenangan masing-masing instansi.
"""

    return None
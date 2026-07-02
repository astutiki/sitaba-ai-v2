"""
Knowledge Base
Infrastruktur Pekerjaan Umum
AI SINTA
"""


def jawab_infrastruktur(pertanyaan):

    q = pertanyaan.lower()

    # =====================================================
    # JALAN
    # =====================================================

    if (
        "jalan nasional" in q
        or "apa itu jalan nasional" in q
    ):

        return """
🛣 Jalan Nasional

Jalan nasional merupakan jalan yang menghubungkan antar ibu kota provinsi, kawasan strategis nasional, pelabuhan utama, bandar udara, dan pusat kegiatan nasional.

Pengelolaan dilakukan oleh Pemerintah Pusat melalui Kementerian Pekerjaan Umum.
"""

    if (
        "jalan provinsi" in q
    ):

        return """
🛣 Jalan Provinsi

Jalan provinsi merupakan jalan yang menghubungkan antar ibu kota kabupaten/kota di dalam satu provinsi.

Pengelola:
Pemerintah Provinsi.
"""

    if (
        "jalan kabupaten" in q
        or "jalan kota" in q
    ):

        return """
🛣 Jalan Kabupaten/Kota

Jalan yang menghubungkan wilayah dalam kabupaten atau kota.

Pengelola:
Pemerintah Kabupaten/Kota.
"""

    if (
        "jalan tol" in q
    ):

        return """
🚗 Jalan Tol

Jalan tol adalah jalan umum yang merupakan bagian dari sistem jaringan jalan nasional dan penggunaannya dikenakan tarif.

Tujuan:
• Mempercepat mobilitas.
• Mengurangi kemacetan.
• Mendukung pertumbuhan ekonomi.
"""

    # =====================================================
    # JEMBATAN
    # =====================================================

    if (
        "jembatan" in q
    ):

        return """
🌉 Jembatan

Jembatan adalah bangunan yang digunakan untuk menghubungkan dua lokasi yang terpisah oleh sungai, jurang, rel kereta api, atau hambatan lainnya.

Saat terjadi bencana, jembatan menjadi salah satu infrastruktur prioritas untuk dipulihkan.
"""

    # =====================================================
    # BENDUNGAN
    # =====================================================

    if (
        "bendungan" in q
    ):

        return """
🏞 Bendungan

Bendungan adalah bangunan yang dibangun melintang sungai untuk menampung air.

Fungsi:

• Irigasi
• Penyediaan air baku
• Pengendalian banjir
• Pembangkit listrik
• Pariwisata
"""

    # =====================================================
    # EMBUNG
    # =====================================================

    if (
        "embung" in q
    ):

        return """
💧 Embung

Embung merupakan tampungan air berukuran relatif kecil yang digunakan untuk menyimpan air hujan.

Fungsi:

• Cadangan air
• Irigasi
• Mengurangi kekeringan
"""

    # =====================================================
    # IRIGASI
    # =====================================================

    if (
        "irigasi" in q
    ):

        return """
🌾 Irigasi

Sistem penyediaan dan pengaturan air untuk pertanian.

Fungsi:

• Menjamin kebutuhan air tanaman.
• Mendukung ketahanan pangan.
"""

    # =====================================================
    # DRAINASE
    # =====================================================

    if (
        "drainase" in q
    ):

        return """
🌧 Drainase

Drainase adalah sistem saluran yang berfungsi mengalirkan kelebihan air agar tidak terjadi genangan.

Drainase yang tidak berfungsi dapat meningkatkan risiko banjir.
"""

    # =====================================================
    # TANGGUL
    # =====================================================

    if (
        "tanggul" in q
    ):

        return """
🧱 Tanggul

Tanggul adalah bangunan pelindung untuk mencegah luapan sungai maupun gelombang laut.

Tanggul membantu mengurangi risiko banjir.
"""

    # =====================================================
    # BRONJONG
    # =====================================================

    if (
        "bronjong" in q
    ):

        return """
🪨 Bronjong

Bronjong adalah susunan kawat baja yang diisi batu.

Digunakan untuk:

• Menahan longsor.
• Melindungi tebing sungai.
• Mengurangi erosi.
"""

    # =====================================================
    # SABO DAM
    # =====================================================

    if (
        "sabo" in q
        or "sabo dam" in q
    ):

        return """
🏔 Sabo Dam

Bangunan pengendali sedimen di daerah gunung api.

Fungsi:

• Menahan material vulkanik.
• Mengurangi bahaya lahar.
"""

    # =====================================================
    # SPAM
    # =====================================================

    if (
        "spam" in q
        or "air minum" in q
    ):

        return """
🚰 SPAM

SPAM adalah Sistem Penyediaan Air Minum.

Tujuan:

• Menyediakan air minum yang layak.
• Menjamin pelayanan air bersih kepada masyarakat.
"""

    # =====================================================
    # SANITASI
    # =====================================================

    if (
        "sanitasi" in q
    ):

        return """
🚽 Sanitasi

Sanitasi adalah upaya menjaga kesehatan lingkungan melalui pengelolaan air limbah, sampah, dan fasilitas sanitasi yang layak.

Sanitasi yang baik membantu mencegah penyakit pasca bencana.
"""

    # =====================================================
    # RUMAH SUSUN
    # =====================================================

    if (
        "rumah susun" in q
        or "rusun" in q
    ):

        return """
🏢 Rumah Susun

Bangunan bertingkat yang digunakan sebagai tempat tinggal bersama.

Rumah susun dapat dimanfaatkan sebagai hunian tetap maupun hunian sementara pada kondisi tertentu sesuai kebijakan pemerintah.
"""

    # =====================================================
    # INFRASTRUKTUR
    # =====================================================

    if (
        "infrastruktur" in q
        or "fasilitas pu" in q
    ):

        return """
🏗 Infrastruktur Pekerjaan Umum

Contoh infrastruktur yang dikelola/dibina di bidang Pekerjaan Umum antara lain:

• Jalan Nasional
• Jalan Tol
• Jembatan
• Bendungan
• Embung
• Irigasi
• Drainase
• Tanggul
• Bronjong
• Sabo Dam
• SPAM
• Sanitasi

Infrastruktur tersebut berperan penting dalam mendukung konektivitas, ketahanan air, pengendalian banjir, serta pelayanan dasar kepada masyarakat.
"""

    return None
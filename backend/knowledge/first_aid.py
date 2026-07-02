"""
Knowledge Base
Pertolongan Pertama (First Aid)
AI SINTA

Catatan:
Informasi ini hanya bersifat edukasi dan bukan pengganti
penanganan tenaga kesehatan profesional.
"""


def jawab_pertolongan_pertama(pertanyaan):

    q = pertanyaan.lower()

    # =====================================================
    # LUKA
    # =====================================================

    if "luka" in q:

        return """
🩹 Pertolongan Pertama pada Luka

• Cuci tangan sebelum menolong bila memungkinkan.
• Hentikan perdarahan dengan menekan luka menggunakan kain atau kasa bersih.
• Bersihkan luka menggunakan air mengalir bersih.
• Tutup luka dengan perban steril.
• Jangan mengoleskan bahan yang tidak steril.

Segera ke fasilitas kesehatan apabila:
• Perdarahan tidak berhenti.
• Luka sangat dalam.
• Luka akibat benda berkarat.
• Luka menunjukkan tanda infeksi.
"""

    # =====================================================
    # PATAH TULANG
    # =====================================================

    if (
        "patah" in q
        or "fraktur" in q
    ):

        return """
🦴 Dugaan Patah Tulang

• Jangan menggerakkan bagian yang cedera.
• Imobilisasi menggunakan bidai bila tersedia.
• Kompres dingin untuk mengurangi bengkak.
• Segera menuju fasilitas kesehatan.

Jangan mencoba meluruskan tulang sendiri.
"""

    # =====================================================
    # PENDARAHAN
    # =====================================================

    if (
        "perdarahan" in q
        or "berdarah" in q
    ):

        return """
🩸 Pertolongan Pertama pada Perdarahan

• Tekan luka dengan kasa atau kain bersih.
• Tinggikan bagian tubuh yang terluka bila memungkinkan.
• Jangan membuka kasa yang sudah basah darah, tambahkan lapisan baru di atasnya.
• Segera cari bantuan medis bila perdarahan tidak berhenti.
"""

    # =====================================================
    # PINGSAN
    # =====================================================

    if "pingsan" in q:

        return """
😵 Pertolongan Pertama pada Orang Pingsan

• Pastikan lokasi aman.
• Baringkan korban.
• Longgarkan pakaian yang ketat.
• Angkat kedua kaki sedikit bila tidak ada dugaan cedera.
• Periksa pernapasan.

Hubungi layanan darurat bila korban:
• Tidak sadar lama.
• Tidak bernapas normal.
• Mengalami kejang.
"""

    # =====================================================
    # TERSETRUM
    # =====================================================

    if (
        "tersetrum" in q
        or "kesetrum" in q
    ):

        return """
⚡ Pertolongan Pertama pada Sengatan Listrik

• Jangan menyentuh korban sebelum sumber listrik diputus.
• Matikan aliran listrik bila aman.
• Hubungi layanan darurat bila korban tidak sadar.
• Periksa pernapasan.
• Segera bawa ke fasilitas kesehatan.
"""

    # =====================================================
    # LUKA BAKAR
    # =====================================================

    if (
        "luka bakar" in q
        or "terbakar" in q
    ):

        return """
🔥 Pertolongan Pertama Luka Bakar

• Dinginkan area luka dengan air mengalir selama sekitar 20 menit.
• Lepaskan aksesori yang ketat bila memungkinkan.
• Tutup luka menggunakan kain atau kasa steril yang tidak lengket.
• Jangan mengoleskan pasta gigi, mentega, minyak, atau bahan lain pada luka bakar.

Segera ke fasilitas kesehatan bila luka bakar luas atau mengenai wajah, tangan, kaki, alat kelamin, atau saluran napas.
"""

    # =====================================================
    # TENGGELAM
    # =====================================================

    if (
        "tenggelam" in q
        or "hanyut" in q
    ):

        return """
🌊 Pertolongan Pertama Korban Tenggelam

• Pastikan keselamatan penolong terlebih dahulu.
• Evakuasi korban ke tempat aman bila memungkinkan.
• Periksa kesadaran dan pernapasan.
• Hubungi layanan darurat.
• Jika korban tidak bernapas dan Anda terlatih, lakukan resusitasi jantung paru (RJP/CPR) sampai bantuan datang.
"""

    # =====================================================
    # HIPOTERMIA
    # =====================================================

    if "hipotermia" in q:

        return """
🥶 Pertolongan Pertama Hipotermia

• Pindahkan korban ke tempat hangat.
• Lepaskan pakaian basah.
• Selimuti korban.
• Berikan minuman hangat bila korban sadar.

Segera ke fasilitas kesehatan apabila kondisi memburuk.
"""

    # =====================================================
    # HEAT STROKE
    # =====================================================

    if (
        "heat stroke" in q
        or "serangan panas" in q
    ):

        return """
☀ Pertolongan Pertama Heat Stroke

• Pindahkan korban ke tempat teduh.
• Longgarkan pakaian.
• Dinginkan tubuh menggunakan kompres atau kipas.
• Berikan air minum bila korban sadar.

Segera hubungi layanan darurat apabila korban tidak sadar atau mengalami kebingungan berat.
"""

    # =====================================================
    # UMUM
    # =====================================================

    if (
        "p3k" in q
        or "pertolongan pertama" in q
        or "first aid" in q
    ):

        return """
⛑ Prinsip Dasar Pertolongan Pertama

1. Pastikan lokasi aman.
2. Lindungi diri sebelum menolong.
3. Periksa kesadaran korban.
4. Periksa pernapasan.
5. Hubungi layanan darurat bila diperlukan.
6. Berikan pertolongan pertama sesuai kemampuan.
7. Jangan memindahkan korban bila dicurigai mengalami cedera tulang belakang kecuali ada bahaya yang mengancam.

Informasi ini bersifat edukasi dan tidak menggantikan penanganan tenaga kesehatan profesional.
"""

    return None
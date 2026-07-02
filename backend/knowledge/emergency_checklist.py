"""
Knowledge Base
Checklist Darurat Bencana
AI SINTA
"""


def jawab_checklist_darurat(pertanyaan):

    q = pertanyaan.lower()

    if (
        "checklist" not in q
        and "ceklist" not in q
        and "daftar periksa" not in q
        and "yang harus dibawa" not in q
        and "barang darurat" not in q
        and "perlengkapan darurat" not in q
    ):
        return None

    if "banjir" in q:
        return """
✅ Checklist Darurat Banjir

Sebelum evakuasi:
• Matikan listrik jika aman.
• Amankan dokumen penting.
• Pindahkan barang berharga ke tempat tinggi.
• Siapkan tas siaga.
• Bawa obat pribadi.
• Gunakan alas kaki yang aman.
• Hindari arus banjir.

Barang yang dibawa:
• Air minum.
• Makanan siap saji.
• Senter.
• Power bank.
• Pakaian ganti.
• Dokumen penting.
• Obat-obatan.
• Peluit.
"""

    if "gempa" in q:
        return """
✅ Checklist Darurat Gempa

Saat gempa:
• Drop, Cover, Hold On.
• Lindungi kepala.
• Jauhi kaca dan benda berat.
• Jangan gunakan lift.

Setelah gempa:
• Keluar menuju titik kumpul.
• Periksa luka.
• Waspadai gempa susulan.
• Jangan masuk bangunan retak.
• Pantau informasi resmi.
"""

    if "longsor" in q:
        return """
✅ Checklist Darurat Longsor

Tanda bahaya:
• Retakan tanah.
• Suara gemuruh.
• Pohon/tiang miring.
• Air keruh dari lereng.
• Hujan deras lama.

Tindakan:
• Segera menjauh dari lereng.
• Jangan melintasi lokasi longsor.
• Evakuasi ke tempat aman.
• Ikuti arahan petugas.
"""

    if "tsunami" in q:
        return """
✅ Checklist Darurat Tsunami

Segera evakuasi jika:
• Terjadi gempa kuat di pesisir.
• Air laut tiba-tiba surut.
• Ada peringatan tsunami.

Tindakan:
• Menuju tempat tinggi.
• Ikuti jalur evakuasi.
• Jangan kembali ke pantai.
• Bantu kelompok rentan.
"""

    return """
✅ Checklist Darurat Bencana

Dokumen:
• KTP.
• KK.
• Kartu kesehatan.
• Surat penting.

Perlengkapan:
• Tas siaga.
• Senter.
• Power bank.
• Peluit.
• Radio kecil.
• Masker.
• Jas hujan.

Logistik:
• Air minum.
• Makanan siap saji.
• Obat pribadi.
• P3K.

Tindakan:
• Simpan nomor darurat.
• Ketahui jalur evakuasi.
• Tentukan titik kumpul keluarga.
• Ikuti informasi resmi.
"""
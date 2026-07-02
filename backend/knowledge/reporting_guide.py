"""
Knowledge Base
Panduan Pelaporan Kejadian Bencana
AI SINTA
"""


def jawab_panduan_pelaporan(pertanyaan):

    q = pertanyaan.lower()

    if (
        "lapor" not in q
        and "melaporkan" not in q
        and "pelaporan" not in q
        and "cara melapor" not in q
        and "laporan bencana" not in q
    ):
        return None

    if "data apa" in q or "informasi apa" in q or "yang dilaporkan" in q:
        return """
📝 Informasi yang Perlu Dilaporkan Saat Bencana

Saat melaporkan kejadian bencana, sampaikan:

• Jenis bencana
• Lokasi kejadian
• Waktu kejadian
• Kondisi korban
• Kerusakan infrastruktur
• Akses jalan
• Kebutuhan mendesak
• Foto/video bila aman
• Nama dan kontak pelapor

Laporkan hanya informasi yang benar dan dapat dipertanggungjawabkan.
"""

    if "foto" in q or "video" in q or "dokumentasi" in q:
        return """
📷 Dokumentasi Laporan Bencana

Foto/video dapat membantu petugas memahami kondisi lapangan.

Namun keselamatan tetap utama:

• Jangan mengambil gambar di lokasi berbahaya.
• Jangan menghalangi petugas.
• Jangan menyebarkan foto korban secara tidak etis.
• Sertakan lokasi dan waktu kejadian bila tersedia.
"""

    if "sitaba" in q:
        return """
💻 Pelaporan Melalui SITABA

Jika fitur pelaporan tersedia pada SITABA, gunakan data yang jelas dan lengkap:

• Jenis bencana
• Provinsi
• Kabupaten/Kota
• Kecamatan
• Lokasi detail
• Tanggal kejadian
• Infrastruktur terdampak
• Kerusakan
• Penanganan
• Kebutuhan
• Kontak PIC/pelapor

Jika fitur pelaporan belum tersedia untuk masyarakat umum, ikuti kanal resmi Kementerian PU, BPBD, BNPB, atau pemerintah daerah.
"""

    if "bpbd" in q or "pemerintah daerah" in q:
        return """
🏢 Melapor ke BPBD / Pemerintah Daerah

Untuk kejadian bencana di wilayah Anda, segera laporkan kepada:

• BPBD kabupaten/kota
• Pemerintah desa/kelurahan
• Kecamatan
• Petugas keamanan setempat
• Posko bencana terdekat

Sampaikan lokasi dan kondisi dengan jelas agar petugas dapat melakukan verifikasi dan penanganan.
"""

    return """
🚨 Panduan Melaporkan Kejadian Bencana

Jika melihat atau mengalami kejadian bencana:

1. Pastikan keselamatan diri terlebih dahulu.
2. Jangan masuk ke area berbahaya.
3. Catat lokasi kejadian.
4. Catat waktu kejadian.
5. Jelaskan jenis bencana.
6. Jelaskan kondisi korban bila ada.
7. Jelaskan kerusakan infrastruktur.
8. Sampaikan kebutuhan mendesak.
9. Hubungi BPBD, pemerintah daerah, petugas setempat, atau layanan darurat.
10. Gunakan kanal resmi dan hindari menyebarkan informasi yang belum terverifikasi.

Untuk kondisi darurat yang mengancam jiwa, hubungi 112 atau petugas terdekat.
"""
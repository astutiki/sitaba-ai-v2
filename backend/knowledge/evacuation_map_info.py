"""
Knowledge Base
Informasi Peta dan Jalur Evakuasi
AI SINTA
"""


def jawab_peta_evakuasi(pertanyaan):

    q = pertanyaan.lower()

    if (
        "peta evakuasi" not in q
        and "jalur evakuasi" not in q
        and "rute evakuasi" not in q
        and "titik kumpul" not in q
        and "tempat evakuasi" not in q
        and "lokasi evakuasi" not in q
    ):
        return None

    if "peta evakuasi" in q:
        return """
🗺 Peta Evakuasi

Peta evakuasi adalah peta yang menunjukkan jalur aman menuju lokasi perlindungan atau titik kumpul saat terjadi bencana.

Informasi yang biasanya ada pada peta evakuasi:

• Jalur evakuasi
• Titik kumpul
• Posko
• Lokasi pengungsian
• Fasilitas kesehatan
• Area rawan bencana
• Arah menuju tempat aman

Catatan:
Jika peta evakuasi spesifik wilayah belum tersedia di SITABA, masyarakat perlu mengikuti arahan BPBD, pemerintah daerah, dan petugas di lapangan.
"""

    if "jalur evakuasi" in q or "rute evakuasi" in q:
        return """
🛣 Jalur Evakuasi

Jalur evakuasi adalah rute yang digunakan masyarakat untuk menuju tempat aman saat terjadi bencana.

Prinsip jalur evakuasi yang aman:

• Menghindari area rawan
• Mudah dilalui
• Memiliki petunjuk arah
• Mengarah ke tempat tinggi untuk tsunami/banjir
• Tidak melewati jembatan atau jalan yang rusak
• Mengikuti arahan petugas

Jika terjadi bencana, jangan memaksakan melewati jalur yang tergenang, tertutup longsor, atau terlihat retak.
"""

    if "titik kumpul" in q:
        return """
📍 Titik Kumpul

Titik kumpul adalah lokasi aman yang digunakan masyarakat berkumpul setelah melakukan evakuasi.

Titik kumpul yang baik:

• Berada di tempat terbuka
• Aman dari bangunan roboh
• Aman dari banjir, longsor, atau tsunami
• Mudah dijangkau
• Diketahui warga sekitar
• Dekat dengan akses bantuan

Contoh titik kumpul:
• Lapangan
• Halaman sekolah
• Balai desa
• Tempat ibadah yang aman
• Posko evakuasi
"""

    if "tempat evakuasi" in q or "lokasi evakuasi" in q:
        return """
🏕 Tempat Evakuasi / Lokasi Pengungsian

Tempat evakuasi adalah lokasi sementara yang digunakan masyarakat terdampak bencana untuk berlindung.

Tempat evakuasi sebaiknya memiliki:

• Akses aman
• Air bersih
• Sanitasi
• Layanan kesehatan
• Tempat istirahat
• Keamanan
• Informasi resmi dari petugas

Untuk lokasi evakuasi spesifik wilayah, ikuti informasi dari BPBD, pemerintah daerah, dan petugas setempat.
"""

    return """
🗺 Informasi Peta dan Jalur Evakuasi

AI SINTA dapat membantu menjelaskan:

• Apa itu peta evakuasi
• Apa itu jalur evakuasi
• Apa itu titik kumpul
• Apa itu tempat pengungsian
• Prinsip memilih rute aman
• Hal yang perlu dihindari saat evakuasi

Untuk peta evakuasi spesifik lokasi, gunakan informasi resmi dari BPBD, pemerintah daerah, atau petugas di lapangan.
"""
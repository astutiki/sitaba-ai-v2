"""
Knowledge Base
Panduan Evakuasi Bencana
AI SINTA
"""


def jawab_evakuasi(pertanyaan):

    q = pertanyaan.lower()

    # ============================================================
    # BANJIR
    # ============================================================

    if "banjir" in q:

        return """
🌊 Panduan Evakuasi Saat Banjir

🚨 Segera evakuasi jika:
• Air terus naik
• Ada peringatan dari BPBD/petugas
• Rumah mulai terendam
• Arus air semakin deras
• Listrik mulai berbahaya

✅ Langkah evakuasi:
• Matikan listrik jika aman dilakukan
• Bawa tas siaga dan dokumen penting
• Evakuasi ke tempat yang lebih tinggi
• Hindari berjalan melewati arus deras
• Jangan memaksakan melewati jalan tergenang
• Ikuti arahan petugas

👨‍👩‍👧 Prioritaskan:
• Anak-anak
• Lansia
• Ibu hamil
• Penyandang disabilitas
• Orang sakit
"""

    # ============================================================
    # LONGSOR
    # ============================================================

    if "longsor" in q:

        return """
⛰ Panduan Evakuasi Saat Longsor

🚨 Segera menjauh jika:
• Terdengar suara gemuruh dari lereng
• Muncul retakan tanah
• Pohon/tiang mulai miring
• Hujan deras berlangsung lama
• Ada material tanah/batu mulai bergerak

✅ Langkah evakuasi:
• Menjauh dari lereng dan tebing
• Jangan melintasi area longsor
• Evakuasi ke lokasi terbuka yang aman
• Waspadai longsor susulan
• Ikuti arahan BPBD dan petugas setempat
"""

    # ============================================================
    # GEMPA
    # ============================================================

    if "gempa" in q:

        return """
🌍 Panduan Evakuasi Saat Gempa

Saat guncangan:
• Drop, Cover, Hold On
• Lindungi kepala dan leher
• Jauhi kaca, lemari, dan benda berat
• Jangan gunakan lift

Setelah guncangan berhenti:
• Keluar melalui jalur evakuasi
• Menuju titik kumpul
• Waspadai bangunan retak
• Jangan kembali sebelum dinyatakan aman

Jika di luar ruangan:
• Menjauh dari bangunan, tiang listrik, pohon, dan baliho
"""

    # ============================================================
    # TSUNAMI
    # ============================================================

    if "tsunami" in q:

        return """
🌊 Panduan Evakuasi Tsunami

🚨 Segera evakuasi jika:
• Terjadi gempa kuat/berlangsung lama di pesisir
• Air laut tiba-tiba surut
• Ada peringatan tsunami

✅ Langkah evakuasi:
• Segera menuju tempat tinggi
• Ikuti jalur evakuasi tsunami
• Jangan menunggu instruksi tambahan jika tanda alam sudah terlihat
• Jangan kembali ke pantai sebelum dinyatakan aman
• Bantu anak-anak, lansia, dan penyandang disabilitas
"""

    # ============================================================
    # ERUPSI
    # ============================================================

    if "erupsi" in q or "gunung api" in q:

        return """
🌋 Panduan Evakuasi Saat Erupsi Gunung Api

✅ Langkah evakuasi:
• Ikuti radius aman dari petugas/PVMBG
• Gunakan masker dan kacamata
• Hindari lembah/sungai yang berpotensi lahar
• Bawa tas siaga dan obat pribadi
• Segera menuju pos pengungsian resmi
• Jangan kembali ke zona bahaya tanpa izin petugas
"""

    # ============================================================
    # KEBAKARAN
    # ============================================================

    if "kebakaran" in q:

        return """
🔥 Panduan Evakuasi Saat Kebakaran

✅ Langkah evakuasi:
• Tetap tenang dan segera keluar
• Jangan gunakan lift
• Merunduk jika ruangan penuh asap
• Tutup hidung dan mulut dengan kain basah jika memungkinkan
• Hubungi pemadam kebakaran
• Jangan kembali mengambil barang
"""

    # ============================================================
    # CUACA EKSTREM
    # ============================================================

    if "cuaca" in q or "angin" in q or "puting beliung" in q:

        return """
🌪 Panduan Evakuasi Saat Cuaca Ekstrem

✅ Langkah aman:
• Masuk ke bangunan yang kokoh
• Jauhi pohon besar, papan reklame, tiang listrik, dan bangunan rapuh
• Hindari berkendara saat hujan/angin sangat kuat
• Pantau informasi BMKG dan petugas setempat
"""

    # ============================================================
    # UMUM
    # ============================================================

    if (
        "evakuasi" in q
        or "mengungsi" in q
        or "pengungsian" in q
        or "titik kumpul" in q
        or "jalur evakuasi" in q
    ):

        return """
🚨 Panduan Umum Evakuasi Bencana

Sebelum evakuasi:
• Tetap tenang
• Dengarkan informasi resmi
• Bawa tas siaga
• Bawa dokumen penting
• Matikan listrik/gas jika aman

Saat evakuasi:
• Ikuti jalur evakuasi
• Jangan berdesakan
• Bantu kelompok rentan
• Hindari area berbahaya
• Ikuti arahan petugas

Setelah sampai di lokasi aman:
• Lapor kepada petugas
• Jangan kembali sebelum dinyatakan aman
• Pantau informasi resmi dari BPBD/BNPB/pemerintah daerah
"""

    return None
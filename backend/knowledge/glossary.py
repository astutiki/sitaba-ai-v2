"""
Knowledge Base
Glosarium Kebencanaan
AI SINTA
"""


def jawab_glosarium(pertanyaan):

    q = pertanyaan.lower()

    glossary = {

        "bencana":
        """🌍 Bencana

Peristiwa atau rangkaian peristiwa yang mengancam dan mengganggu kehidupan masyarakat sehingga menimbulkan korban jiwa, kerusakan lingkungan, kerugian harta benda, dan dampak psikologis.
""",

        "banjir":
        """🌊 Banjir

Peristiwa meluapnya air yang menggenangi wilayah yang biasanya tidak tergenang akibat curah hujan tinggi, luapan sungai, atau drainase yang tidak memadai.
""",

        "banjir bandang":
        """🌊 Banjir Bandang

Banjir yang datang secara tiba-tiba dengan arus deras dan sering membawa material seperti batu, kayu, serta lumpur.
""",

        "longsor":
        """⛰ Tanah Longsor

Pergerakan massa tanah atau batuan menuruni lereng akibat kondisi geologi, hujan, atau aktivitas manusia.
""",

        "gempa":
        """🌍 Gempa Bumi

Getaran permukaan bumi akibat pelepasan energi dari dalam bumi, biasanya disebabkan oleh pergeseran lempeng tektonik.
""",

        "tsunami":
        """🌊 Tsunami

Gelombang laut besar yang dipicu oleh gempa bumi bawah laut, longsor bawah laut, atau aktivitas vulkanik.
""",

        "erupsi":
        """🌋 Erupsi Gunung Api

Peristiwa keluarnya magma, abu vulkanik, gas, dan material lainnya dari gunung api.
""",

        "kekeringan":
        """☀ Kekeringan

Kondisi ketika ketersediaan air jauh di bawah kebutuhan akibat curah hujan yang rendah dalam waktu lama.
""",

        "abrasi":
        """🌊 Abrasi

Proses pengikisan pantai akibat gelombang laut dan arus.
""",

        "cuaca ekstrem":
        """🌪 Cuaca Ekstrem

Kondisi cuaca yang jauh dari keadaan normal seperti hujan sangat lebat, angin kencang, puting beliung, atau suhu ekstrem.
""",

        "mitigasi":
        """🛡 Mitigasi

Serangkaian upaya untuk mengurangi risiko bencana melalui pembangunan fisik maupun peningkatan kapasitas masyarakat.
""",

        "kesiapsiagaan":
        """🎒 Kesiapsiagaan

Serangkaian kegiatan yang dilakukan sebelum bencana terjadi agar masyarakat siap menghadapi keadaan darurat.
""",

        "evakuasi":
        """🚨 Evakuasi

Pemindahan masyarakat dari daerah berbahaya menuju tempat yang lebih aman.
""",

        "pengungsian":
        """🏕 Pengungsian

Tempat sementara bagi masyarakat yang terdampak bencana.
""",

        "rehabilitasi":
        """🏗 Rehabilitasi

Perbaikan dan pemulihan pelayanan publik serta kehidupan masyarakat setelah bencana.
""",

        "rekonstruksi":
        """🏢 Rekonstruksi

Pembangunan kembali infrastruktur dan fasilitas yang rusak agar lebih baik dan lebih tahan terhadap bencana.
""",

        "tanggap darurat":
        """🚑 Tanggap Darurat

Serangkaian kegiatan yang dilakukan segera setelah bencana terjadi untuk menyelamatkan korban dan memenuhi kebutuhan dasar.
""",

        "bpbd":
        """🏢 BPBD

Badan Penanggulangan Bencana Daerah yang bertugas menyelenggarakan penanggulangan bencana di tingkat provinsi maupun kabupaten/kota.
""",

        "bnpb":
        """🏢 BNPB

Badan Nasional Penanggulangan Bencana yang bertugas mengoordinasikan penanggulangan bencana secara nasional.
""",

        "bmkg":
        """🌦 BMKG

Badan Meteorologi, Klimatologi, dan Geofisika yang menyediakan informasi cuaca, iklim, gempa bumi, dan peringatan dini.
""",

        "basarnas":
        """🚁 Basarnas

Badan Nasional Pencarian dan Pertolongan yang melaksanakan operasi pencarian dan penyelamatan korban.
""",

        "posko":
        """🏕 Posko

Pos Komando yang digunakan sebagai pusat koordinasi penanganan bencana.
""",

        "jalur evakuasi":
        """🛣 Jalur Evakuasi

Rute yang telah ditetapkan menuju lokasi aman saat terjadi bencana.
""",

        "titik kumpul":
        """📍 Titik Kumpul

Lokasi aman tempat masyarakat berkumpul setelah melakukan evakuasi.
""",

        "early warning system":
        """📢 Early Warning System (EWS)

Sistem Peringatan Dini yang memberikan informasi sebelum bencana terjadi agar masyarakat dapat segera melakukan tindakan penyelamatan.
""",

        "ews":
        """📢 Early Warning System (EWS)

Sistem Peringatan Dini untuk mengurangi risiko bencana.
""",

        "api sitaba":
        """💻 API SITABA

Layanan antarmuka aplikasi (Application Programming Interface) yang menyediakan data kebencanaan dari SITABA untuk diakses oleh aplikasi lain seperti AI SINTA.
""",

        "sinta":
        """🤖 AI SINTA

Asisten virtual yang membantu masyarakat memperoleh informasi kebencanaan berdasarkan data dan informasi yang tersedia pada SITABA Kementerian Pekerjaan Umum.
""",

        "sitaba":
        """🏛 SITABA

Sistem Informasi Kebencanaan Kementerian Pekerjaan Umum yang menyediakan informasi terkait kejadian bencana, sumber daya, infrastruktur terdampak, publikasi, dan regulasi.
"""
    }

    for kata, jawaban in glossary.items():

        if kata in q:

            return jawaban

    if (
        "glosarium" in q
        or "istilah" in q
        or "arti kata" in q
        or "definisi" in q
    ):

        return """
📖 Glosarium Kebencanaan AI SINTA

AI SINTA dapat menjelaskan berbagai istilah kebencanaan seperti:

• Bencana
• Banjir
• Longsor
• Gempa
• Tsunami
• Erupsi Gunung Api
• Kekeringan
• Abrasi
• Cuaca Ekstrem
• Mitigasi
• Kesiapsiagaan
• Evakuasi
• Pengungsian
• Rehabilitasi
• Rekonstruksi
• Tanggap Darurat
• BPBD
• BNPB
• BMKG
• Basarnas
• Posko
• Jalur Evakuasi
• Titik Kumpul
• Early Warning System (EWS)
• SITABA
• AI SINTA

Silakan ketik nama istilah yang ingin Anda ketahui.
"""

    return None
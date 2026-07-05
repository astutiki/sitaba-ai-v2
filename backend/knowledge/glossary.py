"""
Knowledge Base
Glosarium Kebencanaan
AI SINTA
"""

from difflib import get_close_matches


def jawab_glosarium(pertanyaan):
    q = pertanyaan.lower()

    glossary = {
        "bencana": """🌍 Bencana

Peristiwa atau rangkaian peristiwa yang mengancam dan mengganggu kehidupan masyarakat sehingga menimbulkan korban jiwa, kerusakan lingkungan, kerugian harta benda, dan dampak psikologis.
""",

        "banjir": """🌊 Banjir

Peristiwa meluapnya air yang menggenangi wilayah yang biasanya tidak tergenang akibat curah hujan tinggi, luapan sungai, atau drainase yang tidak memadai.
""",

        "banjir bandang": """🌊 Banjir Bandang

Banjir yang datang secara tiba-tiba dengan arus deras dan sering membawa material seperti batu, kayu, serta lumpur.
""",

        "longsor": """⛰ Tanah Longsor

Pergerakan massa tanah atau batuan menuruni lereng akibat kondisi geologi, hujan, atau aktivitas manusia.
""",

        "gempa": """🌍 Gempa Bumi

Getaran permukaan bumi akibat pelepasan energi dari dalam bumi, biasanya disebabkan oleh pergeseran lempeng tektonik.
""",

        "tsunami": """🌊 Tsunami

Gelombang laut besar yang dipicu oleh gempa bumi bawah laut, longsor bawah laut, atau aktivitas vulkanik.
""",

        "erupsi": """🌋 Erupsi Gunung Api

Peristiwa keluarnya magma, abu vulkanik, gas, dan material lainnya dari gunung api.
""",

        "kekeringan": """☀ Kekeringan

Kondisi ketika ketersediaan air jauh di bawah kebutuhan akibat curah hujan yang rendah dalam waktu lama.
""",

        "abrasi": """🌊 Abrasi

Proses pengikisan pantai akibat gelombang laut dan arus.
""",

        "cuaca ekstrem": """🌪 Cuaca Ekstrem

Kondisi cuaca yang jauh dari keadaan normal seperti hujan sangat lebat, angin kencang, puting beliung, atau suhu ekstrem.
""",

        "cuaca ekstrim": """🌪 Cuaca Ekstrem

Kondisi cuaca yang jauh dari keadaan normal seperti hujan sangat lebat, angin kencang, puting beliung, atau suhu ekstrem.
""",

        "mitigasi": """🛡 Mitigasi

Serangkaian upaya untuk mengurangi risiko bencana melalui pembangunan fisik, peningkatan kapasitas masyarakat, edukasi, perencanaan tata ruang, dan penguatan sistem peringatan dini.
""",

        "kesiapsiagaan": """🎒 Kesiapsiagaan

Serangkaian kegiatan yang dilakukan sebelum bencana terjadi agar masyarakat, pemerintah, dan lembaga terkait siap menghadapi keadaan darurat.
""",

        "evakuasi": """🚨 Evakuasi

Pemindahan masyarakat dari daerah berbahaya menuju tempat yang lebih aman untuk mengurangi risiko korban jiwa.
""",

        "pengungsian": """🏕 Pengungsian

Tempat sementara bagi masyarakat yang terdampak bencana untuk mendapatkan perlindungan, bantuan dasar, dan layanan darurat.
""",

        "rehabilitasi": """🏗 Rehabilitasi

Perbaikan dan pemulihan pelayanan publik, sarana, prasarana, lingkungan, serta kehidupan masyarakat setelah bencana agar kembali berfungsi secara normal.
""",

        "rehabililitasi": """🏗 Rehabilitasi

Perbaikan dan pemulihan pelayanan publik, sarana, prasarana, lingkungan, serta kehidupan masyarakat setelah bencana agar kembali berfungsi secara normal.
""",

        "rehap": """🏗 Rehap (Rehabilitasi)

Rehap merupakan singkatan dari Rehabilitasi, yaitu upaya perbaikan dan pemulihan pelayanan publik, sarana, prasarana, serta kehidupan masyarakat setelah terjadi bencana agar dapat berfungsi kembali secara normal.
""",

        "rehab": """🏗 Rehab (Rehabilitasi)

Rehab merupakan singkatan dari Rehabilitasi, yaitu upaya perbaikan dan pemulihan pelayanan publik, sarana, prasarana, serta kehidupan masyarakat setelah terjadi bencana agar dapat berfungsi kembali secara normal.
""",

        "rekonstruksi": """🏢 Rekonstruksi

Pembangunan kembali infrastruktur, fasilitas umum, permukiman, dan sistem kehidupan masyarakat yang rusak akibat bencana agar lebih baik, lebih aman, dan lebih tahan terhadap bencana.
""",

        "rekon": """🏢 Rekon (Rekonstruksi)

Rekon merupakan singkatan dari Rekonstruksi, yaitu pembangunan kembali seluruh sarana, prasarana, dan sistem kehidupan masyarakat yang rusak akibat bencana dengan prinsip membangun lebih baik, lebih aman, dan lebih tangguh.
""",

        "rehap rekon": """🏗 
        Rehab-Rekon (Rehabilitasi dan Rekonstruksi)
Rehab-Rekon adalah dua tahapan dalam manajemen penanggulangan bencana yang berfokus pada pemulihan wilayah pascabencana. Istilah ini merujuk pada upaya mengembalikan fungsi fasilitas umum, rumah warga, dan kehidupan masyarakat ke kondisi normal atau bahkan lebih baik.
""",

        "rehab rekon": """🏗 Rehab-Rekon (Rehabilitasi dan Rekonstruksi)

Rehab-Rekon adalah dua tahapan dalam manajemen penanggulangan bencana yang berfokus pada pemulihan wilayah pascabencana. Istilah ini merujuk pada upaya mengembalikan fungsi fasilitas umum, rumah warga, dan kehidupan masyarakat ke kondisi normal atau bahkan lebih baik.
""",

        "tanggap darurat": """🚑 Tanggap Darurat

Serangkaian kegiatan yang dilakukan segera setelah bencana terjadi untuk menyelamatkan korban, memenuhi kebutuhan dasar, melindungi kelompok rentan, dan memulihkan fungsi layanan penting.
""",

        "bpbd": """🏢 BPBD

Badan Penanggulangan Bencana Daerah yang bertugas menyelenggarakan penanggulangan bencana di tingkat provinsi maupun kabupaten/kota.
""",

        "bnpb": """🏢 BNPB

Badan Nasional Penanggulangan Bencana yang bertugas mengoordinasikan penanggulangan bencana secara nasional.
""",

        "bmkg": """🌦 BMKG

Badan Meteorologi, Klimatologi, dan Geofisika yang menyediakan informasi cuaca, iklim, gempa bumi, tsunami, dan peringatan dini.
""",

        "basarnas": """🚁 Basarnas

Badan Nasional Pencarian dan Pertolongan yang melaksanakan operasi pencarian dan penyelamatan korban.
""",

        "posko": """🏕 Posko

Pos Komando yang digunakan sebagai pusat koordinasi penanganan bencana.
""",

        "pos komando": """🏢 Pos Komando

Pos Komando merupakan pusat koordinasi penanganan bencana yang berfungsi mengendalikan operasi tanggap darurat, komunikasi, dan distribusi bantuan.
""",

        "pos lapangan": """🏕 Pos Lapangan

Pos Lapangan adalah lokasi operasional di area terdampak bencana yang digunakan untuk mendukung evakuasi, pencarian, penyelamatan, dan distribusi bantuan.
""",

        "jalur evakuasi": """🛣 Jalur Evakuasi

Rute yang telah ditetapkan menuju lokasi aman saat terjadi bencana.
""",

        "titik kumpul": """📍 Titik Kumpul

Lokasi aman tempat masyarakat berkumpul setelah melakukan evakuasi.
""",

        "early warning system": """📢 Early Warning System (EWS)

Sistem Peringatan Dini yang memberikan informasi sebelum bencana terjadi agar masyarakat dapat segera melakukan tindakan penyelamatan.
""",

        "ews": """📢 Early Warning System (EWS)

Sistem Peringatan Dini untuk mengurangi risiko bencana.
""",

        "ancaman": """⚠ Ancaman (Hazard)

Ancaman adalah suatu kejadian, fenomena, atau kondisi alam maupun nonalam yang berpotensi menimbulkan bencana.
""",

        "hazard": """⚠ Hazard

Hazard adalah istilah bahasa Inggris dari Ancaman, yaitu kondisi atau peristiwa yang berpotensi menimbulkan bencana.
""",

        "risiko bencana": """📊 Risiko Bencana

Risiko Bencana adalah potensi kerugian akibat suatu ancaman terhadap masyarakat dengan mempertimbangkan kerentanan dan kapasitas.
""",

        "kerentanan": """🏚 Kerentanan (Vulnerability)

Kerentanan adalah kondisi yang menyebabkan masyarakat, bangunan, lingkungan, atau sistem menjadi lebih mudah terdampak oleh ancaman bencana.
""",

        "vulnerability": """🏚 Vulnerability

Vulnerability adalah istilah bahasa Inggris dari Kerentanan.
""",

        "kapasitas": """💪 Kapasitas (Capacity)

Kapasitas adalah kemampuan individu, masyarakat, pemerintah, dan organisasi dalam mengantisipasi, menghadapi, merespons, dan pulih dari dampak bencana.
""",

        "capacity": """💪 Capacity

Capacity adalah istilah bahasa Inggris dari Kapasitas.
""",

        "resiliensi": """🛡 Resiliensi

Resiliensi adalah kemampuan masyarakat, wilayah, atau sistem untuk bertahan, beradaptasi, dan pulih kembali secara cepat setelah mengalami bencana.
""",

        "build back better": """🏗 Build Back Better

Build Back Better adalah prinsip pembangunan kembali pascabencana dengan menghasilkan infrastruktur, lingkungan, dan sistem kehidupan yang lebih baik, lebih aman, dan lebih tangguh.
""",

        "krb": """🗺 KRB (Kawasan Rawan Bencana)

Kawasan Rawan Bencana adalah wilayah yang memiliki tingkat potensi ancaman bencana berdasarkan kondisi geologi, hidrologi, meteorologi, maupun faktor lainnya.
""",

        "kawasan rawan bencana": """🗺 Kawasan Rawan Bencana (KRB)

Wilayah yang memiliki potensi tinggi mengalami bencana sehingga memerlukan perhatian khusus dalam pembangunan dan mitigasi.
""",

        "kaji cepat": """📋 Kaji Cepat

Kaji Cepat merupakan penilaian awal setelah terjadi bencana untuk mengetahui lokasi terdampak, jumlah korban, tingkat kerusakan, kebutuhan mendesak, dan tindakan penanganan yang harus dilakukan.
""",

        "logistik": """📦 Logistik

Logistik bencana adalah barang dan kebutuhan dasar untuk penanganan bencana seperti makanan, air bersih, obat-obatan, tenda, selimut, pakaian, dan perlengkapan darurat.
""",

        "huntara": """🏠 Hunian Sementara (Huntara)

Hunian Sementara adalah tempat tinggal sementara bagi masyarakat terdampak bencana sebelum memperoleh hunian tetap.
""",

        "hunian sementara": """🏠 Hunian Sementara (Huntara)

Tempat tinggal sementara yang disediakan selama masa rehabilitasi dan rekonstruksi pascabencana.
""",

        "huntap": """🏡 Hunian Tetap (Huntap)

Hunian Tetap adalah rumah permanen yang dibangun bagi masyarakat terdampak bencana sebagai tempat tinggal jangka panjang.
""",

        "hunian tetap": """🏡 Hunian Tetap (Huntap)

Rumah permanen yang dibangun untuk menggantikan tempat tinggal yang rusak akibat bencana.
""",

        "infrastruktur kritis": """🏗 Infrastruktur Kritis

Infrastruktur Kritis adalah fasilitas penting bagi keberlangsungan pelayanan masyarakat seperti jalan, jembatan, bendungan, rumah sakit, listrik, air bersih, dan telekomunikasi.
""",

        "kerusakan": """🏚 Kerusakan

Kerusakan adalah kondisi rusaknya bangunan, infrastruktur, fasilitas umum, maupun lingkungan akibat bencana.
""",

        "kerugian": """💰 Kerugian

Kerugian adalah kehilangan akibat bencana, baik berupa kerugian ekonomi, sosial, lingkungan, maupun terganggunya aktivitas masyarakat.
""",

        "korban terdampak": """👥 Korban Terdampak

Korban Terdampak adalah masyarakat yang mengalami dampak langsung maupun tidak langsung akibat bencana.
""",

        "korban mengungsi": """🏕 Korban Mengungsi

Korban Mengungsi adalah masyarakat yang harus meninggalkan tempat tinggalnya menuju lokasi yang lebih aman akibat ancaman atau dampak bencana.
""",

        "pusdalops": """📡 Pusdalops

Pusat Pengendalian Operasi Penanggulangan Bencana adalah unit yang melakukan pemantauan, pengumpulan informasi, koordinasi, komunikasi, dan pelaporan penanganan bencana.
""",

        "inarisk": """🗺 InaRISK

InaRISK merupakan platform BNPB yang menyediakan informasi risiko bencana di seluruh wilayah Indonesia.
""",

        "inasafe": """💻 InaSAFE

InaSAFE adalah perangkat lunak berbasis Sistem Informasi Geografis untuk menganalisis dampak potensi bencana terhadap penduduk, bangunan, dan infrastruktur.
""",

        "dsp": """💵 Dana Siap Pakai (DSP)

Dana Siap Pakai adalah dana yang disediakan pemerintah melalui BNPB untuk mendukung kegiatan tanggap darurat bencana.
""",

        "dana siap pakai": """💵 Dana Siap Pakai (DSP)

Dana pemerintah yang digunakan secara cepat untuk mendukung penanganan darurat bencana sesuai ketentuan.
""",

        "api sitaba": """💻 API SITABA

Layanan antarmuka aplikasi yang menyediakan data kebencanaan dari SITABA untuk diakses oleh aplikasi lain seperti AI SINTA.
""",

        "sinta": """🤖 AI SINTA

Asisten virtual yang membantu masyarakat memperoleh informasi kebencanaan berdasarkan data SITABA Kementerian Pekerjaan Umum.
""",

        "sitaba": """🏛 SITABA

Sistem Informasi Kebencanaan Kementerian Pekerjaan Umum yang menyediakan informasi kejadian bencana, sumber daya, infrastruktur terdampak, publikasi, dan regulasi.
""",
    }

    for kata, jawaban in glossary.items():
        if kata in q:
            return jawaban

    for token in q.split():
        cocok = get_close_matches(token, glossary.keys(), n=1, cutoff=0.78)
        if cocok:
            return glossary[cocok[0]]

    if any(k in q for k in [
        "glosarium", "istilah", "arti kata", "definisi", "pengertian",
        "pengertiannya", "apa itu", "apaan", "apa maksudnya",
        "itu apa", "artinya apa", "maksud", "jelaskan", "adalah"
    ]):
        return """📖 Glosarium Kebencanaan AI SINTA

AI SINTA dapat menjelaskan istilah seperti: bencana, banjir, longsor, gempa, tsunami, cuaca ekstrem, mitigasi, kesiapsiagaan, evakuasi, rehabilitasi, rekonstruksi, rehap rekon, huntara, huntap, KRB, Pusdalops, InaRISK, InaSAFE, dan DSP.
"""

    return None
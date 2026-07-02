"""
Knowledge Base
Potensi / Penyebab Bencana
AI SINTA
"""


def jawab_potensi_bencana(pertanyaan):

    q = pertanyaan.lower()

    # ==================================
    # BANJIR
    # ==================================

    if "banjir" in q:

        return """
🌊 Potensi Terjadinya Banjir

Penyebab utama:

• Curah hujan tinggi
• Luapan sungai
• Drainase tidak berfungsi
• Pendangkalan sungai
• Sampah yang menyumbat saluran
• Alih fungsi lahan
• Berkurangnya daerah resapan air
• Pasang air laut (rob)

Wilayah yang berpotensi:

• Dataran rendah
• Bantaran sungai
• Kawasan perkotaan dengan drainase buruk
• Wilayah pesisir

Upaya mitigasi:

• Membersihkan saluran air
• Tidak membuang sampah ke sungai
• Menambah daerah resapan
• Normalisasi sungai
"""

    # ==================================
    # LONGSOR
    # ==================================

    if "longsor" in q:

        return """
⛰ Potensi Tanah Longsor

Penyebab:

• Curah hujan tinggi
• Lereng terjal
• Tanah labil
• Penebangan hutan
• Getaran gempa
• Beban bangunan pada lereng

Wilayah berpotensi:

• Pegunungan
• Perbukitan
• Tebing jalan
• Lereng sungai

Mitigasi:

• Menanam vegetasi
• Membuat drainase lereng
• Tidak membangun di lereng rawan
• Pemantauan retakan tanah
"""

    # ==================================
    # GEMPA
    # ==================================

    if "gempa" in q:

        return """
🌍 Potensi Gempabumi

Penyebab:

• Pergeseran lempeng tektonik
• Aktivitas sesar aktif
• Aktivitas vulkanik

Wilayah berpotensi:

• Dekat sesar aktif
• Zona subduksi
• Kawasan gunung api

Mitigasi:

• Bangunan tahan gempa
• Jalur evakuasi
• Simulasi gempa
• Edukasi masyarakat
"""

    # ==================================
    # TSUNAMI
    # ==================================

    if "tsunami" in q:

        return """
🌊 Potensi Tsunami

Penyebab:

• Gempa bawah laut
• Longsor bawah laut
• Aktivitas gunung api laut

Wilayah berpotensi:

• Pesisir Samudera Hindia
• Pesisir Pasifik
• Pantai dekat zona subduksi

Mitigasi:

• Sistem peringatan dini
• Jalur evakuasi
• Evakuasi ke tempat tinggi
"""

    # ==================================
    # KEKERINGAN
    # ==================================

    if "kekeringan" in q:

        return """
☀ Potensi Kekeringan

Penyebab:

• Curah hujan rendah
• Musim kemarau panjang
• Fenomena El Nino
• Kerusakan daerah resapan

Wilayah berpotensi:

• Daerah tadah hujan
• Wilayah kering
• Daerah dengan irigasi terbatas

Mitigasi:

• Penghematan air
• Embung
• Waduk
• Sumur resapan
"""

    # ==================================
    # CUACA EKSTRIM
    # ==================================

    if "cuaca" in q:

        return """
🌪 Potensi Cuaca Ekstrem

Penyebab:

• Perubahan iklim
• Angin kencang
• Hujan lebat
• Puting beliung

Potensi dampak:

• Pohon tumbang
• Atap rumah rusak
• Banjir
• Longsor
"""

    # ==================================
    # ERUPSI
    # ==================================

    if "erupsi" in q or "gunung api" in q:

        return """
🌋 Potensi Erupsi Gunung Api

Penyebab:

• Aktivitas magma
• Tekanan gas vulkanik

Potensi bahaya:

• Abu vulkanik
• Lava
• Awan panas
• Lahar
• Gas beracun

Mitigasi:

• Mematuhi zona bahaya
• Mengikuti informasi PVMBG
• Evakuasi sesuai arahan petugas
"""

    # ==================================
    # ABRASI
    # ==================================

    if "abrasi" in q:

        return """
🌊 Potensi Abrasi Pantai

Penyebab:

• Gelombang tinggi
• Arus laut
• Hilangnya mangrove
• Perubahan garis pantai

Mitigasi:

• Penanaman mangrove
• Breakwater
• Rehabilitasi pantai
"""

    # ==================================
    # UMUM
    # ==================================

    if (
        "potensi" in q
        or "penyebab" in q
        or "rawan" in q
    ):

        return """
📊 Potensi Bencana di Indonesia

Jenis bencana yang sering terjadi:

• Banjir
• Tanah longsor
• Gempa bumi
• Tsunami
• Erupsi gunung api
• Kekeringan
• Cuaca ekstrem
• Abrasi

Faktor penyebab:

• Kondisi geografis Indonesia
• Pertemuan tiga lempeng tektonik
• Curah hujan tinggi
• Perubahan iklim
• Aktivitas manusia
"""

    return None
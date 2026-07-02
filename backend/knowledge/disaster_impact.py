"""
Knowledge Base
Dampak dan Kerugian Bencana
AI SINTA - SITABA
"""


def jawab_dampak_bencana(pertanyaan):

    q = pertanyaan.lower()

    # ==========================
    # BANJIR
    # ==========================

    if "banjir" in q:

        return """
🌊 Dampak Bencana Banjir

🏚 Dampak Fisik
• Rumah dan permukiman terendam
• Jalan dan jembatan rusak
• Drainase tersumbat
• Fasilitas umum terganggu

💰 Dampak Ekonomi
• Aktivitas perdagangan berhenti
• Kerugian usaha masyarakat
• Kerusakan kendaraan
• Kerusakan lahan pertanian

👨‍👩‍👧 Dampak Sosial
• Pengungsian
• Gangguan pendidikan
• Gangguan kesehatan
• Kekurangan air bersih

⚠ Potensi Risiko
• Penyakit pasca banjir
• Longsor
• Listrik padam
• Gangguan transportasi
"""

    # ==========================
    # LONGSOR
    # ==========================

    if "longsor" in q:

        return """
⛰ Dampak Tanah Longsor

🏚 Kerusakan
• Rumah tertimbun
• Jalan tertutup material
• Jembatan rusak
• Saluran irigasi rusak

💰 Kerugian
• Kerugian ekonomi masyarakat
• Biaya evakuasi
• Biaya pemulihan infrastruktur

👨‍👩‍👧 Dampak Sosial
• Korban jiwa
• Pengungsian
• Isolasi wilayah
• Gangguan distribusi logistik

⚠ Risiko Lanjutan
• Longsor susulan
• Putusnya akses jalan
"""

    # ==========================
    # GEMPA
    # ==========================

    if "gempa" in q:

        return """
🌍 Dampak Gempabumi

🏚 Kerusakan
• Bangunan roboh
• Jalan retak
• Jembatan rusak
• Bendungan terdampak

💰 Kerugian
• Kerusakan aset masyarakat
• Gangguan ekonomi
• Biaya rehabilitasi

👨‍👩‍👧 Dampak Sosial
• Korban jiwa
• Luka-luka
• Trauma psikologis
• Pengungsian

⚠ Risiko Lanjutan
• Gempa susulan
• Tsunami (wilayah pesisir)
"""

    # ==========================
    # KEKERINGAN
    # ==========================

    if "kekeringan" in q:

        return """
🌞 Dampak Kekeringan

• Kekurangan air bersih
• Gagal panen
• Penurunan produksi pangan
• Kebakaran lahan
• Gangguan kesehatan
"""

    # ==========================
    # ERUPSI
    # ==========================

    if "erupsi" in q or "gunung api" in q:

        return """
🌋 Dampak Erupsi Gunung Api

• Abu vulkanik
• Gangguan penerbangan
• Kerusakan tanaman
• Gangguan kesehatan
• Pengungsian
• Lahar hujan
"""

    # ==========================
    # CUACA EKSTRIM
    # ==========================

    if "cuaca" in q:

        return """
🌪 Dampak Cuaca Ekstrem

• Pohon tumbang
• Atap rumah rusak
• Jalan tertutup
• Listrik padam
• Gangguan transportasi
"""

    # ==========================
    # KERUGIAN
    # ==========================

    if (
        "kerugian" in q
        or "dampak" in q
        or "kerusakan" in q
    ):

        return """
📊 Dampak Umum Bencana

🏚 Infrastruktur
• Jalan Nasional
• Jalan Daerah
• Jembatan
• Drainase
• Bendungan
• Bangunan pemerintah
• Sekolah
• Rumah sakit

💰 Ekonomi
• Kerusakan aset
• Gangguan perdagangan
• Kerugian UMKM
• Kerusakan pertanian
• Gangguan logistik

👨‍👩‍👧 Sosial
• Korban jiwa
• Luka-luka
• Pengungsian
• Trauma psikologis

🌱 Lingkungan
• Kerusakan hutan
• Pencemaran air
• Erosi tanah
• Kerusakan ekosistem

🏛 Pemerintah
• Biaya tanggap darurat
• Biaya rehabilitasi
• Biaya rekonstruksi
"""

    return None
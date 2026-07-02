"""
Intent Router
Otak awal AI SINTA untuk menentukan jenis pertanyaan pengguna.
"""


def deteksi_intent(pertanyaan: str):
    q = pertanyaan.lower()

    # ==========================
    # OUT OF SCOPE
    # ==========================
    kata_outscope = [
        "presiden", "wakil presiden", "menteri", "gubernur",
        "bupati", "walikota", "wali kota", "pemilu", "politik",
        "prabowo", "jokowi", "gibran", "anies", "ganjar",
        "film", "musik", "artis", "sepak bola", "liga",
        "bitcoin", "crypto", "saham", "resep", "makanan",
        "chatgpt", "gemini", "google", "instagram", "whatsapp",
    ]

    for kata in kata_outscope:
        if kata in q:
            return "OUT_OF_SCOPE"

    # ==========================
    # INFORMASI UMUM
    # ==========================
    if (
        "apa itu sitaba" in q
        or "sitaba itu apa" in q
        or "apa itu sinta" in q
        or "ai sinta" in q
        or "fitur sitaba" in q
        or "menu sitaba" in q
        or "bisa tanya apa" in q
        or "informasi apa saja" in q
    ):
        return "PUBLIC_INFORMATION"

    # ==========================
    # FAQ
    # ==========================
    if (
        "faq" in q
        or "pertanyaan umum" in q
        or "contoh pertanyaan" in q
        or "cara menggunakan" in q
        or "cara pakai" in q
    ):
        return "FAQ"

    # ==========================
    # KONTAK DARURAT
    # ==========================
    if (
        "kontak darurat" in q
        or "nomor darurat" in q
        or "call center" in q
        or "hubungi siapa" in q
        or "bantuan darurat" in q
        or "nomor bantuan" in q
    ):
        return "EMERGENCY_CONTACT"

    # ==========================
    # EVAKUASI
    # ==========================
    if (
        "evakuasi" in q
        or "mengungsi" in q
        or "pengungsian" in q
        or "titik kumpul" in q
        or "jalur evakuasi" in q
    ):
        return "EVACUATION"

    # ==========================
    # PERTOLONGAN PERTAMA
    # ==========================
    if (
        "p3k" in q
        or "pertolongan pertama" in q
        or "first aid" in q
        or "luka" in q
        or "pingsan" in q
        or "berdarah" in q
        or "patah" in q
        or "tersetrum" in q
        or "kesetrum" in q
        or "luka bakar" in q
    ):
        return "FIRST_AID"

    # ==========================
    # DAMPAK / KERUGIAN
    # ==========================
    if (
        "dampak" in q
        or "kerugian" in q
        or "kerusakan" in q
        or "dampak ekonomi" in q
        or "biaya akibat bencana" in q
    ):
        return "DISASTER_IMPACT"

    # ==========================
    # POTENSI / PENYEBAB
    # ==========================
    if (
        "potensi" in q
        or "penyebab" in q
        or "rawan" in q
        or "kenapa terjadi" in q
        or "mengapa terjadi" in q
    ):
        return "DISASTER_POTENTIAL"

    # ==========================
    # MITIGASI
    # ==========================
    if (
        "mitigasi" in q
        or "apa yang harus dilakukan" in q
        or "bagaimana menghadapi" in q
        or "cara menghadapi" in q
        or "cara mengatasi" in q
    ):
        return "MITIGATION"

    # ==========================
    # KESIAPSIAGAAN
    # ==========================
    if (
        "kesiapsiagaan" in q
        or "preparedness" in q
        or "persiapan" in q
        or "sebelum bencana" in q
        or "tas siaga" in q
        or "apa yang harus disiapkan" in q
    ):
        return "PREPAREDNESS"

    # ==========================
    # STATISTIK
    # ==========================
    if (
        "statistik" in q
        or "berapa kali" in q
        or "jumlah kejadian" in q
        or "berapa kejadian" in q
        or "paling banyak" in q
        or "total bencana" in q
    ):
        return "STATISTICS"

    # ==========================
    # INFRASTRUKTUR
    # ==========================
    if (
        "infrastruktur" in q
        or "ruas jalan" in q
        or "jalan terdampak" in q
        or "jembatan" in q
        or "bendungan" in q
        or "drainase" in q
    ):
        return "INFRASTRUCTURE"

    # ==========================
    # RESOURCE
    # ==========================
    if (
        "personel" in q
        or "alat" in q
        or "material" in q
        or "bahan" in q
        or "logistik" in q
    ):
        return "RESOURCE"

    # ==========================
    # BERITA
    # ==========================
    if (
        "berita" in q
        or "info pu" in q
        or "kabar" in q
    ):
        return "NEWS"

    # ==========================
    # PUBLIKASI / REGULASI
    # ==========================
    if (
        "publikasi" in q
        or "regulasi" in q
        or "peraturan" in q
        or "surat edaran" in q
        or "pedoman" in q
    ):
        return "PUBLICATION"

    # ==========================
    # DATA BENCANA
    # ==========================
    if (
        "bencana" in q
        or "banjir" in q
        or "longsor" in q
        or "gempa" in q
        or "tsunami" in q
        or "kekeringan" in q
        or "erupsi" in q
        or "cuaca ekstrem" in q
        or "cuaca ekstrim" in q
        or "kebakaran" in q
        or "abrasi" in q
    ):
        return "DISASTER"

    # ==========================
    # DEFAULT
    # ==========================
    return "GENERAL"
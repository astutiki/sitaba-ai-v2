"""
Intent Router
AI SINTA
"""


def deteksi_intent(pertanyaan: str):
    q = pertanyaan.lower()

    OUT_SCOPE = [
        "presiden", "menteri", "gubernur", "bupati", "walikota",
        "wali kota", "pemilu", "politik", "film", "musik",
        "artis", "sepak bola", "bitcoin", "crypto", "chatgpt", "gemini",
    ]

    if any(k in q for k in OUT_SCOPE):
        return "OUT_OF_SCOPE"

    GLOSSARY = [
        "apa itu", "pengertian", "definisi", "arti", "artinya",
        "maksud", "jelaskan", "istilah", "glosarium",
        "pengertianya", "artinya apa", "maksudnya apa",
        "apa maksudnya", "rehap", "rehab", "rekon",
        "rehabilitasi", "rekonstruksi", "apaan",
    ]

    if any(k in q for k in GLOSSARY):
        return "GLOSSARY"

    # Harus sebelum DISASTER karena mengandung kata "bencana"
    REPORTING_CHANNEL = [
        "lapor bencana",
        "laporkan bencana",
        "pelaporan bencana",
        "kanal pelaporan",
        "cara melapor",
        "cara melaporkan",
        "laporan masyarakat",
        "nomor pelaporan",
        "nomor pengaduan",
        "call center sitaba",
        "call center bencana",
        "whatsapp sitaba",
        "wa sitaba",
        "kontak sitaba",
        "hubungi sitaba",
        "ingin melapor",
    ]

    if any(k in q for k in REPORTING_CHANNEL):
        return "REPORTING_CHANNEL"

    # Gempa harus diperiksa sebelum statistik dan bencana umum
    GEMPA_KEYWORDS = [
        "gempa",
        "gempa bumi",
        "gempa terkini",
        "gempa terbaru",
        "magnitudo",
        "magnitude",
        "pusat gempa",
        "episentrum",
        "kedalaman gempa",
        "potensi tsunami",
    ]

    if any(k in q for k in GEMPA_KEYWORDS):
        return "EARTHQUAKE"

    RESOURCE = [
        "alat", "alat berat", "material", "bahan", "logistik",
        "personel", "excavator", "bulldozer", "dump truck",
        "genset", "pompa", "perahu", "mobil toilet",
        "toilet", "kendaraan pelayanan khusus",
        "aset", "asset", "digunakan", "dipakai",
        "dibutuhkan", "diterjunkan", "stok",
        "tersedia", "sumber daya",
    ]

    if any(k in q for k in RESOURCE):
        return "RESOURCE"

    STATISTICS = [
        "statistik", "jumlah", "berapa", "total", "grafik",
        "trend", "tren", "paling banyak",
    ]

    if any(k in q for k in STATISTICS):
        return "STATISTICS"

    INFRA = [
        "jalan", "jembatan", "bendungan",
        "irigasi", "drainase", "infrastruktur",
    ]

    if any(k in q for k in INFRA):
        return "INFRASTRUCTURE"

    PUBLICATION = [
        "regulasi", "peraturan", "publikasi",
        "surat edaran", "pedoman",
    ]

    if any(k in q for k in PUBLICATION):
        return "PUBLICATION"

    NEWS = [
        "berita", "kabar", "info pu",
    ]

    if any(k in q for k in NEWS):
        return "NEWS"

    if "mitigasi" in q:
        return "MITIGATION"

    if "kesiapsiagaan" in q:
        return "PREPAREDNESS"

    if "evakuasi" in q:
        return "EVACUATION"

    if "kontak darurat" in q or "nomor darurat" in q:
        return "EMERGENCY_CONTACT"

    if (
        "p3k" in q
        or "pertolongan pertama" in q
        or "first aid" in q
    ):
        return "FIRST_AID"

    if "sitaba" in q or "ai sinta" in q:
        return "PUBLIC_INFORMATION"

    if "faq" in q:
        return "FAQ"

    DISASTER = [
        "bencana", "banjir", "longsor", "tsunami",
        "erupsi", "kekeringan", "abrasi", "cuaca ekstrem",
        "cuaca ekstrim", "kebakaran",
    ]

    if any(k in q for k in DISASTER):
        return "DISASTER"

    return "GENERAL"
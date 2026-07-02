"""
Knowledge Base
Kontak Darurat Bencana
AI SINTA
"""


def jawab_kontak_darurat(pertanyaan):

    q = pertanyaan.lower()

    if (
        "kontak darurat" not in q
        and "nomor darurat" not in q
        and "call center" not in q
        and "hubungi siapa" not in q
        and "bantuan darurat" not in q
        and "nomor bantuan" not in q
    ):
        return None

    return """
☎ Kontak Darurat yang Dapat Dihubungi

🚨 Layanan Darurat Nasional
• 112

🏥 Ambulans / Kedaruratan Medis
• 119

🚒 Pemadam Kebakaran
• 113

👮 Kepolisian
• 110

🚢 Basarnas / SAR
• 115

🌧 Informasi Cuaca, Gempa, dan Peringatan Dini
• BMKG: 196

🏛 Kebencanaan Daerah
• Hubungi BPBD provinsi/kabupaten/kota setempat.

📌 Catatan:
Jika kondisi mengancam keselamatan jiwa, segera hubungi 112 atau petugas terdekat. Ikuti arahan resmi dari BPBD, BNPB, Basarnas, TNI/Polri, dan pemerintah daerah.
"""
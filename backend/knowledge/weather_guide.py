"""
Knowledge Base
Panduan Cuaca dan Kaitannya dengan Bencana
AI SINTA
"""


def jawab_panduan_cuaca(pertanyaan):

    q = pertanyaan.lower()

    if (
        "cuaca" not in q
        and "hujan" not in q
        and "bmkg" not in q
        and "angin" not in q
        and "peringatan dini" not in q
        and "hidrometeorologi" not in q
    ):
        return None

    if "hujan lebat" in q or "curah hujan" in q:
        return """
🌧 Hujan Lebat dan Risiko Bencana

Hujan lebat dapat meningkatkan risiko:

• Banjir
• Banjir bandang
• Tanah longsor
• Genangan
• Jalan licin
• Gangguan drainase

Yang perlu dilakukan:

• Pantau informasi BMKG.
• Hindari melintasi daerah banjir.
• Waspadai lereng, tebing, dan bantaran sungai.
• Bersihkan saluran air di lingkungan sekitar.
"""

    if "angin" in q or "puting beliung" in q:
        return """
🌪 Angin Kencang dan Puting Beliung

Potensi dampak:

• Pohon tumbang
• Atap rumah rusak
• Tiang listrik roboh
• Gangguan transportasi
• Bangunan ringan terdampak

Yang perlu dilakukan:

• Hindari berteduh di bawah pohon.
• Jauhi papan reklame dan tiang listrik.
• Amankan benda di luar rumah.
• Masuk ke bangunan yang kokoh.
"""

    if "peringatan dini" in q:
        return """
📢 Peringatan Dini Cuaca

Peringatan dini adalah informasi awal mengenai potensi cuaca berbahaya.

Masyarakat disarankan:

• Mengikuti informasi resmi BMKG, BPBD, BNPB, dan pemerintah daerah.
• Tidak menyebarkan informasi yang belum terverifikasi.
• Menyiapkan tas siaga bila berada di daerah rawan.
• Mengikuti arahan petugas di lapangan.
"""

    if "bmkg" in q:
        return """
🌦 BMKG

BMKG menyediakan informasi mengenai:

• Prakiraan cuaca
• Peringatan dini cuaca ekstrem
• Gempa bumi
• Tsunami
• Iklim

Untuk informasi cuaca terkini, masyarakat disarankan memantau kanal resmi BMKG.
"""

    if "hidrometeorologi" in q:
        return """
🌧 Bencana Hidrometeorologi

Bencana hidrometeorologi berkaitan dengan cuaca, iklim, dan air.

Contohnya:

• Banjir
• Tanah longsor
• Kekeringan
• Cuaca ekstrem
• Angin kencang
• Gelombang pasang
• Abrasi
"""

    return """
🌦 Panduan Cuaca dan Kebencanaan

Kondisi cuaca dapat memengaruhi risiko bencana, terutama bencana hidrometeorologi.

Contoh hubungan cuaca dan bencana:

• Hujan lebat → banjir dan longsor
• Angin kencang → pohon tumbang dan kerusakan bangunan
• Kemarau panjang → kekeringan dan kebakaran lahan
• Gelombang tinggi → abrasi dan gangguan pesisir

Gunakan informasi resmi dari BMKG, BPBD, BNPB, dan pemerintah daerah untuk mengambil keputusan yang aman.
"""
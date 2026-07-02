from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import requests
import re
from collections import Counter
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont
import textwrap

app = FastAPI(
    title="SINTA API",
    description="Backend AI SITABA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sitaba-ai.vercel.app",
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"

SITABA_NEW_DISASTER_API = "https://sitaba.pu.go.id/api-public/noauth/new-disaster/"

import os
from datetime import datetime

LAST_REPLY = ""
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

LAST_RESPONSE = {
    "question": "",
    "answer": "",
    "source": "",
    "created_at": ""
}

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)


def get_bencana_terkini():
    try:
        res = requests.get(SITABA_NEW_DISASTER_API, timeout=30)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("ERROR API SITABA:", e)
        return None


def ambil_list_bencana(data):
    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for key in ["data", "result", "results", "items", "records"]:
            if key in data and isinstance(data[key], list):
                return data[key]

        for value in data.values():
            if isinstance(value, list):
                return value

    return []


def normalisasi_bencana(item):
    return {
        "jenis": item.get("category") or item.get("child_category") or "Jenis bencana tidak tersedia",
        "sub_jenis": item.get("child_category") or "",
        "tanggal": item.get("report_date") or item.get("date_time") or "",
        "provinsi": item.get("province") or "",
        "kota": item.get("city") or "",
        "kecamatan": item.get("district") or "",
        "kelurahan": item.get("ward") or "",
        "lokasi": item.get("location") or "",
        "nama": item.get("name") or "",
        "status": item.get("status") or "",
        "current_status": item.get("current_status") or "",
    }


def deteksi_tahun(text):
    match = re.search(r"(20\d{2})", text)
    return match.group(1) if match else None


def deteksi_bulan(text):
    bulan_map = {
        "januari": "01",
        "februari": "02",
        "maret": "03",
        "april": "04",
        "mei": "05",
        "juni": "06",
        "juli": "07",
        "agustus": "08",
        "september": "09",
        "oktober": "10",
        "november": "11",
        "desember": "12",
    }

    for nama, angka in bulan_map.items():
        if nama in text:
            return angka, nama.capitalize()

    return None, None


def ambil_provinsi_dari_pertanyaan(pertanyaan):

    PROVINSI_MAP = {
        # Sumatera
        "aceh": "ACEH",
        "sumatera utara": "SUMATERA UTARA",
        "sumatera barat": "SUMATERA BARAT",
        "riau": "RIAU",
        "kepulauan riau": "KEPULAUAN RIAU",
        "jambi": "JAMBI",
        "sumatera selatan": "SUMATERA SELATAN",
        "kepulauan bangka belitung": "KEPULAUAN BANGKA BELITUNG",
        "bangka belitung": "KEPULAUAN BANGKA BELITUNG",
        "bengkulu": "BENGKULU",
        "lampung": "LAMPUNG",

        # Jawa
        "jakarta": "DKI JAKARTA",
        "dki jakarta": "DKI JAKARTA",

        "banten": "BANTEN",
        "jawa barat": "JAWA BARAT",
        "jabar": "JAWA BARAT",

        "jawa tengah": "JAWA TENGAH",
        "jateng": "JAWA TENGAH",

        "di yogyakarta": "DI YOGYAKARTA",
        "yogyakarta": "DI YOGYAKARTA",
        "jogja": "DI YOGYAKARTA",
        "jogya": "DI YOGYAKARTA",
        "diy": "DI YOGYAKARTA",

        "jawa timur": "JAWA TIMUR",
        "jatim": "JAWA TIMUR",

        # Bali & Nusa Tenggara
        "bali": "BALI",

        "nusa tenggara barat": "NUSA TENGGARA BARAT",
        "ntb": "NUSA TENGGARA BARAT",

        "nusa tenggara timur": "NUSA TENGGARA TIMUR",
        "ntt": "NUSA TENGGARA TIMUR",

        # Kalimantan
        "kalimantan barat": "KALIMANTAN BARAT",
        "kalbar": "KALIMANTAN BARAT",

        "kalimantan tengah": "KALIMANTAN TENGAH",
        "kalteng": "KALIMANTAN TENGAH",

        "kalimantan selatan": "KALIMANTAN SELATAN",
        "kalsel": "KALIMANTAN SELATAN",

        "kalimantan timur": "KALIMANTAN TIMUR",
        "kaltim": "KALIMANTAN TIMUR",

        "kalimantan utara": "KALIMANTAN UTARA",
        "kalut": "KALIMANTAN UTARA",

        # Sulawesi
        "sulawesi utara": "SULAWESI UTARA",
        "sulut": "SULAWESI UTARA",

        "gorontalo": "GORONTALO",

        "sulawesi tengah": "SULAWESI TENGAH",
        "sulteng": "SULAWESI TENGAH",

        "sulawesi barat": "SULAWESI BARAT",
        "sulbar": "SULAWESI BARAT",

        "sulawesi selatan": "SULAWESI SELATAN",
        "sulsel": "SULAWESI SELATAN",

        "sulawesi tenggara": "SULAWESI TENGGARA",
        "sultra": "SULAWESI TENGGARA",

        # Maluku
        "maluku": "MALUKU",
        "maluku utara": "MALUKU UTARA",
        "malut":"MALUKU UTARA",

        # Papua
        "papua": "PAPUA",
        "papua barat": "PAPUA BARAT",
        "pabar": "PAPUA BARAT",
        "papua selatan": "PAPUA SELATAN",
        "pasel": "PAPUA SELATAN",
        "papua tengah": "PAPUA TENGAH",
        "pateng": "PAPUA TENGAH",
        "papua pegunungan": "PAPUA PEGUNUNGAN",
        "papua barat daya": "PAPUA BARAT DAYA",
    }

    pertanyaan = pertanyaan.lower()

    for keyword, provinsi in PROVINSI_MAP.items():
        if keyword in pertanyaan:
            return provinsi

    return None

def filter_bencana(daftar, pertanyaan):
    tahun = deteksi_tahun(pertanyaan)
    bulan_angka, bulan_nama = deteksi_bulan(pertanyaan)
    provinsi_dicari = ambil_provinsi_dari_pertanyaan(pertanyaan)
    kota_dicari = ambil_kota_dari_pertanyaan(pertanyaan)

    hasil = []

    for item in daftar:
        data = normalisasi_bencana(item)
        tanggal = data["tanggal"]
        provinsi_data = (data.get("provinsi") or "").upper()
        kota_data = (data.get("kota") or "").upper()

        if provinsi_dicari and provinsi_data != provinsi_dicari:
            continue

        if kota_dicari and kota_data != kota_dicari:
            continue

        if tahun and tahun not in tanggal:
            continue

        if bulan_angka and f"-{bulan_angka}-" not in tanggal:
            continue

        if "longsor" in pertanyaan and "longsor" not in data["jenis"].lower() and "longsor" not in data["nama"].lower():
            continue

        if "banjir" in pertanyaan and "banjir" not in data["jenis"].lower() and "banjir" not in data["nama"].lower():
            continue

        hasil.append(data)

    return hasil, tahun, bulan_nama, provinsi_dicari, kota_dicari

def format_jawaban_bencana(data, pertanyaan):
    daftar = ambil_list_bencana(data)

    if not daftar:
        return "Maaf, data dari API SITABA belum tersedia atau format datanya belum terbaca."

    hasil, tahun, bulan_nama, provinsi_dicari, kota_dicari = filter_bencana(daftar, pertanyaan)

    if not hasil:
        keterangan = []

        if provinsi_dicari:
            keterangan.append(provinsi_dicari)

        if kota_dicari:
            keterangan.append(kota_dicari)

        if bulan_nama:
            keterangan.append(bulan_nama)

        if tahun:
            keterangan.append(tahun)

        if keterangan:
            return (
                f"Data bencana untuk {' '.join(keterangan)} tidak ditemukan pada API SITABA yang sedang digunakan.\n\n"
                "Catatan: SINTA tidak menampilkan data provinsi lain agar jawaban tidak menyesatkan."
            )

        hasil = [normalisasi_bencana(item) for item in daftar[:10]]

    counter_jenis = Counter([item["jenis"] for item in hasil])
    counter_provinsi = Counter([item["provinsi"] for item in hasil if item["provinsi"]])

    teks = "Berikut data bencana dari API SITABA:\n\n"
    teks += f"Total data terbaca: {len(hasil)} kejadian\n\n"

    teks += "Ringkasan jenis bencana:\n"
    for jenis, jumlah in counter_jenis.most_common():
        teks += f"- {jenis}: {jumlah} kejadian\n"

    if counter_provinsi:
        teks += "\nSebaran provinsi:\n"
        for provinsi, jumlah in counter_provinsi.most_common():
            teks += f"- {provinsi}: {jumlah} kejadian\n"

    teks += "\nDetail kejadian:\n"
    for i, item in enumerate(hasil[:10], start=1):
        teks += f"{i}. {item['jenis']}\n"
        teks += f"   Tanggal: {item['tanggal']}\n"
        teks += f"   Provinsi: {item['provinsi']}\n"
        teks += f"   Kab/Kota: {item['kota']}\n"
        teks += f"   Kecamatan: {item['kecamatan']}\n"
        teks += f"   Lokasi: {item['lokasi']}\n\n"

    teks += "Sumber: API SITABA Kementerian PU."
    return teks

def ambil_kota_dari_pertanyaan(pertanyaan, daftar):

    pertanyaan = pertanyaan.lower()

    kota_ditemukan = set()

    for item in daftar:

        kota = (item.get("city") or "").strip()

        if not kota:
            continue

        kota_lower = kota.lower()

        nama = (
            kota_lower
            .replace("kabupaten ", "")
            .replace("kab. ", "")
            .replace("kab ", "")
            .replace("kota ", "")
            .replace("kot.", "")
            .strip()
        )

        if kota_lower in pertanyaan or nama in pertanyaan:
            kota_ditemukan.add(kota.upper())

    return list(kota_ditemukan)
    
def filter_bencana(daftar, pertanyaan):
    tahun = deteksi_tahun(pertanyaan)
    bulan_angka, bulan_nama = deteksi_bulan(pertanyaan)
    provinsi_dicari = ambil_provinsi_dari_pertanyaan(pertanyaan)
    kota_dicari = ambil_kota_dari_pertanyaan(pertanyaan, daftar)

    hasil = []

    for item in daftar:
        data = normalisasi_bencana(item)
        tanggal = data["tanggal"]
        provinsi_data = (data.get("provinsi") or "").upper()
        kota_data = (data.get("kota") or "").upper()
        kabupaten_data = (data.get ("kabupaten")or "").upper()

        if provinsi_dicari and provinsi_data != provinsi_dicari:
            continue

        if kota_dicari and kota_data not in kota_dicari:
            continue

        if tahun and tahun not in tanggal:
            continue

        if bulan_angka and f"-{bulan_angka}-" not in tanggal:
            continue

        if "longsor" in pertanyaan and "longsor" not in data["jenis"].lower() and "longsor" not in data["nama"].lower():
            continue

        if "banjir" in pertanyaan and "banjir" not in data["jenis"].lower() and "banjir" not in data["nama"].lower():
            continue

        hasil.append(data)

    return hasil, tahun, bulan_nama, provinsi_dicari, kota_dicari

@app.get("/debug-sitaba")
def debug_sitaba():
    data = get_bencana_terkini()
    daftar = ambil_list_bencana(data)

    return {
        "jumlah_data": len(daftar),
        "contoh_data_pertama": daftar[0] if daftar else None
    }


@app.get("/cek-tahun")
def cek_tahun():
    data = get_bencana_terkini()
    daftar = ambil_list_bencana(data)

    tahun = {}

    for item in daftar:
        tanggal = item.get("report_date") or item.get("date_time") or ""
        if tanggal:
            th = tanggal[:4]
            tahun[th] = tahun.get(th, 0) + 1

    return tahun

def jawab_informasi_umum(pertanyaan):
    q = pertanyaan.lower()

    # ===== Tentang SITABA =====
    if "apa itu sitaba" in q:
        return (
            "SITABA (Sistem Informasi Tanggap Bencana) merupakan sistem informasi "
            "kebencanaan Kementerian Pekerjaan Umum yang menyediakan informasi "
            "kejadian bencana, penanganan, sumber daya, publikasi, regulasi, "
            "serta data pendukung penanggulangan bencana."
        )

    if (
        "menu sitaba" in q
        or "fitur sitaba" in q
        or "informasi kebencanaan" in q
        or "apa saja yang bisa dicari" in q
        or "apa yang bisa dicari" in q
    ):

        return """Melalui SITABA masyarakat dapat memperoleh informasi mengenai:

• Bencana terkini
• Statistik kejadian bencana
• Berita kebencanaan
• Penanganan bencana oleh Kementerian PU
• Infrastruktur terdampak
• Material/Bahan
• Peralatan
• Personel
• Publikasi
• Regulasi
• Mitigasi bencana
• Kesiapsiagaan bencana

Silakan ajukan pertanyaan terkait informasi tersebut."""
    return None

def cek_out_of_scope(pertanyaan):

    q = pertanyaan.lower()

    kata_out = [
    "presiden",
    "wakil presiden",
    "menteri",
    "gubernur",
    "wali kota",
    "walikota",
    "bupati",
    "pemilu",
    "politik",

    "prabowo",
    "prabowo subianto",
    "jokowi",
    "joko widodo",
    "gibran",
    "faisal baswedi",
    "anies",
    "ganjar",

    "sepak bola",
    "liga",
    "film",
    "drama",
    "lagu",
    "musik",
    "artis",
    "resep",
    "makanan",
    "cuaca",
    "bitcoin",
    "crypto",
    "saham",
    "chatgpt",
    "gemini",
    "google",
    "facebook",
    "instagram",
    "whatsapp",
    "namaorang",
    "negara"
]

    for kata in kata_out:
        if kata in q:
            return (
                "Maaf, pertanyaan tersebut berada di luar cakupan AI SINTA.\n\n"
                "AI SINTA hanya melayani informasi yang tersedia pada SITABA "
                "Kementerian Pekerjaan Umum, seperti informasi bencana, statistik, "
                "berita, sumber daya, publikasi, regulasi, mitigasi, dan kesiapsiagaan."
            )
    return None

def pertanyaan_sitaba(q):
    q = q.lower()

    keyword = [

        # SITABA
        "sitaba",
        "kebencanaan",
        "bencana",
        "banjir",
        "longsor",
        "gempa",
        "tsunami",
        "erupsi",
        "kekeringan",
        "cuaca ekstrem",

        # data
        "statistik",
        "kejadian",

        # berita
        "berita",

        # regulasi
        "regulasi",
        "publikasi",

        # sumber daya
        "personel",
        "alat",
        "bahan",
        "material",

        # mitigasi
        "mitigasi",
        "kesiapsiagaan",

        # kementerian
        "jalan", 
        "jembatan",
        "bendungan",
        "bendung",
        "infrastruktur",

        # PU
        "kementerian pu",
        "pekerjaan umum"
    ]
    return any(k in q for k in keyword)

def simpan_jawaban_terakhir(teks):
    global LAST_REPLY
    LAST_REPLY = teks

def buat_pdf(teks):
    filename = f"laporan_sinta_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(EXPORT_DIR, filename)

    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Laporan AI SINTA - SITABA")
    y -= 30

    c.setFont("Helvetica", 10)

    for line in teks.split("\n"):
        wrapped = textwrap.wrap(line, width=90) or [""]
        for wline in wrapped:
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 50

            c.drawString(50, y, wline)
            y -= 14

    c.save()
    return filepath


def buat_jpg(teks):
    filename = f"laporan_sinta_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    filepath = os.path.join(EXPORT_DIR, filename)

    width = 1200
    padding = 50
    line_height = 28

    wrapped_lines = []
    for line in teks.split("\n"):
        wrapped_lines.extend(textwrap.wrap(line, width=80) or [""])

    height = padding * 2 + len(wrapped_lines) * line_height + 60

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    draw.text((padding, padding), "Laporan AI SINTA - SITABA", fill="black")
    y = padding + 50

    for line in wrapped_lines:
        draw.text((padding, y), line, fill="black")
        y += line_height

    img.save(filepath, "JPEG", quality=95)
    return filepath

@app.get("/export/pdf")
def export_pdf():
    if not LAST_REPLY:
        raise HTTPException(status_code=400, detail="Belum ada jawaban untuk diexport.")

    filepath = buat_pdf(LAST_REPLY)

    return FileResponse(
        filepath,
        media_type="application/pdf",
        filename=os.path.basename(filepath)
    )

@app.get("/export/jpg")
def export_jpg():
    if not LAST_REPLY:
        raise HTTPException(status_code=400, detail="Belum ada jawaban untuk diexport.")

    filepath = buat_jpg(LAST_REPLY)

    return FileResponse(
        filepath,
        media_type="image/jpeg",
        filename=os.path.basename(filepath)
    )

def simpan_jawaban(question, answer, source):
    global LAST_RESPONSE

    LAST_RESPONSE = {
        "question": question,
        "answer": answer,
        "source": source,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

@app.post("/chat")
def chat(data: ChatRequest):
    user_message = data.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Pesan tidak boleh kosong.")

    lower_message = user_message.lower()

    provinsi_target = None
    if (
        "jogya" in lower_message
        or "yogya" in lower_message
        or "yogyakarta" in lower_message
        or "jogja" in lower_message
    ):
     provinsi_target = "DI YOGYAKARTA"

    info = jawab_informasi_umum(lower_message)
    if info:
        simpan_jawaban_terakhir(info)
        return {"reply": info}

    out = cek_out_of_scope(lower_message)
    if out:
        simpan_jawaban_terakhir(out)
        return {"reply": out}

    if (
        "bencana" in lower_message
        or "statistik" in lower_message
        or "banjir" in lower_message
        or "longsor" in lower_message
        or "gempa" in lower_message
        or "ruas jalan" in lower_message
        or "jalan terdampak" in lower_message
        or "infrastruktur terdampak" in lower_message
    ):
        data_bencana = get_bencana_terkini()
        reply = format_jawaban_bencana(data_bencana, lower_message)
        simpan_jawaban_terakhir(reply)
        return {
             "reply": reply
        }

        data_bencana = get_bencana_terkini()
        return {
             "reply": format_bencana_terkini(data_bencana, provinsi_target)
        }
    
    prompt = f"""
Kamu adalah SINTA, AI Chatbot resmi untuk SITABA Kementerian Pekerjaan Umum.
SITABA adalah sistem informasi kebencanaan Kementerian PU.
Jawab singkat, jelas, profesional, dan jangan mengarang data spesifik.

Pertanyaan pengguna:
{user_message}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "top_p": 0.8
                }
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        reply = result.get("response", "").strip()

        if not reply:
            reply = "Maaf, SINTA belum menemukan jawaban yang sesuai."
            simpan_jawaban_terakhir(reply)
        return {"reply": reply}

    except requests.exceptions.ConnectionError:
        return {
            "reply": "Maaf, layanan AI lokal belum aktif. Pastikan Ollama sudah berjalan."
        }

    except requests.exceptions.Timeout:
        return {
            "reply": "Maaf, SINTA membutuhkan waktu terlalu lama untuk menjawab. Silakan coba lagi."
        }

    except Exception:
        return {
            "reply": "Maaf, terjadi kendala pada layanan SINTA. Silakan coba beberapa saat lagi."
        }        
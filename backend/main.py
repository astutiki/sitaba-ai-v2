from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import requests

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


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)


def get_bencana_terkini():
    try:
        res = requests.get(SITABA_NEW_DISASTER_API, timeout=20)
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


def format_bencana_terkini(data):
    daftar = ambil_list_bencana(data)

    if not daftar:
        return "Maaf, data bencana terkini dari SITABA belum tersedia atau format datanya belum terbaca."

    teks = "Berikut data bencana terkini dari SITABA:\n\n"

    for i, item in enumerate(daftar[:10], start=1):
        if not isinstance(item, dict):
            teks += f"{i}. {item}\n"
            continue

        jenis = (
            item.get("jenis_bencana")
            or item.get("jenis")
            or item.get("disaster_type")
            or item.get("nama_bencana")
            or item.get("title")
            or "Jenis bencana tidak tersedia"
        )

        lokasi = (
            item.get("lokasi")
            or item.get("kab_kota")
            or item.get("kabupaten")
            or item.get("kota")
            or item.get("district")
            or item.get("location")
            or "Lokasi tidak tersedia"
        )

        provinsi = item.get("provinsi") or item.get("province") or ""

        tanggal = (
            item.get("tanggal")
            or item.get("tanggal_kejadian")
            or item.get("created_at")
            or item.get("date")
            or ""
        )

        teks += f"{i}. {jenis}\n"
        teks += f"   Lokasi: {lokasi}"
        if provinsi:
            teks += f", {provinsi}"
        teks += "\n"

        if tanggal:
            teks += f"   Tanggal: {tanggal}\n"

        teks += "\n"

    teks += "Sumber: SITABA Kementerian PU."
    return teks


@app.post("/chat")
def chat(data: ChatRequest):
    user_message = data.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Pesan tidak boleh kosong.")

    lower_message = user_message.lower()

    if (
        "bencana hari ini" in lower_message
        or "bencana terkini" in lower_message
        or "kejadian bencana" in lower_message
        or "bencana terbaru" in lower_message
    ):
        data_bencana = get_bencana_terkini()
        return {
            "reply": format_bencana_terkini(data_bencana)
        }

    prompt = f"""
Kamu adalah SINTA, AI Chatbot resmi untuk SITABA Kementerian Pekerjaan Umum.

KONTEKS WAJIB:
SITABA yang dimaksud adalah situs https://sitaba.pu.go.id/.

SITABA adalah sistem informasi kebencanaan Kementerian PU yang memuat:
- Berita bencana
- Statistik kejadian bencana
- Sumber daya: bahan, alat, dan personel
- Publikasi dan regulasi
- Informasi pra-bencana/mitigasi
- Informasi terkait penanganan bencana oleh Kementerian PU

ATURAN KETAT:
- Jangan pernah mengartikan SITABA sebagai sekolah, lembaga pendidikan, aplikasi lain, atau istilah lain.
- Jangan mengarang data angka, lokasi, tanggal, atau berita.
- Jika data spesifik belum tersedia, jawab: "Data tersebut perlu dicek melalui situs resmi SITABA di https://sitaba.pu.go.id."
- Fokus hanya pada SITABA Kementerian PU dan informasi kebencanaan.
- Jawab dalam Bahasa Indonesia yang singkat, jelas, dan profesional.

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
const express = require("express");
const { chatLogs } = require("../dataStore");

const router = express.Router();

const sitabaKnowledge = `
SITABA adalah Sistem Informasi Tanggap Bencana Kementerian PU.

informasi yang tersedia bersumber dari http://sitaba.pu.go.id

SITABA membantu masyarakat memperoleh informasi tentang:
- bencana terkini
- infrastruktur PU terdampak
- statistik kebencanaan
- sumber daya
- publikasi/regulasi
- mitigasi dan kesiapsiagaan
- berita dan informasi PU terkait bencana
`;

function sanitizeInput(text) {
  return String(text || "")
    .trim()
    .replace(/[<>]/g, "")
    .slice(0, 500);
}

function sanitizeOutput(text) {
  return String(text || "")
    .trim()
    .replace(/[<>]/g, "")
    .slice(0, 10000);
}

function buildPrompt(message) {
  return `
Kamu adalah SINTA, AI Chatbot resmi untuk SITABA Kementerian PU.

GUNAKAN KNOWLEDGE BERIKUT:
${sitabaKnowledge}

ATURAN JAWABAN:
1. Jawab topik SITABA, kebencanaan, infrastruktur PU, mitigasi, dan informasi layanan SITABA.
2. Untuk pertanyaan umum tentang kebencanaan, tetap bantu jawab secara edukatif.
3. Untuk data spesifik tanggal/lokasi/jumlah kejadian, jangan mengarang. Katakan perlu dicek melalui API/database SITABA.
4. Jangan menjawab topik di luar SITABA seperti paspor, visa, asmara, atau hiburan.
5. Jawab dalam Bahasa Indonesia yang jelas, natural, ramah, dan tidak terlalu kaku.

PERTANYAAN USER:
${message}
`;
}

router.post("/", async (req, res) => {
  const startTime = Date.now();

const message = sanitizeInput(req.body.message);
const sessionId = sanitizeInput(req.body.sessionId || "guest");

  if (!message) {
    return res.status(400).json({ error: "Pesan tidak valid" });
  }

  try {
    const response = await fetch(process.env.OLLAMA_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: process.env.OLLAMA_MODEL || "gemma3:4b",
        prompt: buildPrompt(message),
        stream: false,
        options: {
          temperature: 0.2,
          top_p: 0.9,
          num_ctx: 8192,
          num_predict: 2048
        }
      })
    });

    if (!response.ok) {
      throw new Error(`Ollama tidak merespon. Status: ${response.status}`);
    }

    const data = await response.json();
    console.log("==================================");
    console.log("OLLAMA RESPONSE:");
   console.log(data.response);
    console.log("==================================");

  const answer = sanitizeOutput(
  data.response || "Maaf, AI SITABA belum memberikan jawaban."
  );

    const responseTimeMs = Date.now() - startTime;

    chatLogs.push({
      id: Date.now(),
      sessionId,
      question: message,
      answer,
      responseTimeMs,
      status: "success",
      createdAt: new Date()
    });

    return res.json({
      answer,
      responseTimeMs
    });

  } catch (error) {
    console.error("======================================");
    console.error("OLLAMA ERROR:");
    console.error(error);
    console.error("Message:", error.message);
    console.error("OLLAMA_URL:", process.env.OLLAMA_URL);
    console.error("OLLAMA_MODEL:", process.env.OLLAMA_MODEL);
    console.error("======================================");

    const responseTimeMs = Date.now() - startTime;

    chatLogs.push({
      id: Date.now(),
      sessionId,
      question: message,
      answer: "Error koneksi ke Gemma/Ollama",
      responseTimeMs,
      status: "error",
      createdAt: new Date()
    });

    return res.status(500).json({
      error: "Maaf, koneksi ke AI SITABA belum aktif. Pastikan Ollama dan Gemma berjalan."
    });
  }
});

module.exports = router;
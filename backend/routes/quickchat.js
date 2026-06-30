const express = require("express");
const jwt = require("jsonwebtoken");

const router = express.Router();

function verifyToken(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: "Token tidak ada" });

  try {
    const token = authHeader.split(" ")[1];
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    return res.status(403).json({ error: "Token tidak valid" });
  }
}

let quickChats = [
  {
    id: 1,
    question: "Rekapitulasi infrastruktur terdampak bencana minggu ini",
    status: "Aktif"
  },
  {
    id: 2,
    question: "Daftar lokasi bencana dengan status penanganan kritis",
    status: "Aktif"
  },
  {
    id: 3,
    question: "Apa saja kriteria infrastruktur yang masuk kategori rusak berat?",
    status: "Aktif"
  }
];

function cleanQuestion(text) {
  return String(text || "").trim().replace(/[<>]/g, "");
}

router.get("/", verifyToken, (req, res) => {
  res.json(quickChats);
});

router.post("/", verifyToken, (req, res) => {
  const question = cleanQuestion(req.body.question);

  if (question.length < 10 || question.length > 200) {
    return res.status(400).json({ error: "Pertanyaan tidak valid" });
  }

  const item = {
    id: Date.now(),
    question,
    status: "Aktif"
  };

  quickChats.push(item);
  res.json(item);
});

router.put("/:id", verifyToken, (req, res) => {
  const id = Number(req.params.id);
  const question = cleanQuestion(req.body.question);

  if (question.length < 10 || question.length > 200) {
    return res.status(400).json({ error: "Pertanyaan tidak valid" });
  }

  const item = quickChats.find(q => q.id === id);
  if (!item) return res.status(404).json({ error: "Data tidak ditemukan" });

  item.question = question;
  res.json(item);
});

router.put("/:id/toggle", verifyToken, (req, res) => {
  const id = Number(req.params.id);
  const item = quickChats.find(q => q.id === id);

  if (!item) return res.status(404).json({ error: "Data tidak ditemukan" });

  item.status = item.status === "Aktif" ? "Non Aktif" : "Aktif";
  res.json(item);
});

router.delete("/:id", verifyToken, (req, res) => {
  const id = Number(req.params.id);
  quickChats = quickChats.filter(q => q.id !== id);

  res.json({ success: true });
});

module.exports = router;
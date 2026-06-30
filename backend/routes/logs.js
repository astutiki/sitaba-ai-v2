const express = require("express");

const router = express.Router();

router.get("/", (req, res) => {
    res.json([
        {
            id: 1,
            user: "Guest",
            question: "Apa itu SITABA?",
            answer: "SITABA adalah Sistem Informasi Tanggap Bencana.",
            time: "2026-06-26 08:30"
        }
    ]);
});

module.exports = router;
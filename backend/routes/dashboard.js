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

const { chatLogs } = require("../dataStore");

router.get("/", verifyToken, (req, res) => {
  const totalChat = chatLogs.length;
  const totalUser = new Set(chatLogs.map(log => log.sessionId)).size;

  const avgMs =
    totalChat === 0
      ? 0
      : chatLogs.reduce((sum, log) => sum + log.responseTimeMs, 0) / totalChat;

  res.json({
    totalUser,
    totalChat,
    avgResponse: totalChat === 0 ? "0s" : `${(avgMs / 1000).toFixed(2)}s`
  });
});

module.exports = router;
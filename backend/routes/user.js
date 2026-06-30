const express = require("express");
const jwt = require("jsonwebtoken");

const router = express.Router();

function verifyToken(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader) {
    return res.status(401).json({
      error: "Token tidak ada"
    });
  }

  try {
    const token = authHeader.split(" ")[1];
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    return res.status(403).json({
      error: "Token tidak valid"
    });
  }
}

router.get("/", verifyToken, (req, res) => {
  res.json([
    {
      id: 1,
      name: "Admin Pengguna",
      email: "admin@sitaba.go.id"
    },
    {
      id: 2,
      name: "User Lokal",
      email: "user@sitaba.go.id"
    }
  ]);
});

module.exports = router;
const express = require("express");
const jwt = require("jsonwebtoken");

const router = express.Router();

router.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username !== "adminsitaba" || password !== "admin123") {
    return res.status(401).json({ error: "Username atau password salah" });
  }

  const token = jwt.sign(
    { role: "admin", username },
    process.env.JWT_SECRET,
    { expiresIn: "2h" }
  );

  res.json({ token });
});

module.exports = router;
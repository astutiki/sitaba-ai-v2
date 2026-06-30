const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
require("dotenv").config();

const authRoutes = require("./routes/auth");
const dashboardRoutes = require("./routes/dashboard");
const quickChatRoutes = require("./routes/quickchat");
const userRoutes = require("./routes/user");
const logsRoutes = require("./routes/logs");
const chatRoutes = require("./routes/chat");

const app = express();

app.use(helmet());
app.use(express.json({ limit: "1mb" }));

app.use(cors({
  origin: [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
  ],
  credentials: true,
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"]
}));

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 60,
  message: {
    error: "Terlalu banyak request."
  }
});

app.use("/api", limiter);

app.use("/api/auth", authRoutes);
app.use("/api/dashboard", dashboardRoutes);
app.use("/api/quickchat", quickChatRoutes);
app.use("/api/users", userRoutes);
app.use("/api/logs", logsRoutes);
app.use("/api/chat", chatRoutes);

app.get("/", (req, res) => {
  res.json({
    status: "OK",
    message: "AI SITABA Backend Running"
  });
});

app.use((req, res) => {
  res.status(404).json({
    error: "Endpoint tidak ditemukan"
  });
});

app.use((err, req, res, next) => {
  console.error(err);

  res.status(500).json({
    error: "Internal Server Error"
  });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 AI SITABA Backend berjalan di http://localhost:${PORT}`);
});
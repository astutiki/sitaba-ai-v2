const API_CHAT_URL = "https://constable-krypton-sketch.ngrok-free.dev/chat";

const chatToggle = document.getElementById("chatToggle");
const prechatPanel = document.getElementById("prechatPanel");
const chatWidget = document.getElementById("chatWidget");
const prechatClose = document.getElementById("prechatClose");
const chatClose = document.getElementById("chatClose");

const startChatButton = document.getElementById("startChatButton");
const visitorName = document.getElementById("visitorName");
const visitorEmail = document.getElementById("visitorEmail");

const sendButton = document.getElementById("sendButton");
const userInput = document.getElementById("userInput");
const chatBody = document.getElementById("chatBody");
const suggestedQuestions = document.getElementById("suggestedQuestions");
const suggestedButtons = document.querySelectorAll(".suggested-questions button");

let currentVisitor = null;
let sessionId = createSessionId();

function createSessionId() {
  return "session_" + Date.now() + "_" + Math.random().toString(36).substring(2, 8);
}

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email);
}

function hideAllPanels() {
  prechatPanel.classList.add("hidden");
  chatWidget.classList.add("hidden");
}

function showPrechat() {
  chatWidget.classList.add("hidden");
  prechatPanel.classList.remove("hidden");
  visitorName.focus();
}

function showChat() {
  prechatPanel.classList.add("hidden");
  chatWidget.classList.remove("hidden");
  userInput.focus();
}

function hideSuggestedQuestions() {
  if (suggestedQuestions) {
    suggestedQuestions.style.display = "none";
  }
}

function addUserMessage(message) {
  const row = document.createElement("div");
  row.className = "user-row";

  const bubble = document.createElement("div");
  bubble.className = "user-message";
  bubble.innerText = safeText(message);

  row.appendChild(bubble);
  chatBody.appendChild(row);
  chatBody.scrollTop = chatBody.scrollHeight;
}

function addBotMessage(message) {
  const row = document.createElement("div");
  row.className = "bot-row";

  const icon = document.createElement("div");
  icon.className = "bot-icon";

  const img = document.createElement("img");
  img.src = "assets/sinta-1.png";
  img.alt = "Logo SINTA";

  icon.appendChild(img);

  const bubble = document.createElement("div");
  bubble.className = "bot-message";
  bubble.innerText = safeText(message);

  row.appendChild(icon);
  row.appendChild(bubble);

  chatBody.appendChild(row);
  chatBody.scrollTop = chatBody.scrollHeight;

  return bubble;
}

async function sendMessage(customMessage = null) {
  const message = safeText(customMessage || userInput.value.trim());

  if (!message) return;

  hideSuggestedQuestions();
  addUserMessage(message);
  userInput.value = "";

  const loadingBubble = addBotMessage("Sedang memproses...");

  try {
    const response = await fetch(API_CHAT_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true"
      },
      body: JSON.stringify({
        message: message,
        sessionId: sessionId,
        visitorName: currentVisitor?.nama || null,
        visitorEmail: currentVisitor?.email || null
      })
    });

    const data = await response.json();

    if (!response.ok) {
      loadingBubble.innerText = safeText(
        data.error || data.detail || "Terjadi kesalahan."
      );
      return;
    }

    loadingBubble.innerText = safeText(
      data.reply || "Maaf, jawaban belum tersedia."
    );

  } catch (error) {
    loadingBubble.innerText = "Maaf, koneksi ke AI SITABA belum aktif.";
  }
}

chatToggle.addEventListener("click", () => {
  if (currentVisitor) {
    showChat();
  } else {
    showPrechat();
  }
});

prechatClose.addEventListener("click", hideAllPanels);
chatClose.addEventListener("click", hideAllPanels);

startChatButton.addEventListener("click", () => {
  const nama = visitorName.value.trim();
  const email = visitorEmail.value.trim();

  if (!nama) {
    alert("Nama wajib diisi.");
    visitorName.focus();
    return;
  }

  if (!email) {
    alert("Email wajib diisi.");
    visitorEmail.focus();
    return;
  }

  if (!isValidEmail(email)) {
    alert("Format email tidak valid. Contoh: nama@email.com");
    visitorEmail.focus();
    return;
  }

  currentVisitor = {
    nama: nama,
    email: email
  };

  sessionId = createSessionId();

  showChat();
});

sendButton.addEventListener("click", () => {
  sendMessage();
});

userInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});

suggestedButtons.forEach((button) => {
  button.addEventListener("click", () => {
    sendMessage(button.dataset.question);
  });
});

window.addEventListener("DOMContentLoaded", () => {
  currentVisitor = null;
  hideAllPanels();
});
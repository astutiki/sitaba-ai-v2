const API_CHAT_URL = "https://constable-krypton-sketch.ngrok-free.dev/chat";

const chatToggle = document.getElementById("chatToggle");
const chatWidget = document.getElementById("chatWidget");
const sendButton = document.getElementById("sendButton");
const userInput = document.getElementById("userInput");
const chatBody = document.getElementById("chatBody");
const suggestedButtons = document.querySelectorAll(".suggested-questions button");

let sessionId = localStorage.getItem("sitaba_session_id");

if (!sessionId) {
  sessionId =
    "session_" +
    Date.now() +
    "_" +
    Math.random().toString(36).substring(2, 8);

  localStorage.setItem("sitaba_session_id", sessionId);
}

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

function sendMessage() {
  const input = document.getElementById("messageInput");
  const message = input.value.trim();

  if (!message) return;

  const suggestedQuestions = document.getElementById("suggestedQuestions");
  if (suggestedQuestions) {
    suggestedQuestions.style.display = "none";
  }

  addUserMessage(message);
  input.value = "";

  // lanjut fetch ke backend di sini
}

document.querySelectorAll(".suggested-questions button").forEach((button) => {
  button.addEventListener("click", () => {
    const input = document.getElementById("messageInput");
    input.value = button.dataset.question;

    const suggestedQuestions = document.getElementById("suggestedQuestions");
    if (suggestedQuestions) {
      suggestedQuestions.style.display = "none";
    }

    sendMessage();
  });
});

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
  img.src = "/assets/sinta-1.png";
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

  addUserMessage(message);
  userInput.value = "";

  const loadingBubble = addBotMessage("Sedang memproses...");

  try {
    const response = await fetch(API_CHAT_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: message,
        sessionId: sessionId
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
    loadingBubble.innerText =
      "Maaf, koneksi ke AI SITABA belum aktif.";
  }
}

chatToggle.addEventListener("click", () => {
  chatWidget.classList.toggle("hidden");
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
    const question = button.dataset.question;
    sendMessage(question);
  });
});
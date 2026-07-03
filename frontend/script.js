const API_CHAT_URL = "https://constable-krypton-sketch.ngrok-free.dev/chat";

const chatToggle = document.getElementById("chatToggle");
const chatWidget = document.getElementById("chatWidget");
const sendButton = document.getElementById("sendButton");
const userInput = document.getElementById("userInput");
const chatBody = document.getElementById("chatBody");
const suggestedQuestions = document.getElementById("suggestedQuestions");
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
    visitorName: visitor.nama || null,
    visitorEmail: visitor.email || null
  })

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

    const visitor = JSON.parse(localStorage.getItem("sitaba_visitor") || "{}");

    if(visitor){

        chatWidget.classList.remove("hidden");

    }else{

        document
        .getElementById("prechatOverlay")
        .classList.remove("hidden");

    }

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

document
.getElementById("prechatClose")
.addEventListener("click",()=>{

    document
    .getElementById("prechatOverlay")
    .classList.add("hidden");

});

document
.getElementById("startChatButton")
.addEventListener("click",()=>{

    const nama=document
    .getElementById("visitorName")
    .value.trim();

    const email=document
    .getElementById("visitorEmail")
    .value.trim();

    if(!nama){

        alert("Nama wajib diisi.");

        return;
    }

    if(!email){

        alert("Email wajib diisi.");

        return;
    }

    localStorage.setItem(
        "sitaba_visitor",
        JSON.stringify({
            nama,
            email
        })
    );

    document
    .getElementById("prechatOverlay")
    .classList.add("hidden");

    chatWidget.classList.remove("hidden");
});

window.addEventListener("DOMContentLoaded", () => {
  const visitor = localStorage.getItem("sitaba_visitor");

  if (!visitor) {
    chatWidget.classList.add("hidden");
    document.getElementById("prechatOverlay").classList.add("hidden");
  }
});
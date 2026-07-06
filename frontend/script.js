console.log("SITABA-AI");

const API_BASE_URL = "https://wildfowl-extras-comma.ngrok-free.dev";
const API_CHAT_URL = API_BASE_URL + "/chat/";

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
let lastBotReply = "";
let lastUserQuestion = "";

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

function saveVisitorToLocal(nama, email) {
  const visitors = JSON.parse(localStorage.getItem("sitaba_visitors") || "[]");

  visitors.push({
    nama: nama,
    email: email,
    waktu: new Date().toISOString(),
    sessionId: sessionId
  });

  localStorage.setItem("sitaba_visitors", JSON.stringify(visitors));
}

async function saveVisitorToBackend(nama, email) {
  try {
    const response = await fetch(API_BASE_URL + "/visitors/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true"
      },
      body: JSON.stringify({
        name: nama,
        email: email
      })
    });

    if (!response.ok) {
      console.error("Gagal menyimpan visitor:", response.status);
      return null;
    }

    return await response.json();
  } catch (error) {
    console.error("Gagal menyimpan visitor ke backend:", error);
    return null;
  }
}

function saveChatToLocal(question, answer, responseTime) {
  const chats = JSON.parse(localStorage.getItem("sitaba_chat_history") || "[]");

  chats.push({
    nama: currentVisitor?.nama || "-",
    email: currentVisitor?.email || "-",
    question: question,
    answer: answer || "",
    waktu: new Date().toISOString(),
    time: new Date().toLocaleTimeString("id-ID", {
      hour: "2-digit",
      minute: "2-digit"
    }),
    responseTime: responseTime,
    sessionId: sessionId
  });

  localStorage.setItem("sitaba_chat_history", JSON.stringify(chats));
}

async function saveChatToBackend(question, answer, responseTime) {
  try {
    const response = await fetch(API_BASE_URL + "/dashboard/chats/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true"
      },
      body: JSON.stringify({
        name: currentVisitor?.nama || "-",
        email: currentVisitor?.email || "-",
        question: question,
        answer: answer || "",
        responseTime: responseTime,
        sessionId: sessionId
      })
    });

    if (!response.ok) {
      console.error("Gagal menyimpan chat:", response.status);
      return null;
    }

    return await response.json();
  } catch (error) {
    console.error("Gagal menyimpan chat ke backend:", error);
    return null;
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

function addExportButtons(bubble, answer) {
  lastBotReply = answer;

  const exportDiv = document.createElement("div");
  exportDiv.className = "export-buttons";

  const formats = [
    { label: "📄 PDF", format: "pdf" },
    { label: "📝 Word", format: "docx" },
    { label: "📊 Excel", format: "xlsx" },
    { label: "📋 CSV", format: "csv" }
  ];

  formats.forEach((item) => {
    const button = document.createElement("button");
    button.type = "button";
    button.innerText = item.label;

    button.addEventListener("click", () => {
      downloadFile(item.format);
    });

    exportDiv.appendChild(button);
  });

  bubble.appendChild(exportDiv);
}

async function downloadFile(format) {
  try {
    const response = await fetch(API_BASE_URL + "/export/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true"
      },
      body: JSON.stringify({
        question: lastUserQuestion,
        answer: lastBotReply,
        format: format
      })
    });

    const data = await response.json();

    if (!data.success) {
      alert("Gagal membuat file.");
      return;
    }

    window.open(API_BASE_URL + data.download, "_blank");
  } catch (error) {
    console.error("Gagal download file:", error);
    alert("Gagal download file.");
  }
}

async function sendMessage(customMessage = null) {
  const message = safeText(customMessage || userInput.value.trim());

  if (!message) return;

  hideSuggestedQuestions();
  addUserMessage(message);
  userInput.value = "";

  const loadingBubble = addBotMessage("Sedang memproses...");
  const startTime = performance.now();

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
    const endTime = performance.now();
    const responseTime = Math.round(endTime - startTime);

    if (!response.ok) {
      const errorMessage = data.error || data.detail || "Terjadi kesalahan.";
      loadingBubble.innerText = safeText(errorMessage);
      saveChatToLocal(message, errorMessage, responseTime);
      saveChatToBackend(message, errorMessage, responseTime);
      return;
    }

    const answer = data.reply || "Maaf, jawaban belum tersedia.";
    loadingBubble.innerText = safeText(answer);

    lastUserQuestion = message;
    lastBotReply = answer;

    addExportButtons(loadingBubble, answer);

    saveChatToLocal(message, answer, responseTime);
    saveChatToBackend(message, answer, responseTime);

  } catch (error) {
    console.error("ERROR CHAT:", error);

    const errorMessage = "Network Error: " + error.message;
    loadingBubble.innerText = errorMessage;

    saveChatToLocal(message, errorMessage, 0);
    saveChatToBackend(message, errorMessage, 0);
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

  saveVisitorToLocal(nama, email);
  showChat();

  saveVisitorToBackend(nama, email);
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
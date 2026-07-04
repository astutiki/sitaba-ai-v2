const LOGIN_KEY = "sitaba_admin_login";

const loginPage = document.getElementById("loginPage");
const dashboardPage = document.getElementById("dashboardPage");
const loginButton = document.getElementById("loginButton");
const logoutButton = document.getElementById("logoutButton");

const adminUser = document.getElementById("adminUser");
const adminPass = document.getElementById("adminPass");

const recentList = document.getElementById("recentList");
const tableArea = document.getElementById("tableArea");
const searchInput = document.getElementById("searchInput");
const addQuickButton = document.getElementById("addQuickButton");

const modal = document.getElementById("modal");
const closeModal = document.getElementById("closeModal");
const saveQuickButton = document.getElementById("saveQuickButton");
const questionInput = document.getElementById("questionInput");
const statusInput = document.getElementById("statusInput");

const tableTitle = document.getElementById("tableTitle");
const tableDesc = document.getElementById("tableDesc");

let currentPage = "quick";

let quickChats = [
  { question: "Sebutkan tahun kejadian banjir di Bali?", status: "Aktif" },
  { question: "Longsor di Jawa Timur terjadi kapan?", status: "Aktif" },
  { question: "Informasi kebencanaan apa saja yang bisa dicari masyarakat melalui SITABA?", status: "Aktif" }
];

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

function getVisitors() {
  return JSON.parse(localStorage.getItem("sitaba_visitors") || "[]");
}

function getChats() {
  return JSON.parse(localStorage.getItem("sitaba_chat_history") || "[]");
}

function getLast7Days() {
  const bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"];
  const result = [];

  for (let i = 6; i >= 0; i--) {
    const d = new Date();
    d.setDate(d.getDate() - i);

    result.push({
      label: `${d.getDate()} ${bulan[d.getMonth()]}`,
      date: d.toLocaleDateString("id-ID")
    });
  }

  return result;
}

function loadDashboardStats() {
  const visitors = getVisitors();
  const chats = getChats();

  document.getElementById("totalUsers").innerText = visitors.length;
  document.getElementById("totalUsersDesc").innerText =
    visitors.length > 0 ? `${visitors.length} pengguna telah mengisi form chatbot` : "Belum ada pengunjung";

  document.getElementById("totalChats").innerText = chats.length;
  document.getElementById("totalChatsDesc").innerText =
    chats.length > 0 ? "Total seluruh percakapan chatbot" : "Belum ada percakapan";

  const responseTimes = chats
    .map(chat => Number(chat.responseTime))
    .filter(time => !isNaN(time) && time > 0);

  const avgResponse = responseTimes.length
    ? responseTimes.reduce((a, b) => a + b, 0) / responseTimes.length
    : 0;

  document.getElementById("avgResponse").innerText =
    avgResponse > 0 ? `${avgResponse.toFixed(2)} ms` : "0 ms";

  document.getElementById("avgResponseDesc").innerText =
    responseTimes.length > 0 ? "Rata-rata waktu respon AI" : "Menunggu data";

  const today = new Date().toLocaleDateString("id-ID");
  const todayChats = chats.filter(chat => {
    if (!chat.waktu) return false;
    return new Date(chat.waktu).toLocaleDateString("id-ID") === today;
  });

  document.getElementById("todayChats").innerText = todayChats.length;
  document.getElementById("todayChatsDesc").innerText =
    todayChats.length > 0 ? `${todayChats.length} percakapan hari ini` : "Belum ada percakapan hari ini";
}

function renderRecent() {
  const chats = getChats().slice(-4).reverse();

  if (!recentList) return;

  if (!chats.length) {
    recentList.innerHTML = `<div class="empty">Belum ada percakapan terbaru.</div>`;
    return;
  }

  recentList.innerHTML = chats.map(item => `
    <div class="recent-item">
      <time>${safeText(item.time || "-")}</time>
      <div>
        <p>${safeText(item.question || "-")}</p>
        <small>${safeText(item.nama || item.name || item.email || "-")}</small>
      </div>
      <span>Selesai</span>
    </div>
  `).join("");
}

function renderChart() {
  const last7Days = getLast7Days();
  const chats = getChats();

  const values = last7Days.map(day => {
    return chats.filter(chat => {
      if (!chat.waktu) return false;
      return new Date(chat.waktu).toLocaleDateString("id-ID") === day.date;
    }).length;
  });

  const max = Math.max(...values, 1);
  const width = 700;
  const height = 210;

  const points = values.map((value, index) => {
    const x = (width / (values.length - 1)) * index;
    const y = height - (value / max) * height + 20;
    return `${x},${y}`;
  });

  const chartLine = document.getElementById("chartLine");
  const chartArea = document.getElementById("chartArea");
  const chartDots = document.getElementById("chartDots");

  if (chartLine) chartLine.setAttribute("points", points.join(" "));
  if (chartArea) chartArea.setAttribute("points", `0,230 ${points.join(" ")} 700,230`);

  if (chartDots) {
    chartDots.innerHTML = points.map((point, index) => {
      const [x, y] = point.split(",");
      return `<circle cx="${x}" cy="${y}" r="6" fill="#2478ff" stroke="white" stroke-width="3">
        <title>${last7Days[index].label}: ${values[index]} chat</title>
      </circle>`;
    }).join("");
  }

  const labelBox = document.querySelector(".chart-labels");
  if (labelBox) {
    labelBox.innerHTML = last7Days.map(day => `<span>${day.label}</span>`).join("");
  }
}

function renderQuickChat() {
  currentPage = "quick";

  tableTitle.innerText = "Quick Chat";
  tableDesc.innerText = "Kelola pertanyaan cepat yang tampil di chatbot SINTA.";

  const keyword = searchInput.value.toLowerCase();

  const data = quickChats.filter(item =>
    item.question.toLowerCase().includes(keyword)
  );

  tableArea.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>No</th>
          <th>Question</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        ${
          data.length
            ? data.map((item, index) => `
              <tr>
                <td>${index + 1}</td>
                <td>${safeText(item.question)}</td>
                <td><span class="badge">${safeText(item.status)}</span></td>
                <td>
                  <button class="action" onclick="toggleStatus(${index})">✎</button>
                  <button class="action" onclick="deleteQuestion(${index})">⌫</button>
                </td>
              </tr>
            `).join("")
            : `<tr><td colspan="4" class="empty">Data tidak ditemukan.</td></tr>`
        }
      </tbody>
    </table>
  `;
}

function renderUsers() {
  currentPage = "users";

  const visitors = getVisitors();

  tableTitle.innerText = "User Pengunjung";
  tableDesc.innerText = "Daftar pengguna yang mengisi form chatbot SINTA.";

  tableArea.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>No</th>
          <th>Nama</th>
          <th>Email</th>
          <th>Waktu Login</th>
        </tr>
      </thead>
      <tbody>
        ${
          visitors.length
            ? visitors.map((item, index) => `
              <tr>
                <td>${index + 1}</td>
                <td>${safeText(item.nama || item.name || "-")}</td>
                <td>${safeText(item.email || "-")}</td>
                <td>${safeText(item.waktu || "-")}</td>
              </tr>
            `).join("")
            : `<tr><td colspan="4" class="empty">Belum ada pengunjung chatbot.</td></tr>`
        }
      </tbody>
    </table>
  `;
}

function setPage(page) {
  document.querySelectorAll(".nav-item").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.page === page);
  });

  if (page === "users") {
    renderUsers();
  } else {
    renderQuickChat();
  }
}

function toggleStatus(index) {
  quickChats[index].status = quickChats[index].status === "Aktif" ? "Nonaktif" : "Aktif";
  renderQuickChat();
}

function deleteQuestion(index) {
  quickChats.splice(index, 1);
  renderQuickChat();
}

function updateClock() {
  const now = new Date();

  const tanggal = now.toLocaleDateString("id-ID", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric"
  });

  const jam = now.toLocaleTimeString("id-ID");

  const el = document.getElementById("currentDateTime");
  if (el) {
    el.innerHTML = `${tanggal}<br><small>${jam} WIB</small>`;
  }
}

function showDashboard() {
  loginPage.classList.add("hidden");
  dashboardPage.classList.remove("hidden");

  loadDashboardStats();
  renderRecent();
  renderChart();
  renderQuickChat();
}

loginButton.addEventListener("click", () => {
  const user = adminUser.value.trim();
  const pass = adminPass.value.trim();

  if (user !== "admin" || pass !== "admin123") {
    alert("Username atau password salah.");
    return;
  }

  localStorage.setItem(LOGIN_KEY, "true");
  showDashboard();
});

logoutButton.addEventListener("click", () => {
  localStorage.removeItem(LOGIN_KEY);
  dashboardPage.classList.add("hidden");
  loginPage.classList.remove("hidden");
});

document.querySelectorAll(".nav-item").forEach(btn => {
  btn.addEventListener("click", () => setPage(btn.dataset.page));
});

searchInput.addEventListener("input", () => {
  if (currentPage === "users") {
    renderUsers();
  } else {
    renderQuickChat();
  }
});

addQuickButton.addEventListener("click", () => {
  modal.classList.remove("hidden");
});

closeModal.addEventListener("click", () => {
  modal.classList.add("hidden");
});

saveQuickButton.addEventListener("click", () => {
  const question = questionInput.value.trim();

  if (!question) {
    alert("Pertanyaan wajib diisi.");
    return;
  }

  quickChats.push({
    question,
    status: statusInput.value
  });

  questionInput.value = "";
  modal.classList.add("hidden");
  renderQuickChat();
});

window.addEventListener("DOMContentLoaded", () => {
  updateClock();
  setInterval(updateClock, 1000);

  if (localStorage.getItem(LOGIN_KEY) === "true") {
    showDashboard();
  } else {
    loginPage.classList.remove("hidden");
    dashboardPage.classList.add("hidden");
  }
});
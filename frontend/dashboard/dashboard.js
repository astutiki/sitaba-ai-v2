const LOGIN_KEY = "sitaba_admin_login";
const QUICK_CHAT_KEY = "sitaba_quick_chats";
const API_BASE_URL = "https://skimmed-lilly-roving.ngrok-free.dev";

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

let currentPage = "dashboard";

let quickChats = JSON.parse(localStorage.getItem(QUICK_CHAT_KEY) || "null") || [
  { question: "Sebutkan tahun kejadian banjir di Bali?", status: "Aktif" },
  { question: "Longsor di Jawa Timur terjadi kapan?", status: "Aktif" },
  { question: "Informasi kebencanaan apa saja yang bisa dicari masyarakat melalui SITABA?", status: "Aktif" }
];

function saveQuickChats() {
  localStorage.setItem(QUICK_CHAT_KEY, JSON.stringify(quickChats));
}

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

function formatDateTime(value) {
  if (!value) return "-";
  const d = new Date(value);
  if (isNaN(d.getTime())) return safeText(value);

  return d.toLocaleString("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function normalizeEmail(email) {
  return String(email || "").toLowerCase().trim();
}

function getUniqueUserCount(visitors) {
  const emails = new Set();

  visitors.forEach((item) => {
    const email = normalizeEmail(item.email);
    if (email) emails.add(email);
  });

  return emails.size;
}

async function getVisitors() {
  try {
    const response = await fetch(API_BASE_URL + "/visitors/", {
      headers: { "ngrok-skip-browser-warning": "true" }
    });

    if (!response.ok) {
      return JSON.parse(localStorage.getItem("sitaba_visitors") || "[]");
    }

    const result = await response.json();

    if (Array.isArray(result.data)) {
      return result.data;
    }

    return [];
  } catch (error) {
    console.error("Gagal ambil visitors:", error);
    return JSON.parse(localStorage.getItem("sitaba_visitors") || "[]");
  }
}

async function getChats() {
  try {
    const response = await fetch(API_BASE_URL + "/dashboard/chats/", {
      headers: { "ngrok-skip-browser-warning": "true" }
    });

    if (!response.ok) {
      return JSON.parse(localStorage.getItem("sitaba_chat_history") || "[]");
    }

    const result = await response.json();

    if (Array.isArray(result.data)) {
      return result.data;
    }

    return [];
  } catch (error) {
    console.error("Gagal ambil chats:", error);
    return JSON.parse(localStorage.getItem("sitaba_chat_history") || "[]");
  }
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

async function loadDashboardStats() {
  const visitors = await getVisitors();
  const chats = await getChats();

  const totalLogin = visitors.length;
  const totalUserUnik = getUniqueUserCount(visitors);

  document.getElementById("totalUsers").innerText = totalUserUnik;
  document.getElementById("totalUsersDesc").innerText =
    totalLogin > 0
      ? `${totalUserUnik} user unik dari ${totalLogin} total login`
      : "Belum ada pengunjung";

  document.getElementById("totalChats").innerText = chats.length;
  document.getElementById("totalChatsDesc").innerText =
    chats.length > 0 ? "Total seluruh percakapan chatbot" : "Belum ada percakapan";

  const responseTimes = chats
    .map(chat => Number(chat.responseTime ?? chat.response_time))
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
    const waktu = chat.waktu || chat.created_at;
    if (!waktu) return false;
    return new Date(waktu).toLocaleDateString("id-ID") === today;
  });

  document.getElementById("todayChats").innerText = todayChats.length;
  document.getElementById("todayChatsDesc").innerText =
    todayChats.length > 0
      ? `${todayChats.length} percakapan hari ini`
      : "Belum ada percakapan hari ini";
}

async function renderRecent() {
  const chats = (await getChats()).slice(-4).reverse();

  if (!recentList) return;

  if (!chats.length) {
    recentList.innerHTML = `<div class="empty">Belum ada percakapan terbaru.</div>`;
    return;
  }

  recentList.innerHTML = chats.map(item => `
    <div class="recent-item">
      <time>${safeText(formatDateTime(item.waktu || item.created_at || item.time))}</time>
      <div>
        <p>${safeText(item.question || "-")}</p>
        <small>${safeText(item.name || item.nama || item.email || "-")}</small>
      </div>
      <span>Selesai</span>
    </div>
  `).join("");
}

async function renderChart() {
  const last7Days = getLast7Days();
  const chats = await getChats();

  const values = last7Days.map(day => {
    return chats.filter(chat => {
      const waktu = chat.waktu || chat.created_at;
      if (!waktu) return false;
      return new Date(waktu).toLocaleDateString("id-ID") === day.date;
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
  addQuickButton.style.display = "inline-block";

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

async function renderUsers() {
  currentPage = "users";
  addQuickButton.style.display = "none";

  const visitors = await getVisitors();

  tableTitle.innerText = "User Pengunjung";
  tableDesc.innerText = "Daftar seluruh login chatbot SINTA. Email yang sama bisa muncul lebih dari sekali sebagai total login.";

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
                <td>${safeText(formatDateTime(item.waktu || item.created_at || "-"))}</td>
              </tr>
            `).join("")
            : `<tr><td colspan="4" class="empty">Belum ada pengunjung chatbot.</td></tr>`
        }
      </tbody>
    </table>
  `;
}

async function renderLogs() {
  currentPage = "logs";
  addQuickButton.style.display = "none";

  const chats = (await getChats()).slice().reverse();

  tableTitle.innerText = "Log Percakapan";
  tableDesc.innerText = "Daftar percakapan pengguna chatbot SINTA dari seluruh perangkat.";

  tableArea.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>No</th>
          <th>Waktu</th>
          <th>Nama / Email</th>
          <th>Pertanyaan</th>
          <th>Respon</th>
        </tr>
      </thead>
      <tbody>
        ${
          chats.length
            ? chats.map((item, index) => `
              <tr>
                <td>${index + 1}</td>
                <td>${safeText(formatDateTime(item.waktu || item.created_at || item.time))}</td>
                <td>${safeText(item.name || item.nama || item.email || "-")}</td>
                <td>${safeText(item.question || "-")}</td>
                <td>${safeText(item.responseTime || item.response_time || 0)} ms</td>
              </tr>
            `).join("")
            : `<tr><td colspan="5" class="empty">Belum ada log percakapan.</td></tr>`
        }
      </tbody>
    </table>
  `;
}

async function renderAllChats() {
  currentPage = "logs";
  await renderLogs();

  document.querySelectorAll(".nav-item").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.page === "logs");
  });
}

async function renderDashboardTable() {
  currentPage = "dashboard";
  addQuickButton.style.display = "none";

  tableTitle.innerText = "Ringkasan Dashboard";
  tableDesc.innerText = "Ringkasan data login dan percakapan lintas perangkat.";

  const visitors = await getVisitors();
  const chats = await getChats();
  const totalLogin = visitors.length;
  const totalUserUnik = getUniqueUserCount(visitors);

  tableArea.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>Metrik</th>
          <th>Nilai</th>
          <th>Keterangan</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>User Unik</td>
          <td>${totalUserUnik}</td>
          <td>Berdasarkan email unik</td>
        </tr>
        <tr>
          <td>Total Login</td>
          <td>${totalLogin}</td>
          <td>Satu email login 10x tetap dihitung 10 login</td>
        </tr>
        <tr>
          <td>Total Percakapan</td>
          <td>${chats.length}</td>
          <td>Gabungan seluruh perangkat dan browser</td>
        </tr>
      </tbody>
    </table>
  `;
}

async function setPage(page) {
  document.querySelectorAll(".nav-item").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.page === page);
  });

  if (page === "dashboard") {
    await renderDashboardTable();
  } else if (page === "users") {
    await renderUsers();
  } else if (page === "logs") {
    await renderLogs();
  } else {
    renderQuickChat();
  }

  await loadDashboardStats();
  await renderRecent();
  await renderChart();
}

function toggleStatus(index) {
  quickChats[index].status = quickChats[index].status === "Aktif" ? "Nonaktif" : "Aktif";
  saveQuickChats();
  renderQuickChat();
}

function deleteQuestion(index) {
  quickChats.splice(index, 1);
  saveQuickChats();
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

async function showDashboard() {
  loginPage.classList.add("hidden");
  dashboardPage.classList.remove("hidden");

  await loadDashboardStats();
  await renderRecent();
  await renderChart();
  await renderDashboardTable();
}

loginButton.addEventListener("click", async () => {
  const user = adminUser.value.trim();
  const pass = adminPass.value.trim();

  if (user !== "admin" || pass !== "admin123") {
    alert("Username atau password salah.");
    return;
  }

  localStorage.setItem(LOGIN_KEY, "true");
  await showDashboard();
});

logoutButton.addEventListener("click", () => {
  localStorage.removeItem(LOGIN_KEY);
  dashboardPage.classList.add("hidden");
  loginPage.classList.remove("hidden");
});

document.querySelectorAll(".nav-item").forEach(btn => {
  btn.addEventListener("click", () => setPage(btn.dataset.page));
});

const seeAllButton = document.querySelector(".recent-panel .panel-head button");
if (seeAllButton) {
  seeAllButton.addEventListener("click", () => {
    renderAllChats();
  });
}

searchInput.addEventListener("input", () => {
  if (currentPage === "users") {
    renderUsers();
  } else if (currentPage === "logs") {
    renderLogs();
  } else if (currentPage === "dashboard") {
    renderDashboardTable();
  } else {
    renderQuickChat();
  }
});

addQuickButton.addEventListener("click", () => {
  questionInput.value = "";
  statusInput.value = "Aktif";
  modal.classList.remove("hidden");
});

closeModal.addEventListener("click", () => {
  modal.classList.add("hidden");
});

modal.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.classList.add("hidden");
  }
});

saveQuickButton.addEventListener("click", () => {
  const question = questionInput.value.trim();

  if (!question) {
    alert("Pertanyaan wajib diisi.");
    questionInput.focus();
    return;
  }

  quickChats.push({
    question: question,
    status: statusInput.value
  });

  saveQuickChats();

  questionInput.value = "";
  statusInput.value = "Aktif";
  modal.classList.add("hidden");

  renderQuickChat();
});

window.addEventListener("DOMContentLoaded", async () => {
  updateClock();
  setInterval(updateClock, 1000);

  if (localStorage.getItem(LOGIN_KEY) === "true") {
    await showDashboard();
  } else {
    loginPage.classList.remove("hidden");
    dashboardPage.classList.add("hidden");
  }
});

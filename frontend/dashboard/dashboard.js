const LOGIN_KEY = "sitaba_admin_login";
const QUICK_CHAT_KEY = "sitaba_quick_chats";
const API_BASE_URL = "http://127.0.0.1:8000";

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


async function loadQuickChats() {
  try {
    const response = await fetch(API_BASE_URL + "/quick-chat/", {
      headers: { "ngrok-skip-browser-warning": "true" }
    });

    if (!response.ok) throw new Error(`HTTP ${response.status}`);

    const result = await response.json();
    if (Array.isArray(result.data)) {
      quickChats = result.data;
      saveQuickChats();
    }
  } catch (error) {
    console.warn("Backend Quick Chat belum dapat diakses, memakai data lokal:", error);
  }
}

async function createQuickChat(question, status) {
  const response = await fetch(API_BASE_URL + "/quick-chat/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "ngrok-skip-browser-warning": "true"
    },
    body: JSON.stringify({ question, status })
  });

  const result = await response.json();
  if (!response.ok) throw new Error(result.detail || `HTTP ${response.status}`);
  return result.data;
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
  function getLocalDateKey(value) {
  const date = value instanceof Date ? value : new Date(value);

  if (isNaN(date.getTime())) {
    return "";
  }

  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");

  return `${year}-${month}-${day}`;
}

function getMonthKey(value) {
  const date = value instanceof Date ? value : new Date(value);

  if (isNaN(date.getTime())) {
    return "";
  }

  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");

  return `${year}-${month}`;
}

function getYearKey(value) {
  const date = value instanceof Date ? value : new Date(value);

  if (isNaN(date.getTime())) {
    return "";
  }

  return String(date.getFullYear());
}

function getDailyPeriods(totalDays) {
  const bulan = [
    "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
    "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
  ];

  const periods = [];

  for (let i = totalDays - 1; i >= 0; i--) {
    const date = new Date();
    date.setHours(0, 0, 0, 0);
    date.setDate(date.getDate() - i);

    periods.push({
      key: getLocalDateKey(date),
      label: `${date.getDate()} ${bulan[date.getMonth()]}`,
      group: "day"
    });
  }

  return periods;
}

function getMonthlyPeriods(totalMonths) {
  const bulan = [
    "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
    "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
  ];

  const periods = [];

  for (let i = totalMonths - 1; i >= 0; i--) {
    const date = new Date();
    date.setDate(1);
    date.setHours(0, 0, 0, 0);
    date.setMonth(date.getMonth() - i);

    periods.push({
      key: getMonthKey(date),
      label: `${bulan[date.getMonth()]} ${date.getFullYear()}`,
      group: "month"
    });
  }

  return periods;
}

function getYearlyPeriods(chats) {
  const currentYear = new Date().getFullYear();

  const chatYears = chats
    .map(chat => {
      const waktu = chat.waktu || chat.created_at || chat.time;
      return waktu ? Number(getYearKey(waktu)) : null;
    })
    .filter(year => Number.isInteger(year));

  const earliestYear = chatYears.length
    ? Math.min(...chatYears)
    : currentYear - 4;

  const startYear = Math.min(earliestYear, currentYear - 4);
  const periods = [];

  for (let year = startYear; year <= currentYear; year++) {
    periods.push({
      key: String(year),
      label: String(year),
      group: "year"
    });
  }

  return periods;
}

function getChartPeriods(range, chats) {
  switch (range) {
    case "30":
    case "1m":
      return getDailyPeriods(30);

    case "3m":
      return getMonthlyPeriods(3);

    case "6m":
      return getMonthlyPeriods(6);

    case "12m":
      return getMonthlyPeriods(12);

    case "year":
      return getYearlyPeriods(chats);

    case "7":
    default:
      return getDailyPeriods(7);
  }
}

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
        <small>
           ${safeText(item.name || item.nama || "-")}
           ${item.email ? `(${safeText(item.email)})` : ""}
        </small>
      </div>
      <span>Selesai</span>
    </div>
  `).join("");
}

async function renderChart() {
 async function renderChart() {
  const rangeSelect = document.getElementById("rangeSelect");
  const selectedRange = rangeSelect?.value || "7";

  const chats = await getChats();
  const periods = getChartPeriods(selectedRange, chats);

  const values = periods.map(period => {
    return chats.filter(chat => {
      const waktu = chat.waktu || chat.created_at || chat.time;

      if (!waktu) {
        return false;
      }

      if (period.group === "month") {
        return getMonthKey(waktu) === period.key;
      }

      if (period.group === "year") {
        return getYearKey(waktu) === period.key;
      }

      return getLocalDateKey(waktu) === period.key;
    }).length;
  });

  const max = Math.max(...values, 1);
  const width = 700;
  const height = 210;
  const bottomY = 230;

  const totalPoints = values.length;

  const points = values.map((value, index) => {
    const x = totalPoints > 1
      ? (width / (totalPoints - 1)) * index
      : width / 2;

    const y = height - (value / max) * height + 20;

    return `${x},${y}`;
  });

  const chartLine = document.getElementById("chartLine");
  const chartArea = document.getElementById("chartArea");
  const chartDots = document.getElementById("chartDots");

  if (chartLine) {
    chartLine.setAttribute("points", points.join(" "));
  }

  if (chartArea) {
    if (points.length) {
      const firstX = points[0].split(",")[0];
      const lastX = points[points.length - 1].split(",")[0];

      chartArea.setAttribute(
        "points",
        `${firstX},${bottomY} ${points.join(" ")} ${lastX},${bottomY}`
      );
    } else {
      chartArea.setAttribute("points", "");
    }
  }

  if (chartDots) {
    chartDots.innerHTML = points.map((point, index) => {
      const [x, y] = point.split(",");

      return `
        <circle
          cx="${x}"
          cy="${y}"
          r="6"
          fill="#2478ff"
          stroke="white"
          stroke-width="3"
        >
          <title>
            ${periods[index].label}: ${values[index]} chat
          </title>
        </circle>
      `;
    }).join("");
  }

  const labelBox = document.querySelector(".chart-labels");

  if (labelBox) {
    let visiblePeriods = periods;

    // Supaya label 30 hari tidak bertumpuk terlalu rapat.
    if (selectedRange === "30" || selectedRange === "1m") {
      visiblePeriods = periods.map((period, index) => {
        const shouldShow =
          index === 0 ||
          index === periods.length - 1 ||
          index % 5 === 0;

        return {
          ...period,
          label: shouldShow ? period.label : ""
        };
      });
    }

    labelBox.innerHTML = visiblePeriods
      .map(period => `<span>${period.label}</span>`)
      .join("");
  }
}

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

  const data = quickChats
    .map((item, originalIndex) => ({ item, originalIndex }))
    .filter(({ item }) =>
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
            ? data.map(({ item, originalIndex }, index) => `
              <tr>
                <td>${index + 1}</td>
                <td>${safeText(item.question)}</td>
                <td><span class="badge">${safeText(item.status)}</span></td>
                <td>
                  <button class="action" onclick="toggleStatus(${originalIndex})">✎</button>
                  <button class="action" onclick="deleteQuestion(${originalIndex})">⌫</button>
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

async function toggleStatus(index) {
  const item = quickChats[index];
  if (!item) return;

  try {
    const response = await fetch(`${API_BASE_URL}/quick-chat/${item.id}/toggle`, {
      method: "PUT",
      headers: { "ngrok-skip-browser-warning": "true" }
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.detail || `HTTP ${response.status}`);
    quickChats[index] = result.data;
  } catch (error) {
    console.error("Gagal mengubah status Quick Chat:", error);
    alert("Gagal mengubah status Quick Chat.");
    return;
  }

  saveQuickChats();
  renderQuickChat();
}

async function deleteQuestion(index) {
  const item = quickChats[index];
  if (!item) return;

  try {
    const response = await fetch(`${API_BASE_URL}/quick-chat/${item.id}`, {
      method: "DELETE",
      headers: { "ngrok-skip-browser-warning": "true" }
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.detail || `HTTP ${response.status}`);
  } catch (error) {
    console.error("Gagal menghapus Quick Chat:", error);
    alert("Gagal menghapus Quick Chat.");
    return;
  }

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

saveQuickButton.addEventListener("click", async () => {
  const question = questionInput.value.trim();

  if (!question) {
    alert("Pertanyaan wajib diisi.");
    questionInput.focus();
    return;
  }

  saveQuickButton.disabled = true;

  try {
    const item = await createQuickChat(question, statusInput.value);
    quickChats.push(item);
    saveQuickChats();

    questionInput.value = "";
    statusInput.value = "Aktif";
    modal.classList.add("hidden");
    renderQuickChat();
  } catch (error) {
    console.error("Gagal menyimpan Quick Chat:", error);
    alert("Gagal menyimpan Quick Chat ke backend.");
  } finally {
    saveQuickButton.disabled = false;
  }
});

const rangeSelect = document.getElementById("rangeSelect");

if (rangeSelect) {
  rangeSelect.addEventListener("change", async () => {
    await renderChart();
  });
}

window.addEventListener("DOMContentLoaded", async () => {
  await loadQuickChats();
  updateClock();
  setInterval(updateClock, 1000);

  if (localStorage.getItem(LOGIN_KEY) === "true") {
    await showDashboard();
  } else {
    loginPage.classList.remove("hidden");
    dashboardPage.classList.add("hidden");
  }
});

document.addEventListener("DOMContentLoaded", function () {
    loadChatbotDashboardData();
});

function loadChatbotDashboardData() {
    const chatHistory = getLocalStorageArray("sitaba_chat_history");
    const visitors = getLocalStorageArray("sitaba_visitors");

    updateDashboardStatistics(chatHistory, visitors);
    updateRecentChats(chatHistory);
    updateQuickChart(chatHistory);
}

function getLocalStorageArray(key) {
    try {
        const storedData = localStorage.getItem(key);

        if (!storedData) {
            return [];
        }

        const parsedData = JSON.parse(storedData);

        return Array.isArray(parsedData) ? parsedData : [];
    } catch (error) {
        console.error(`Gagal membaca localStorage ${key}:`, error);
        return [];
    }
}

function updateDashboardStatistics(chatHistory, visitors) {
    const totalChatElement = document.getElementById("totalChats");
    const totalVisitorElement = document.getElementById("totalVisitors");
    const totalSessionElement = document.getElementById("totalSessions");
    const averageResponseElement = document.getElementById("averageResponseTime");

    if (totalChatElement) {
        totalChatElement.textContent = chatHistory.length;
    }

    if (totalVisitorElement) {
        totalVisitorElement.textContent = visitors.length;
    }

    if (totalSessionElement) {
        const sessionIds = chatHistory
            .map((chat) => chat.sessionId || chat.session_id)
            .filter(Boolean);

        const uniqueSessions = [...new Set(sessionIds)];

        totalSessionElement.textContent = uniqueSessions.length;
    }

    if (averageResponseElement) {
        const responseTimes = chatHistory
            .map((chat) => {
                const value =
                    chat.responseTime ??
                    chat.response_time ??
                    chat.duration ??
                    0;

                return Number(value);
            })
            .filter((value) => Number.isFinite(value) && value > 0);

        const average =
            responseTimes.length > 0
                ? responseTimes.reduce((total, value) => total + value, 0) /
                  responseTimes.length
                : 0;

        averageResponseElement.textContent =
            average > 0 ? `${average.toFixed(2)} detik` : "0 detik";
    }
}

function updateRecentChats(chatHistory) {
    const tableBody = document.getElementById("recentChatsBody");

    if (!tableBody) {
        return;
    }

    tableBody.innerHTML = "";

    const recentChats = [...chatHistory]
        .reverse()
        .slice(0, 10);

    if (recentChats.length === 0) {
        tableBody.innerHTML = `
            <tr>
                <td colspan="5" style="text-align:center;">
                    Belum ada riwayat percakapan.
                </td>
            </tr>
        `;
        return;
    }

    recentChats.forEach((chat, index) => {
        const visitorName =
            chat.visitorName ||
            chat.visitor_name ||
            chat.name ||
            "Pengunjung";

        const question =
            chat.question ||
            chat.message ||
            chat.userMessage ||
            "-";

        const answer =
            chat.answer ||
            chat.reply ||
            chat.botResponse ||
            "-";

        const dateValue =
            chat.created_at ||
            chat.createdAt ||
            chat.timestamp ||
            new Date().toISOString();

        const formattedDate = formatDashboardDate(dateValue);

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${escapeDashboardHtml(visitorName)}</td>
            <td>${escapeDashboardHtml(question)}</td>
            <td>${escapeDashboardHtml(answer)}</td>
            <td>${escapeDashboardHtml(formattedDate)}</td>
        `;

        tableBody.appendChild(row);
    });
}

function updateQuickChart(chatHistory) {
    const chartImage = document.getElementById("quickChartImage");

    if (!chartImage) {
        return;
    }

    const groupedChats = groupChatsByDate(chatHistory);

    const labels = Object.keys(groupedChats);
    const values = Object.values(groupedChats);

    if (labels.length === 0) {
        chartImage.removeAttribute("src");
        chartImage.alt = "Belum ada data percakapan";
        return;
    }

    const chartConfig = {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Jumlah Percakapan",
                    data: values,
                    fill: false,
                    borderWidth: 3,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: "Aktivitas Percakapan SITABA-AI"
                },
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    };

    chartImage.src =
        "https://quickchart.io/chart?c=" +
        encodeURIComponent(JSON.stringify(chartConfig));
}

function groupChatsByDate(chatHistory) {
    const groupedData = {};

    chatHistory.forEach((chat) => {
        const dateValue =
            chat.created_at ||
            chat.createdAt ||
            chat.timestamp;

        if (!dateValue) {
            return;
        }

        const date = new Date(dateValue);

        if (Number.isNaN(date.getTime())) {
            return;
        }

        const label = date.toLocaleDateString("id-ID", {
            day: "2-digit",
            month: "short"
        });

        groupedData[label] = (groupedData[label] || 0) + 1;
    });

    return groupedData;
}

function formatDashboardDate(dateValue) {
    const date = new Date(dateValue);

    if (Number.isNaN(date.getTime())) {
        return "-";
    }

    return date.toLocaleString("id-ID", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });
}

function escapeDashboardHtml(value) {
    const element = document.createElement("div");
    element.textContent = String(value ?? "");
    return element.innerHTML;
}

const defaultQuickChats = [
  {
    id: 1,
    label: "Tahun kejadian banjir di Bali?",
    question: "Sebutkan tahun kejadian banjir di Bali.",
    active: false
  },
  {
    id: 2,
    label: "Longsor di Jawa Timur terjadi kapan?",
    question: "Informasi longsor di Jawa Timur",
    active: false
  },
  {
    id: 3,
    label: "Informasi Kebencanaan",
    question:
      "Informasi kebencanaan apa saja yang bisa dicari masyarakat melalui SITABA?",
    active: false
  }
];

localStorage.setItem(
  "sitaba_quick_chats",
  JSON.stringify(defaultQuickChats)
);

const LOGS_PER_PAGE = 25;

let currentLogsPage = 1;
let allConversationLogs = [];
let filteredConversationLogs = [];
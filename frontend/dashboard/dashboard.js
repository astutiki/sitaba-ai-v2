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

const pageTitle = document.getElementById("pageTitle");
const pageSubtitle = document.getElementById("pageSubtitle");
const tableTitle = document.getElementById("tableTitle");
const tableDesc = document.getElementById("tableDesc");

const LOGIN_KEY = "sitaba_admin_login";

let currentPage = "dashboard";

let quickChats = [
  { question: "Sebutkan tahun kejadian banjir di Bali?", status: "Aktif" },
  { question: "Longsor di Jawa Timur terjadi kapan?", status: "Aktif" },
  { question: "Informasi kebencanaan apa saja yang bisa dicari masyarakat melalui SITABA?", status: "Aktif" }
];

let recentChats = [
  { time: "10:24", name: "Anasta", question: "Sebutkan tahun kejadian banjir di Bali?" },
  { time: "10:21", name: "Budi", question: "Longsor di Jawa Timur terjadi kapan?" },
  { time: "10:18", name: "Citra", question: "Informasi kebencanaan di Jakarta" },
  { time: "10:15", name: "Dewi", question: "Cara melaporkan bencana di SITABA?" }
];

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

function showDashboard() {
  loginPage.classList.add("hidden");
  dashboardPage.classList.remove("hidden");
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

function renderRecent() {
  recentList.innerHTML = recentChats.map(item => `
    <div class="recent-item">
      <time>${safeText(item.time)}</time>
      <div>
        <p>${safeText(item.question)}</p>
        <small>${safeText(item.name)}</small>
      </div>
      <span>Selesai</span>
    </div>
  `).join("");
}

function renderChart() {
  const values = [180, 245, 285, 160, 302, 175, 268];
  const max = 360;
  const width = 700;
  const height = 210;

  const points = values.map((value, index) => {
    const x = (width / (values.length - 1)) * index;
    const y = height - (value / max) * height + 20;
    return `${x},${y}`;
  });

  document.getElementById("chartLine").setAttribute("points", points.join(" "));
  document.getElementById("chartArea").setAttribute("points", `0,230 ${points.join(" ")} 700,230`);

  const dots = document.getElementById("chartDots");
  dots.innerHTML = points.map(point => {
    const [x, y] = point.split(",");
    return `<circle cx="${x}" cy="${y}" r="6" fill="#2478ff" stroke="white" stroke-width="3"></circle>`;
  }).join("");
}

function renderQuickChat() {
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
  tableArea.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>No</th>
          <th>Nama</th>
          <th>Email</th>
          <th>Total Chat</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>Anasta</td><td>anasta@email.com</td><td>3</td></tr>
        <tr><td>2</td><td>Budi</td><td>budi@email.com</td><td>2</td></tr>
      </tbody>
    </table>
  `;
}

function setPage(page) {
  currentPage = page;

  document.querySelectorAll(".nav-item").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.page === page);
  });

  if (page === "users") {
    tableTitle.innerText = "User Pengunjung";
    tableDesc.innerText = "Daftar pengguna yang mengakses chatbot SINTA.";
    renderUsers();
  } else {
    tableTitle.innerText = "Quick Chat";
    tableDesc.innerText = "Kelola pertanyaan cepat yang tampil di chatbot SINTA.";
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

document.querySelectorAll(".nav-item").forEach(btn => {
  btn.addEventListener("click", () => setPage(btn.dataset.page));
});

searchInput.addEventListener("input", () => {
  if (currentPage !== "users") renderQuickChat();
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

    // cek session login
    if(localStorage.getItem(LOGIN_KEY) === "true"){
        showDashboard();
    }else{
        loginPage.classList.remove("hidden");
        dashboardPage.classList.add("hidden");
    }
});

function updateClock(){

    const now = new Date();

    const hari = [
        "Minggu",
        "Senin",
        "Selasa",
        "Rabu",
        "Kamis",
        "Jumat",
        "Sabtu"
    ];

    const bulan = [
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember"
    ];

    const tanggal =
        hari[now.getDay()] + ", " +
        now.getDate() + " " +
        bulan[now.getMonth()] + " " +
        now.getFullYear();

    const jam =
        String(now.getHours()).padStart(2,"0") + ":" +
        String(now.getMinutes()).padStart(2,"0") + ":" +
        String(now.getSeconds()).padStart(2,"0");

    document.getElementById("currentDateTime").innerHTML =
        tanggal + "<br><small>" + jam + " WIB</small>";

}

updateClock();

setInterval(updateClock,1000);
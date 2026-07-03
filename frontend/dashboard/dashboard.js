let quickChats = [
  {
    question: "Sebutkan tahun kejadian banjir di Bali?",
    status: "Aktif"
  },
  {
    question: "Longsor di Jawa Timur terjadi kapan?",
    status: "Aktif"
  },
  {
    question: "Informasi kebencanaan apa saja yang bisa dicari masyarakat melalui SITABA?",
    status: "Aktif"
  }
];

let visitors = [
  {
    name: "Anasta",
    email: "anasta@email.com",
    total: 3
  }
];

const tableArea = document.getElementById("tableArea");
const pageTitle = document.getElementById("pageTitle");
const pageDesc = document.getElementById("pageDesc");
const searchInput = document.getElementById("searchInput");

const modal = document.getElementById("modal");
const addButton = document.getElementById("addButton");
const closeModal = document.getElementById("closeModal");
const saveQuestion = document.getElementById("saveQuestion");
const questionInput = document.getElementById("questionInput");
const statusInput = document.getElementById("statusInput");

document.getElementById("totalUser").innerText = visitors.length;
document.getElementById("totalChat").innerText = quickChats.length;
document.getElementById("avgResponse").innerText = "1.2s";

let currentPage = "quick";

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

function renderQuickChat() {
  pageTitle.innerText = "Quick Chat";
  pageDesc.innerText = "Kelola daftar pertanyaan cepat yang tampil di chatbot SINTA.";

  const keyword = searchInput.value.toLowerCase();

  const rows = quickChats
    .filter(item => item.question.toLowerCase().includes(keyword))
    .map((item, index) => `
      <tr>
        <td>${index + 1}</td>
        <td>${safeText(item.question)}</td>
        <td>
          <span class="badge ${item.status === "Aktif" ? "active-badge" : "off-badge"}">
            ${item.status}
          </span>
        </td>
        <td>
          <button class="action-btn" onclick="toggleStatus(${index})">Ubah Status</button>
        </td>
      </tr>
    `)
    .join("");

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
        ${rows || `<tr><td colspan="4" class="empty">Data tidak ditemukan.</td></tr>`}
      </tbody>
    </table>
  `;
}

function renderVisitors() {
  pageTitle.innerText = "User Pengunjung";
  pageDesc.innerText = "Daftar pengunjung yang menggunakan chatbot SINTA.";

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
        ${visitors.map((item, index) => `
          <tr>
            <td>${index + 1}</td>
            <td>${safeText(item.name)}</td>
            <td>${safeText(item.email)}</td>
            <td>${item.total}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;
}

function renderLogs() {
  pageTitle.innerText = "Log Percakapan";
  pageDesc.innerText = "Riwayat pertanyaan yang masuk ke AI SITABA.";

  tableArea.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>Waktu</th>
          <th>User</th>
          <th>Pertanyaan</th>
          <th>Intent</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Hari ini</td>
          <td>Anasta</td>
          <td>Sebutkan tahun kejadian banjir di Bali?</td>
          <td>DISASTER</td>
        </tr>
      </tbody>
    </table>
  `;
}

function renderSetting() {
  pageTitle.innerText = "Pengaturan";
  pageDesc.innerText = "Pengaturan tampilan dan fitur chatbot SINTA.";

  tableArea.innerHTML = `
    <div class="empty">
      Pengaturan lanjutan dapat dihubungkan ke Supabase pada tahap berikutnya.
    </div>
  `;
}

function setPage(page) {
  currentPage = page;

  document.querySelectorAll(".menu").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.page === page);
  });

  if (page === "quick" || page === "assistant") renderQuickChat();
  if (page === "visitor") renderVisitors();
  if (page === "logs") renderLogs();
  if (page === "setting") renderSetting();
}

function toggleStatus(index) {
  quickChats[index].status = quickChats[index].status === "Aktif" ? "Nonaktif" : "Aktif";
  renderQuickChat();
}

document.querySelectorAll(".menu").forEach(btn => {
  btn.addEventListener("click", () => setPage(btn.dataset.page));
});

searchInput.addEventListener("input", () => {
  if (currentPage === "quick" || currentPage === "assistant") {
    renderQuickChat();
  }
});

addButton.addEventListener("click", () => {
  modal.classList.remove("hidden");
});

closeModal.addEventListener("click", () => {
  modal.classList.add("hidden");
});

saveQuestion.addEventListener("click", () => {
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

  document.getElementById("totalChat").innerText = quickChats.length;
  renderQuickChat();
});

setPage("quick");
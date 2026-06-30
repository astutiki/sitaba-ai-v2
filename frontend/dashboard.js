const API_URL = "http://localhost:3000/api";

let token = localStorage.getItem("sitaba_token");
let editingId = null;

function safeText(value) {
  return String(value ?? "").replace(/[<>]/g, "");
}

async function loginAdmin() {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: "adminsitaba",
      password: "admin123"
    })
  });

  const data = await res.json();

  if (data.token) {
    token = data.token;
    localStorage.setItem("sitaba_token", token);
    return token;
  }

  throw new Error("Login gagal");
}

async function apiFetch(path, options = {}) {
  if (!token) {
    await loginAdmin();
  }

  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      ...(options.headers || {})
    }
  });

  if (res.status === 401 || res.status === 403) {
    localStorage.removeItem("sitaba_token");
    token = null;
    await loginAdmin();
    return apiFetch(path, options);
  }

  return res.json();
}

async function loadDashboard() {
  const data = await apiFetch("/dashboard");

  document.getElementById("totalUser").innerText = safeText(data.totalUser);
  document.getElementById("totalChat").innerText = safeText(data.totalChat);
  document.getElementById("avgResponse").innerText = safeText(data.avgResponse);
}

async function loadQuickChat() {
  const data = await apiFetch("/quickchat");
  const tbody = document.getElementById("quickChatTable");

  tbody.innerHTML = "";

  data.forEach((item, index) => {
    const row = document.createElement("tr");

    const no = document.createElement("td");
    no.innerText = index + 1;

    const question = document.createElement("td");
    question.innerText = safeText(item.question);

    const status = document.createElement("td");
    const toggle = document.createElement("button");
    toggle.className = item.status === "Aktif" ? "toggle active" : "toggle";
    toggle.onclick = () => toggleStatus(item.id);
    status.appendChild(toggle);

    const action = document.createElement("td");

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "action-btn";
    deleteBtn.innerText = "🗑";
    deleteBtn.onclick = () => deleteQuickChat(item.id);

    const editBtn = document.createElement("button");
    editBtn.className = "action-btn";
    editBtn.innerText = "✎";
    editBtn.onclick = () => openEditModal(item);

    action.appendChild(deleteBtn);
    action.appendChild(editBtn);

    row.appendChild(no);
    row.appendChild(question);
    row.appendChild(status);
    row.appendChild(action);

    tbody.appendChild(row);
  });
}

async function loadUsers() {
  const data = await apiFetch("/users");
  const tbody = document.getElementById("userTable");

  tbody.innerHTML = "";

  data.forEach((item, index) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${index + 1}</td>
      <td></td>
      <td></td>
      <td><button class="action-btn">👁</button></td>
    `;

    row.children[1].innerText = safeText(item.name);
    row.children[2].innerText = safeText(item.email);

    tbody.appendChild(row);
  });
}

function openAddModal() {
  editingId = null;
  document.getElementById("modalTitle").innerText = "Tambah Quick Chat";
  document.getElementById("quickInput").value = "";
  document.getElementById("modalOverlay").classList.remove("hidden");
}

function openEditModal(item) {
  editingId = item.id;
  document.getElementById("modalTitle").innerText = "Edit Quick Chat";
  document.getElementById("quickInput").value = safeText(item.question);
  document.getElementById("modalOverlay").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("modalOverlay").classList.add("hidden");
}

async function saveQuickChat() {
  const question = document.getElementById("quickInput").value.trim();

  if (question.length < 10 || question.length > 200) {
    alert("Pertanyaan harus 10-200 karakter.");
    return;
  }

  if (editingId) {
    await apiFetch(`/quickchat/${editingId}`, {
      method: "PUT",
      body: JSON.stringify({ question })
    });
  } else {
    await apiFetch("/quickchat", {
      method: "POST",
      body: JSON.stringify({ question })
    });
  }

  closeModal();
  loadQuickChat();
}

async function toggleStatus(id) {
  await apiFetch(`/quickchat/${id}/toggle`, {
    method: "PUT"
  });
  loadQuickChat();
}

async function deleteQuickChat(id) {
  if (!confirm("Hapus quick chat ini?")) return;

  await apiFetch(`/quickchat/${id}`, {
    method: "DELETE"
  });

  loadQuickChat();
}

function showTab(tab) {
  document.getElementById("quickSection").classList.toggle("hidden", tab !== "quick");
  document.getElementById("userSection").classList.toggle("hidden", tab !== "users");

  document.getElementById("tabQuick").classList.toggle("active", tab === "quick");
  document.getElementById("tabUsers").classList.toggle("active", tab === "users");
}

function logout() {
  localStorage.removeItem("sitaba_token");
  location.reload();
}

async function init() {
  await loadDashboard();
  await loadQuickChat();
  await loadUsers();
}

init();
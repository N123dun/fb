// ---------- Tabs ----------
document.querySelectorAll(".tab-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById(btn.dataset.tab).classList.add("active");
  });
});

// ---------- Mentor Chat ----------
const chatWindow = document.getElementById("chatWindow");
const chatInput = document.getElementById("chatInput");
const sendBtn = document.getElementById("sendBtn");
const matchesArea = document.getElementById("matchesArea");
const roadmapArea = document.getElementById("roadmapArea");

function addMessage(text, who) {
  const div = document.createElement("div");
  div.className = `msg ${who}`;
  div.textContent = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function startChat() {
  matchesArea.classList.add("hidden");
  roadmapArea.classList.add("hidden");
  matchesArea.innerHTML = "";
  roadmapArea.innerHTML = "";
  chatWindow.innerHTML = "";
  const res = await fetch("/api/chat/start", { method: "POST" });
  const data = await res.json();
  addMessage(data.reply, "bot");
}

async function sendMessage() {
  const text = chatInput.value.trim();
  if (!text) return;
  addMessage(text, "user");
  chatInput.value = "";

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text }),
  });
  const data = await res.json();
  addMessage(data.reply, "bot");

  if (data.done && data.matches) {
    renderMatches(data.matches);
  }
}

function renderMatches(matches) {
  matchesArea.classList.remove("hidden");
  matchesArea.innerHTML = "<h3>Top career matches</h3>";
  matches.forEach(m => {
    const card = document.createElement("div");
    card.className = "match-card";
    card.innerHTML = `
      <div class="sector">${m.sector}</div>
      <h4>${m.title}</h4>
      <p>${m.description}</p>
    `;
    card.addEventListener("click", () => loadRoadmap(m.id));
    matchesArea.appendChild(card);
  });
}

async function loadRoadmap(careerId) {
  const res = await fetch(`/api/roadmap/${careerId}`);
  const c = await res.json();
  roadmapArea.classList.remove("hidden");
  roadmapArea.innerHTML = `
    <div class="roadmap-block">
      <h3>${c.title} — Roadmap</h3>
      <p><strong>Core skills to build:</strong></p>
      <ul>${c.core_skills.map(s => `<li>${s}</li>`).join("")}</ul>
      <p><strong>Where to start learning:</strong></p>
      <ul>${c.resources.map(r => `<li><a href="${r.url}" target="_blank" rel="noopener">${r.name}</a> — ${r.cost}</li>`).join("")}</ul>
    </div>
  `;
  roadmapArea.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

sendBtn.addEventListener("click", sendMessage);
chatInput.addEventListener("keydown", e => { if (e.key === "Enter") sendMessage(); });

startChat();

// ---------- CV Builder ----------
const educationList = document.getElementById("educationList");
const experienceList = document.getElementById("experienceList");
const projectsList = document.getElementById("projectsList");

function addRepeatBlock(container, fields) {
  const block = document.createElement("div");
  block.className = "repeat-block";
  block.innerHTML =
    fields.map(f => `<label>${f.label}<input type="text" data-field="${f.key}" placeholder="${f.placeholder || ""}"></label>`).join("") +
    `<button type="button" class="remove-btn">Remove</button>`;
  block.querySelector(".remove-btn").addEventListener("click", () => {
    block.remove();
    updatePreview();
  });
  block.querySelectorAll("input").forEach(inp => inp.addEventListener("input", updatePreview));
  container.appendChild(block);
  updatePreview();
}

document.getElementById("addEducation").addEventListener("click", () => {
  addRepeatBlock(educationList, [
    { key: "degree", label: "Degree / Qualification", placeholder: "e.g. G.C.E. A/L, BSc in IT" },
    { key: "institution", label: "Institution", placeholder: "e.g. Royal College" },
    { key: "year", label: "Year", placeholder: "e.g. 2024" },
  ]);
});

document.getElementById("addExperience").addEventListener("click", () => {
  addRepeatBlock(experienceList, [
    { key: "role", label: "Role", placeholder: "e.g. Intern, Volunteer" },
    { key: "organization", label: "Organization", placeholder: "" },
    { key: "duration", label: "Duration", placeholder: "e.g. Jun 2024 - Aug 2024" },
    { key: "description", label: "What you did", placeholder: "One or two lines" },
  ]);
});

document.getElementById("addProject").addEventListener("click", () => {
  addRepeatBlock(projectsList, [
    { key: "name", label: "Project name", placeholder: "" },
    { key: "description", label: "Description", placeholder: "" },
  ]);
});

function collectRepeatBlocks(container) {
  return Array.from(container.querySelectorAll(".repeat-block")).map(block => {
    const obj = {};
    block.querySelectorAll("input").forEach(inp => { obj[inp.dataset.field] = inp.value.trim(); });
    return obj;
  });
}

function collectFormData() {
  const form = document.getElementById("cvForm");
  const fd = new FormData(form);
  const skills = (fd.get("skills") || "").split(",").map(s => s.trim()).filter(Boolean);
  const languages = (fd.get("languages") || "").split(",").map(s => s.trim()).filter(Boolean);

  return {
    full_name: fd.get("full_name") || "",
    email: fd.get("email") || "",
    phone: fd.get("phone") || "",
    location: fd.get("location") || "",
    target_career: fd.get("target_career") || "",
    summary: fd.get("summary") || "",
    skills,
    languages,
    education: collectRepeatBlocks(educationList),
    experience: collectRepeatBlocks(experienceList),
    projects: collectRepeatBlocks(projectsList),
  };
}

function updatePreview() {
  const d = collectFormData();
  const box = document.getElementById("previewBox");
  const contactBits = [d.email, d.phone, d.location].filter(Boolean).join(" | ");

  let html = `<h1>${d.full_name || "Your Name"}</h1>`;
  if (contactBits) html += `<div class="contact">${contactBits}</div>`;
  if (d.target_career) html += `<div class="contact"><em>Target Role: ${d.target_career}</em></div>`;

  if (d.summary) {
    html += `<h2>Summary</h2><p>${d.summary}</p>`;
  }
  if (d.skills.length) {
    html += `<h2>Skills</h2><p>${d.skills.join(", ")}</p>`;
  }
  if (d.education.length) {
    html += `<h2>Education</h2>` + d.education.map(e =>
      `<p><strong>${e.degree || ""}</strong> — ${[e.institution, e.year].filter(Boolean).join(", ")}</p>`).join("");
  }
  if (d.experience.length) {
    html += `<h2>Experience</h2>` + d.experience.map(e =>
      `<p><strong>${e.role || ""}</strong> — ${[e.organization, e.duration].filter(Boolean).join(", ")}<br>${e.description || ""}</p>`).join("");
  }
  if (d.projects.length) {
    html += `<h2>Projects</h2>` + d.projects.map(p =>
      `<p><strong>${p.name || ""}</strong> — ${p.description || ""}</p>`).join("");
  }
  if (d.languages.length) {
    html += `<h2>Languages</h2><p>${d.languages.join(", ")}</p>`;
  }
  box.innerHTML = html;
}

document.getElementById("cvForm").addEventListener("input", updatePreview);

document.getElementById("cvForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = collectFormData();
  const res = await fetch("/api/cv/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    alert("Something went wrong generating the CV.");
    return;
  }
  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${(data.full_name || "FuturePath").replace(/\s+/g, "_")}_CV.docx`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  window.URL.revokeObjectURL(url);
});

// seed one empty block of each so the form isn't intimidatingly empty
addRepeatBlock(educationList, [
  { key: "degree", label: "Degree / Qualification", placeholder: "e.g. G.C.E. A/L, BSc in IT" },
  { key: "institution", label: "Institution", placeholder: "e.g. Royal College" },
  { key: "year", label: "Year", placeholder: "e.g. 2024" },
]);
updatePreview();

// === Existing chat code ===
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function addMessage(text, sender, isNew = false) {
  const div = document.createElement("div");
  div.className = sender + (isNew ? " new-message" : "");
  div.innerHTML = `<span class="bubble">${text}</span>`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const inputBox = document.getElementById("user-input");
  const userMessage = inputBox.value.trim();
  if (!userMessage) return;
  inputBox.value = "";

  // Add user bubble
  addMessage(userMessage, "user", true);

  // Show typing indicator
  const typingDiv = document.createElement("div");
  typingDiv.className = "bot typing-indicator";
  typingDiv.innerHTML = `<span></span><span></span><span></span>`;
  chatBox.appendChild(typingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  // Fetch bot response
  const res = await fetch("http://localhost:5000/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await res.json();

  // Remove typing indicator
  typingDiv.remove();

  // Add bot bubble
  addMessage(data.response, "bot", true);
}

// === Existing chat code ===
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function addMessage(text, sender) {
  const div = document.createElement("div");
  div.className = sender;
  div.innerHTML = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const inputBox = document.getElementById("user-input");
    const userMessage = inputBox.value;
    inputBox.value = "";

    const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    });

    const data = await res.json();
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
}

// === New Recipe Search Code ===

// Only run if the recipes page exists
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('recipe-search');
  if (!searchInput) return;

  const recipeCards = document.querySelectorAll('.recipe-card');
  
  searchInput.addEventListener('input', () => {
    const filter = searchInput.value.toLowerCase();
    recipeCards.forEach(card => {
      const keywords = card.dataset.keywords.toLowerCase();
      const title = card.querySelector('h3').textContent.toLowerCase();
      if (keywords.includes(filter) || title.includes(filter)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

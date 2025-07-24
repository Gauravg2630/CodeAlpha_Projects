document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const questionInput = document.getElementById("question");
  const chatBox = document.getElementById("chat-box");
  const darkModeToggle = document.getElementById("dark-mode-toggle");
  const ttsToggle = document.getElementById("tts-toggle");

  let ttsEnabled = true;

  // Toggle Dark Mode
  darkModeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    darkModeToggle.textContent = document.body.classList.contains("dark-mode")
      ? "☀️ Light Mode"
      : "🌙 Dark Mode";
  });

  // Toggle Text-to-Speech
  ttsToggle.addEventListener("click", () => {
    ttsEnabled = !ttsEnabled;
    ttsToggle.textContent = ttsEnabled ? "🔊 TTS: ON" : "🔇 TTS: OFF";
  });

  // Send message and get answer
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();
    if (!question) return;

    appendMessage("You", question);
    questionInput.value = "";

    // Disable input while waiting for response
    questionInput.disabled = true;

    try {
      const response = await fetch("http://localhost:5000/ask", {  // full URL with port
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({ question }),
      });

      if (!response.ok) {
        // You can parse error JSON if backend sends error messages
        let errMsg = `Server error: ${response.status}`;
        try {
          const errData = await response.json();
          if (errData.error) errMsg += ` - ${errData.error}`;
        } catch {
          // ignore parse error
        }
        throw new Error(errMsg);
      }

      const data = await response.json();
      const answer = data.answer || "Sorry, I don't have an answer for that.";

      appendMessage("Bot", answer);

      if (ttsEnabled) speakText(answer);
    } catch (error) {
      console.error("Error fetching answer:", error);
      appendMessage("Bot", "⚠️ Something went wrong. Please try again.");
    } finally {
      questionInput.disabled = false;
      questionInput.focus();
    }
  });

  // Append messages to chat
  function appendMessage(sender, text) {
    const message = document.createElement("div");
    message.classList.add("message");
    message.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  // Text-to-Speech
  function speakText(text) {
    if (!window.speechSynthesis) return;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = 1;
    speechSynthesis.cancel();  // stop any ongoing speech
    speechSynthesis.speak(utterance);
  }
});

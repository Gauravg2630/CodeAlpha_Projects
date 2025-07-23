// Toggle Dark Mode
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
  const modeText = document.getElementById("modeText");
  modeText.innerText = document.body.classList.contains("dark-mode") ? "Light Mode" : "Dark Mode";
}

// Translate Text
async function translateText() {
  const inputText = document.getElementById("inputText").value.trim();
  const sourceLang = document.getElementById("sourceLang").value;
  const targetLang = document.getElementById("targetLang").value;
  const outputTextElement = document.getElementById("outputText");

  if (!inputText) {
    outputTextElement.innerText = "⚠️ Please enter some text.";
    return;
  }

  outputTextElement.innerText = "Translating...";

  try {
    const response = await fetch("http://localhost:5000/translate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        q: inputText,
        source: sourceLang,
        target: targetLang
      })
    });

    const data = await response.json();
    outputTextElement.innerText = data.translatedText || "No translation found.";
  } catch (error) {
    console.error("Translation Error:", error.message);
    outputTextElement.innerText = "❌ Translation failed. Please try again.";
  }
}

// Copy to Clipboard
function copyText() {
  const output = document.getElementById("outputText").innerText;
  if (!output || output === "Translating..." || output.startsWith("❌")) {
    alert("Nothing to copy!");
    return;
  }

  navigator.clipboard.writeText(output)
    .then(() => alert("✅ Text copied to clipboard!"))
    .catch(() => alert("❌ Failed to copy text."));
}

// Text-to-Speech
function speakText() {
  const text = document.getElementById("outputText").innerText;
  if (!text || text === "Translating..." || text.startsWith("❌")) {
    alert("Nothing to speak!");
    return;
  }

  const utterance = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(utterance);
}

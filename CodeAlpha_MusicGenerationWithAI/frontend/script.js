document.getElementById("generateBtn").addEventListener("click", async () => {
  const status = document.getElementById("status");
  const downloadLink = document.getElementById("downloadLink");

  status.textContent = "🎶 Generating music, please wait...";
  downloadLink.style.display = "none";

  try {
    const response = await fetch("http://localhost:5000/generate", {
      method: "POST",
    });

    const data = await response.json();

    if (data.status !== "success") throw new Error(data.message);

    const filePath = `http://localhost:5000/static/generated/${data.filename}`;

    downloadLink.href = filePath;
    downloadLink.textContent = "⬇️ Download Generated Music";
    downloadLink.setAttribute("download", data.filename);  // ✅ forces download
    downloadLink.style.display = "inline-block";            // ✅ more reliable than 'block'

    status.textContent = "✅ Music generated successfully!";
  } catch (error) {
    console.error("Error:", error);
    status.textContent = "❌ Error generating music. Please try again.";
    downloadLink.style.display = "none";
  }
});

document.getElementById("themeToggle").addEventListener("change", function () {
  const body = document.body;
  body.classList.toggle("dark-theme");
  body.classList.toggle("light-theme");
});

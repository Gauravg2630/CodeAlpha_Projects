const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post("/translate", async (req, res) => {
  const { q, source, target } = req.body;

  if (!q || !target) {
    return res.status(400).json({ error: "Missing text or target language." });
  }

  const langpair = `${source || 'en'}|${target}`;

  try {
    const response = await axios.get("https://api.mymemory.translated.net/get", {
      params: {
        q,
        langpair,
      },
    });

    const translatedText = response.data.responseData.translatedText;
    res.json({ translatedText });
  } catch (error) {
    console.error("Translation Error:", error.message);
    res.status(500).json({ error: "Translation failed. Try again later." });
  }
});

app.listen(5000, () => console.log("✅ Server running at http://localhost:5000"));

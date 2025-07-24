# 🤖 FAQ Chatbot using Flask & NLP | CodeAlpha Internship

This project is a simple AI-powered FAQ Chatbot developed using **Python**, **Flask**, **NLTK**, and **Scikit-learn**. It answers user queries based on a dataset of Frequently Asked Questions (FAQs) by using Natural Language Processing (NLP) techniques such as tokenization, TF-IDF vectorization, and cosine similarity.

## 📌 Features
- Accepts user questions through a web interface
- Preprocesses and matches questions using NLP
- Responds with the most relevant FAQ answer
- Logs errors and server activity
- Error-handling for invalid or blank inputs

## 🛠 Tech Stack
- Python 3
- Flask
- HTML/CSS (Jinja2 Templates)
- JavaScript (AJAX using Fetch API)
- NLTK (Natural Language Toolkit)
- Scikit-learn

## 🧠 NLP Techniques Used
- Tokenization (`punkt`)
- Stopword removal (`stopwords`)
- TF-IDF vectorization
- Cosine similarity for matching

## 📂 Project Structure

/faq-chatbot
├── chatbot.py
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── script.js
└── faqs.csv


## ⚙️ Setup Instructions

**Clone the repository**
git clone https://github.com/Gauravg2630/CodeAlpha_Projects/tree/main/CodeAlpha_ChatbotForFAQs.git
cd CodeAlpha_Projects/tree/main/CodeAlpha_ChatbotForFAQs

Create virtual environment (optional) :
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies :
pip install -r requirements.txt

Download NLTK data :
import nltk
nltk.download('punkt')
nltk.download('stopwords')

Run the app :
python app.py
Open in browser: http://localhost:5000

✅ Sample FAQ Question to Ask
What is Artificial Intelligence?
What is Machine Learning?
What is Python?
What is CodeAlpha?

📸 Screenshot
![Screenshot](Screenshot%20(534).png)

🎓 Internship Credit
This project was developed as part of the Artificial Intelligence Internship at CodeAlpha.

📬 Contact
For queries or contributions, feel free to reach out on LinkedIn.
LInkedin : (https://www.linkedin.com/in/gorav-gumber-9319a2342/)
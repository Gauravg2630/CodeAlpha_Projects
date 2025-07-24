from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import load_faq_data, get_answer
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

# Configure logging to show time and level
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Load FAQ data once at startup
try:
    faqs = load_faq_data()
    logging.info(f"Loaded {len(faqs)} FAQ entries.")
except Exception as e:
    logging.error(f"Failed to load FAQ data: {e}")
    faqs = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.form.get("question", "").strip()

        if not user_input:
            return jsonify({"error": "Error processing the input. Please ask a valid question."}), 400

        answer = get_answer(user_input, faqs)
        return jsonify({"answer": answer})

    except Exception as e:
        logging.exception("Error processing question")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

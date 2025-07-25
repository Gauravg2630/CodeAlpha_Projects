from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from utils.generate_music import generate_music
import os

app = Flask(__name__)
CORS(app)

GENERATED_FOLDER = os.path.join("static", "generated")
GENERATED_FILENAME = "generated_music.mid"

@app.route("/generate", methods=["POST"])
def generate():
    try:
        # Ensure the output directory exists
        os.makedirs(GENERATED_FOLDER, exist_ok=True)

        # Call your music generation function that should save the file here
        generate_music()

        # Check if file exists after generation
        generated_file_path = os.path.join(GENERATED_FOLDER, GENERATED_FILENAME)
        if not os.path.isfile(generated_file_path):
            return jsonify({"status": "error", "message": "Generated music file not found"}), 500

        return jsonify({"status": "success", "filename": GENERATED_FILENAME})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/download", methods=["GET"])
def download():
    return send_from_directory(GENERATED_FOLDER, GENERATED_FILENAME, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

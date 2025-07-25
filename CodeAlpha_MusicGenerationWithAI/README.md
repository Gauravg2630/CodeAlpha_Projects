AI Music Generator 🎵
An AI-powered music generation application leveraging deep learning (LSTM networks) to create new music sequences trained on MIDI datasets. Build your own AI composer!

Features :
Upload and preprocess diverse MIDI music data (classical, jazz, etc.)
Extract note sequences using music21 for model training
Train a deep learning LSTM model to learn and replicate music patterns
Generate new music sequences with the trained model
Download generated music as MIDI files
Responsive frontend with dark/light theme toggle for enhanced user experience

Tech Stack:
Backend: Python, Flask
AI/ML: TensorFlow / Keras (LSTM networks)
MIDI Processing: music21
Frontend: JavaScript, HTML, CSS
Others: Flask-CORS for cross-origin API communication

Folder Structure :
backend/
├── app.py               # Flask API server
├── dta/                 # Place your raw MIDI (.mid) files here
├── output/              # Trained model and notes pickle (auto-generated)
│   ├── music_model.h5
│   └── notes.pkl
├── static/
│   └── generated/       # Generated MIDI output saved here
│       └── generated_music.mid
└── utils/
    ├── generate_music.py  # Music generation logic
    ├── midi_to_notes.py   # Extract notes from MIDI files
    └── train_model.py     # Model training script
frontend/
├── index.html            # Frontend UI
├── style.css             # Styles including dark/light theme
└── script.js             # Frontend JS with API calls and theme toggle

Setup & Usage:
1. Clone the Repository
git clone https://github.com/Gauravg2630/CodeAlpha_Projects.git
cd CodeAlpha_Projects/CodeAlpha_MusicGenerationWithAI/backend

2. Install Dependencies
Ensure you have Python 3.7+ installed, then:
pip install -r requirements.txt

3. Prepare Dataset:
Place your MIDI .mid files inside:
backend/dta/

4. Extract Notes from MIDI Files:
Run the note extraction script to preprocess your dataset:
python -m utils.midi_to_notes
This creates notes.pkl in the backend/output/ folder.

5. Train the Model:
Train your LSTM model on the extracted notes:
python -m utils.train_model
This creates the model file music_model.h5 in backend/output/.

6. Run the Backend Server:
Start the Flask API server:
python app.py
The backend runs on http://localhost:5000.

7. Open the Frontend
Open frontend/index.html in your browser.
Click Generate Music to produce new music based on your trained model.
Use the Download button to save the generated MIDI file.
Toggle dark/light theme for your preferred UI experience.

API Endpoints:
Endpoint	Method	Description
/generate	POST	Generate new music from trained model
/download	GET	Download the last generated MIDI file

Notes on the output Folder :
The output folder contains your trained model and preprocessed notes.
Due to potentially large file sizes, it is excluded from GitHub via .gitignore.
To use the app, train the model locally by following steps 3-5.
Alternatively, provide pretrained files via separate file sharing if needed.

Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit pull requests.

Author
Gorav Gumber
AI Intern at CodeAlpha

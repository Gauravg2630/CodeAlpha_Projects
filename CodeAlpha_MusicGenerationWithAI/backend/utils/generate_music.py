import pickle
import numpy as np
from random import randint
from music21 import stream, note, chord, instrument
from tensorflow.keras.models import load_model
import os

def generate_music():
    # Load notes and mappings
    with open("output/notes.pkl", "rb") as f:
        notes = pickle.load(f)

    pitchnames = sorted(set(notes))
    n_vocab = len(pitchnames)

    note_to_int = {note: number for number, note in enumerate(pitchnames)}
    int_to_note = {number: note for number, note in enumerate(pitchnames)}

    sequence_length = 100
    start = randint(0, len(notes) - sequence_length - 1)
    pattern = notes[start:start + sequence_length]
    pattern = [note_to_int[n] for n in pattern]

    # Load model
    model = load_model("output/music_model.h5")

    prediction_output = []
    for _ in range(200):
        input_seq = np.reshape(pattern, (1, len(pattern), 1))
        input_seq = input_seq / float(n_vocab)

        prediction = model.predict(input_seq, verbose=0)
        index = np.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)

        pattern.append(index)
        pattern = pattern[1:]

    # Convert predictions to notes
    offset = 0
    output_notes = []
    for pattern in prediction_output:
        if ("." in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split(".")
            chord_notes = [note.Note(int(n)) for n in notes_in_chord]
            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            output_notes.append(new_note)
        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    midi_stream.insert(0, instrument.Piano())

    output_dir = "static/generated"
    os.makedirs(output_dir, exist_ok=True)
    midi_path = os.path.join(output_dir, "generated_music.mid")
    midi_stream.write("midi", fp=midi_path)

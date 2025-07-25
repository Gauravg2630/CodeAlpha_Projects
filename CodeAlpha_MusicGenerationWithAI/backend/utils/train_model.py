import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation
from tensorflow.keras.utils import to_categorical
import pickle
import os
from utils.midi_to_notes import midi_to_notes
    
def train_model():
    # Get notes by processing all MIDI files in dta folder
    notes = midi_to_notes()

    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save notes again (optional, since midi_to_notes already saves them)
    with open(os.path.join(output_folder, "notes.pkl"), "wb") as f:
        pickle.dump(notes, f)

    pitchnames = sorted(set(notes))
    n_vocab = len(pitchnames)
    note_to_int = {note: num for num, note in enumerate(pitchnames)}

    sequence_length = 100
    network_input = []
    network_output = []

    for i in range(0, len(notes) - sequence_length):
        seq_in = notes[i:i + sequence_length]
        seq_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in seq_in])
        network_output.append(note_to_int[seq_out])

    n_patterns = len(network_input)
    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(n_vocab)
    network_output = to_categorical(network_output)

    model = Sequential()
    model.add(LSTM(512, input_shape=(network_input.shape[1], network_input.shape[2]), return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(512))
    model.add(Dense(256))
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    model.fit(network_input, network_output, epochs=50, batch_size=64)
    model.save(os.path.join(output_folder, "music_model.h5"))

if __name__ == "__main__":
    train_model()

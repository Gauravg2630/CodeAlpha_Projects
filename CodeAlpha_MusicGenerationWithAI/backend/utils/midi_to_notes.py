import os
import glob
import pickle
from music21 import converter, instrument, note, chord

def midi_to_notes():
    midi_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dta')
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    notes = []

    # Loop through all MIDI files in dta folder
    for file in glob.glob(os.path.join(midi_folder, "*.mid")):
        print(f"Parsing {file}...")
        midi = converter.parse(file)

        parts = instrument.partitionByInstrument(midi)
        if parts:  # If the midi file has instrument parts
            notes_to_parse = parts.parts[0].recurse()
        else:
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                # For chord, save the normalOrder as dot-separated string
                notes.append('.'.join(str(n) for n in element.normalOrder))

    # Save notes to a pickle file
    with open(os.path.join(output_folder, "notes.pkl"), "wb") as filepath:
        pickle.dump(notes, filepath)

    print(f"Extracted {len(notes)} notes/chords from MIDI files.")
    print(f"Notes saved to {os.path.join(output_folder, 'notes.pkl')}")

    return notes  # Return notes list

# Run when this file is executed directly
if __name__ == "__main__":
    midi_to_notes()

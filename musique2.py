import mido
from mido import MidiFile, MidiTrack, Message, bpm2tempo
import random

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo to 120 BPM
tempo = bpm2tempo(120)  # 120 BPM
track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))

note_a4 = 69  # MIDI note number for A4
note_a5 = 81
note_e4 = 76
velocity = 64  # Velocity (volume)

for x in range(1,200):
    random_aigu = random.randint(70,100)
    random_grave = random.randint(35,60)
    track.append(Message('note_on', note=random_aigu, velocity=velocity, time=0))
    track.append(Message('note_on', note=random_grave, velocity=velocity, time=0))
    track.append(Message('note_on', note=random_grave + 12, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_aigu, velocity=velocity, time=100))
    random_aigu = random.randint(70,100)
    track.append(Message('note_on', note=random_aigu, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_aigu, velocity=velocity, time=100))
    random_aigu = random.randint(70,100)
    track.append(Message('note_on', note=random_aigu, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_aigu, velocity=velocity, time=100))
    random_aigu = random.randint(70,100)
    track.append(Message('note_on', note=random_aigu, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_aigu, velocity=velocity, time=100))
    random_aigu = random.randint(70,100)
    track.append(Message('note_on', note=random_aigu, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_aigu, velocity=velocity, time=100))
    random_aigu = random.randint(70,100)
    track.append(Message('note_on', note=random_aigu, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_aigu, velocity=velocity, time=100))

    track.append(Message('note_off', note=random_grave, velocity=velocity, time=0))
    track.append(Message('note_off', note=random_grave + 12, velocity=velocity, time=0))


track.append(Message('note_off', note=note_a4, velocity=velocity, time=250))
track.append(Message('note_off', note=note_a5, velocity=velocity, time=250))
track.append(Message('note_on', note=note_e4, velocity=velocity, time=0))
track.append(Message('note_off', note=note_e4, velocity=velocity, time=500))

mid.save('antoine_morceau.mid')
print("MIDI file saved as 'antoine_morceau.mid'")

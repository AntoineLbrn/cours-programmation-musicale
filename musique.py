from mido import Message
import fonctions

nom_du_fichier_midi = "prenom.mid"
track = fonctions.generer_track()
velocity = 70  # (volume)

midi_notes_list = fonctions.image_to_midi_list("joconde.jpg")

for i in range(1, len(midi_notes_list)):
    track.append(Message('note_on', note=midi_notes_list[i], velocity=velocity, time=0))
    track.append(Message('note_off', note=midi_notes_list[1], velocity=velocity, time=70))



fonctions.generer_midi(nom_du_fichier_midi, track)
fonctions.lire_midi(nom_du_fichier_midi)
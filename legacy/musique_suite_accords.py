from mido import Message
import fonctions

nom_du_fichier_midi = "antoine.mid"
track = fonctions.generer_track()
velocity = 64  # (volume)

# DO
for x in range(1,24):
    note = fonctions.note_aleatoire_accord_majeur(36, 70)
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=100))

# SOL
for x in range(1,24):
    note = fonctions.note_aleatoire_accord_majeur(43, 70)
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=100))

# LA MINEUR
for x in range(1,24):
    note = fonctions.note_aleatoire_accord_mineur(45, 70)
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=100))

# FA
for x in range(1,24):
    note = fonctions.note_aleatoire_accord_majeur(41, 70)
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=100))

fonctions.generer_midi(nom_du_fichier_midi, track)
fonctions.lire_midi(nom_du_fichier_midi)
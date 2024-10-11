from mido import Message
import fonctions

nom_du_fichier_midi = "antoine.mid"
track = fonctions.generer_track()
velocity = 64  # (volume)

for x in range(1,30):
    note_grave = fonctions.note_aleatoire_accord_mineur(24, 48)
    note_aigue = fonctions.note_aleatoire_accord_mineur(48, 108)

    track.append(Message('note_on', note=note_aigue, velocity=velocity, time=0))
    track.append(Message('note_on', note=note_grave, velocity=velocity, time=0))
    track.append(Message('note_on', note=note_grave + 12, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_aigue, velocity=velocity, time=100))

    note_aigue = fonctions.note_aleatoire_accord_mineur(48, 108)
    track.append(Message('note_on', note=note_aigue, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_aigue, velocity=velocity, time=100))

    note_aigue = fonctions.note_aleatoire_accord_mineur(48, 108)
    track.append(Message('note_on', note=note_aigue, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_aigue, velocity=velocity, time=100))

    note_aigue = fonctions.note_aleatoire_accord_mineur(48, 108)
    track.append(Message('note_on', note=note_aigue, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_aigue, velocity=velocity, time=100))

    note_aigue = fonctions.note_aleatoire_accord_mineur(48, 108)
    track.append(Message('note_on', note=note_aigue, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_aigue, velocity=velocity, time=100))

    note_aigue = fonctions.note_aleatoire_accord_mineur(48, 108)
    track.append(Message('note_on', note=note_aigue, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_aigue, velocity=velocity, time=100))

    note_grave = fonctions.note_aleatoire_accord_mineur(24, 48)
    track.append(Message('note_off', note=note_grave, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_grave + 12, velocity=velocity, time=0))

fonctions.generer_midi(nom_du_fichier_midi, track)
fonctions.lire_midi(nom_du_fichier_midi)
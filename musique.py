from mido import Message
import fonctions

nom_du_fichier_midi = "prenom.mid"
track = fonctions.generer_track()
velocity = 64  # (volume)

track.append(Message('note_on', note=60, velocity=velocity, time=0))
track.append(Message('note_off', note=60, velocity=velocity, time=1000))

fonctions.generer_midi(nom_du_fichier_midi, track)
fonctions.lire_midi(nom_du_fichier_midi)
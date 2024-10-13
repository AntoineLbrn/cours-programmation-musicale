# Lire et écrire des fichiers MIDI

Il ne suffit que de la librarie MIDO, disponible sur via le packet manager pip.

`pip3 install mido`

Pour lire ce fichier midi avec un synthéthiseur de piano, il faut également la librairie pygame (ou bien lire le fichier MIDI en sortie sur un logiciel externe)

`pip3 install pygame`

# Lire une image en musique

`python3 musique.py`

Si vous souhaitez une autre image que la joconde, veillez à remplacer la ligne

`midi_notes_list = fonctions.image_to_midi_list("joconde.jpg")`
from mido import MidiFile, MidiTrack, Message, bpm2tempo, MetaMessage
import pygame
import time
import random

def generer_track():
    track = MidiTrack()
    tempo = bpm2tempo(120)  # 120 BPM
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
    return track

def generer_midi(nom_fichier, track):
    mid = MidiFile()
    mid.tracks.append(track)
    mid.save("generated/" + nom_fichier)
    print("MIDI File saved, let's play")

def lire_midi(nom_fichier):
    pygame.mixer.init()
    pygame.mixer.music.load("generated/" + nom_fichier)
    pygame.mixer.music.play()

    # Keep the script alive while the music is playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def note_aleatoire(note_mini, note_maxi):
    return random.randint(note_mini, note_maxi)

def note_aleatoire_gamme_majeure(premiere_note_gamme, derniere_note_gamme):
    gamme = []
    while (premiere_note_gamme < derniere_note_gamme):
        gamme = gamme + [
            premiere_note_gamme, 
            premiere_note_gamme + 2, 
            premiere_note_gamme + 4,
            premiere_note_gamme + 5,
            premiere_note_gamme + 7,
            premiere_note_gamme + 9,
            premiere_note_gamme + 11
        ]
        premiere_note_gamme+=12
    return gamme[random.randint(0, len(gamme) - 1)]

def note_aleatoire_accord_majeur(premiere_note_accord, derniere_note_accord):
    notes = []
    while (premiere_note_accord < derniere_note_accord):
        notes = notes + [
            premiere_note_accord, 
            premiere_note_accord + 4,
            premiere_note_accord + 7,
        ]
        premiere_note_accord+=12
    return notes[random.randint(0, len(notes) - 1)]

def note_aleatoire_accord_mineur(premiere_note_accord, derniere_note_accord):
    notes = []
    while (premiere_note_accord < derniere_note_accord):
        notes = notes + [
            premiere_note_accord, 
            premiere_note_accord + 3,
            premiere_note_accord + 7,
        ]
        premiere_note_accord+=12
    return notes[random.randint(0, len(notes) - 1)]
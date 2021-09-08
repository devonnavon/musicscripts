from pychord import Chord
import random
import os
import time
import pandas as pd

os.system('clear')

def cleanIt(it):
    it.strip().lower()

notes = ['A','B','C','D','E','F','G','Ab','Bb','Db','Eb','Gb','A#','C#','D#','F#','G#']
types = ['7', 'maj7', 'm7']

ftc_dict = {'Ab':'G#','Bb':'A#','Db':'C#','Eb':'D#','Gb':'F#'}

chord_dict = []
for note in notes:
    for type in types:
        el = {
            'note':note,
            'type':type,
            'value':Chord(note+type).components()
        }

        chord_dict.append(el)

majors = [x for x in chord_dict if x['type'] in ['maj7', 'm7'] and '#' not in x['note']]
r_majors = random.sample(majors, len(majors))

# print(majors)

for chord in r_majors:
    print(chord['note']+chord['type'])
    user_chord = input()
    answer = ''.join(chord['value']).lower()
    while(user_chord.strip().lower()!=answer):
        print('wrong, try again (type show to give up)')
        user_chord = input()
        if user_chord.lower() == 'show': 
            print(answer)
            break

    os.system('clear')



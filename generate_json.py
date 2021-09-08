from pychord import Chord
import pandas as pd
import json

notes = ['A','B','C','D','E','F','G','Ab','Bb','Db','Eb','Gb','A#','C#','D#','F#','G#']
types = ['7', 'maj7', 'm7', 'm7b5', 'dim7']

ftc_dict = {'Ab':'G#','Bb':'A#','Db':'C#','Eb':'D#','Gb':'F#'}
dct = {v: k for k, v in ftc_dict.items()}
ftc_dict.update(dct)

chord_dict = []
for note in notes:
    for type in types:
        value = Chord(note+type).components()
        variation = []
        if '#' not in note and 'b' not in note:            
            for n in value:
                if '#' not in n and 'b' not in n:
                    variation.append(n)
                else:
                    variation.append(ftc_dict[n])
        el = {
            'name': note+type,
            'note':note,
            'type':type,
            'value':value,
            'variation': variation 
        }

        chord_dict.append(el)

with open('chords.json', 'w') as f:
    json.dump(chord_dict, f)

set_dict = []

string_sets = [[3,4,5,6],[1,2,3,4],[2,3,4,5],[2,3,4,6],[1,2,3,5],[1,2,3,6],[1,2,5,6]]

shapes=[]
for s in string_sets:
    for n in s:
        ss = "".join([str(x) for x in s])
        shapes.append(
                {
                    "set": ss,
                    "shape":f'{ss}R{n}',
                    "root": n
                }
            )
with open('string_sets.json', 'w') as f:
    json.dump(shapes, f)
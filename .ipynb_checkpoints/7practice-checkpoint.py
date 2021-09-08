import random
import os
import time
import pandas as pd

os.system('clear')

string_sets = [[1,2,3,4],[2,3,4,5],[2,3,4,6]]

chords = ['7', 'maj7', 'min7','Ø7']
letters = ['A','B','C','D','E','F','G']

shapes=[]
for s in string_sets:
    for n in s:
        ss = "".join([str(x) for x in s])
        shapes.append(
                {
                    "shape":f'{ss}R{n}',
                    "set": ss
                }
            )

out = []
for shape in shapes:
    for chord in chords:
        out.append(
                {
                    "out":f'{random.choice(letters)}{chord} - {shape["shape"]}',
                    "set": shape["set"],
                    "chord": chord
                }
            )

# print('Press enter when you find the chord')

random_out = random.sample(out, len(out))

# print(len(random_out))

set_summary = {}
chord_summary = {}

for i,x in enumerate(random_out):
    print(f'({i+1}) ',x["out"],end = "\r")
    start = time.time()
    input()
    end = time.time()
    elapsed = end - start
    if x["set"] in set_summary:
        set_summary[x["set"]].append(elapsed)
    else:
        set_summary[x["set"]] = [elapsed]
    
    if x["chord"] in set_summary:
        chord_summary[x["chord"]].append(elapsed)
    else:
        chord_summary[x["chord"]] = [elapsed]

print('\nSet Summary')
print(pd.DataFrame(set_summary).mean().sort_values(ascending=False).round(2))
print('\nChord Summary')
print(pd.DataFrame(chord_summary).mean().sort_values(ascending=False).round(2))


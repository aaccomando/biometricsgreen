import pandas as pd
import numpy as np

ev = []

import csv
with open('output.csv', 'r') as f:
    reader = csv.reader(f)
    ev = list(reader)

easyLag = 0
easyCount = 0
medLag = 0
medCount = 0
hardLag = 0
hardCount = 0

for x in range(1, len(ev) - 1):
    # only get avg lag bewtween presses of same passwd type
    if ev[x-1][14] == ev[x][14]:
        if ev[x][14] == '0':
            easyLag += int(ev[x][5]) - int(ev[x-1][4])
            easyCount += 1
        elif ev[x][14] == '1':
            medLag += int(ev[x][5]) - int(ev[x-1][4])
            medCount += 1
        elif ev[x][14] == '2':
            hardLag += int(ev[x][5]) - int(ev[x-1][4])
            hardCount += 1

easyAvg = easyLag/easyCount
medAvg = medLag/medCount
hardAvg = hardLag/hardCount

print("Easy Average: {0}".format(easyAvg))
print("Medium Average: {0}".format(medAvg))
print("Hard Average: {0}".format(hardAvg))

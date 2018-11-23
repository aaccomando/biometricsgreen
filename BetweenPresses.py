import pandas as pd
import numpy as np

ev = []

import csv
with open('output.csv', 'r') as f:
    reader = csv.reader(f)
    ev = list(reader)

easyLag = {}
easyCount = {}
medLag = {}
medCount = {}
hardLag = {}
hardCount = {}

for x in range(1, len(ev) - 1):
    # only get avg lag bewtween presses of same passwd type
    if ev[x-1][14] == ev[x][14] and ev[x-1][0] == ev[x][0]:
        user = int(ev[x][0])
        if ev[x][14] == '0':
            if user in easyLag:
                easyLag[user] += int(ev[x][5]) - int(ev[x-1][4])
                easyCount[user] += 1
            else:
                easyLag[user] = int(ev[x][5]) - int(ev[x-1][4])
                easyCount[user] = 1
        elif ev[x][14] == '1':
            if user in medLag:
                medLag[user] += int(ev[x][5]) - int(ev[x-1][4])
                medCount[user] += 1
            else:
                medLag[user] = int(ev[x][5]) - int(ev[x-1][4])
                medCount[user] = 1
        elif ev[x][14] == '2':
            if user in hardLag:
                hardLag[user] += int(ev[x][5]) - int(ev[x-1][4])
                hardCount[user] += 1
            else:
                hardLag[user] = int(ev[x][5]) - int(ev[x-1][4])
                hardCount[user] = 1
easyAvg = {}
for key, value in easyLag.items():
    easyAvg[key] = value / easyCount[key]
medAvg = {}
for key, value in medLag.items():
    medAvg[key] = value / medCount[key]
hardAvg = {}
for key, value in hardLag.items():
    hardAvg[key] = value / hardCount[key]

print('Easy Averages')
print('===========================')
for key, value in easyAvg.items():
    print("User: {0}\t Average:{1}".format(key, value))
print('Medium Averages')
print('===========================')
for key, value in medAvg.items():
    print("User: {0}\t Average:{1}".format(key, value))
print('Hard Averages')
print('===========================')
for key, value in medAvg.items():
    print("User: {0}\t Average:{1}".format(key, value))

import pandas as pd
import numpy as np

ev = []

import csv
with open('output.csv', 'r') as f:
    reader = csv.reader(f)
    ev = list(reader)


easyPre = 0
easyUp = 0 
easyDown = 0

medPre = 0
medUp = 0 
medDown = 0

hardPre = 0
hardUp = 0 
hardDown = 0

easyTotal = 0
medTotal = 0
hardTotal = 0

for x in ev[1::]:
    if x[14] == '0':
        easyPre =+ float(x[6])
        easyUp =+ float(x[5])
        easyDown =+ float(x[4])
        easyTotal += 1
    elif x[14] == '1':
        medPre =+ float(x[6])
        medUp =+ float(x[5])
        medDown =+ float(x[4])
        hardTotal += 1
    elif x[14] == '2':
        hardPre =+ float(x[6])
        hardUp =+ float(x[5])
        hardDown =+ float(x[4])
        hardTotal += 1
    
nEP = easyPre/easyTotal
nEU = easyUp/easyTotal
nED = easyDown/easyTotal

nMP = medPre/medTotal
nMU = medUp/medTotal
nMD = medDown/medTotal

nHP = hardPre/hardTotal
nHU = hardUp/hardTotal
nHD = hardDown/hardTotal

print('-------------Easy-----------------')
print('Pressure')
print(float(nEP))
print('\nUpTime')
print(nEU)
print('\nDownTime')
print(nED)

print('\n-----------Medium----------------')
print('Pressure')
print(nMP)
print('\nUpTime')
print(nMU)
print('DownTime')
print(nMD)

print('\n--------------------Hard------------------')
print('Pressure')
print(nHP)
print('\nUpTime')
print(nHU)
print('\nDownTime')
print(nHD)






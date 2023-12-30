
base = 0

beacons = [(4, 58), (5, 58), (26, 56), (27, 56)]

statements = ''


for i , beacon in enumerate(beacons) : 
    statement = f'LINE {base} {beacons[i][0]} 1| ' 
    statements += statement

print(statements[:-2])
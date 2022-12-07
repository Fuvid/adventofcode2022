f = open("inputs/day2.txt", "r")
# A Rock
# B Paper
# C Scissors
# X Rock
# Y Paper
# Z Scissors
matrix = []
matrix.append([])
matrixa = matrixb = matrixc = {}
matrixa = {'X': 3, 'Y': 6, 'Z': 0}
matrixb = {'X': 0, 'Y': 3, 'Z': 6}
matrixc = {'X': 6, 'Y': 0, 'Z': 3}
matrixm = {'X': 1, 'Y': 2, 'Z': 3}


def resolve(o, m):
    if o == "A":
        return matrixa[m]
    elif o == "B":
        return matrixb[m]
    elif o == "C":
        return matrixc[m]


points = 0
for x in f:
    x.split(' ')
    opponent = x.split(' ')[0]
    mychoice = x.split(' ')[1].strip()
    points += resolve(opponent, mychoice) + matrixm[mychoice]

print(points)
f.close()

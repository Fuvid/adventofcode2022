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
matrixa = {'X': 3, 'Y': 1, 'Z': 2}
matrixb = {'X': 1, 'Y': 2, 'Z': 3}
matrixc = {'X': 2, 'Y': 3, 'Z': 1}
matrixm = {'X': 0, 'Y': 3, 'Z': 6}


def resolve(o, m): 
    if o == "A": 
        return matrixa[m]+matrixm[m]
    elif o == "B": 
        return matrixb[m]+matrixm[m]
    elif o == "C": 
        return matrixc[m]+matrixm[m]


points = 0
for x in f:
    x.split(' ')
    opponent = x.split(' ')[0]
    mychoice = x.split(' ')[1].strip()
    points = points+ resolve(opponent, mychoice)

print(points)
f.close()

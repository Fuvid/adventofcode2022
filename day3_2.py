f = open("inputs/day3.txt", "r")
priorities = 0
def prio(c):
    if c.isupper():
        newc= c.lower()
    else:
        newc = c.upper()
    order = ord(newc)-64
    if (order > 26):
        order -= 6
    return order
def findcommon(truple):
    for c in truple[0]:
        if truple[1].find(c) > -1 and truple[2].find(c) > -1:
            return c
start = 0
truple = {}

for x in f:
    truple[start] = x
    if start == 2:
        common = findcommon(truple)
        priorities += prio(common)
        start = 0
        truple = {}
    else:
        start += 1    
print (priorities)
f.close()
#nicht 10435
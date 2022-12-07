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

for x in f:
    x = x.strip()
    middle = int(len(x)/2)
    front = x[:middle]
    back = x[middle:]
    for c in front:
        if back.find(c) != -1:
            prio_res = prio(c)
            print(c + str(prio_res))
            priorities += prio_res
            break
print (priorities)
f.close()
#nicht 10435
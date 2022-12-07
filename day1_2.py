f = open("inputs/day1.txt", "r")
print(f.readline())
max1 = 0
max2 = 0
max3 = 0
current = 0;
for x in f:
  if x == '\n':
    if current > max1:
      max3 = max2
      max2 = max1
      max1 = current
    else:
      if current > max2:
        max3 = max2
        max2 = current
      else:
          if current > max3:
            max3 = current
    current = 0
    continue
  current += int(x)
print(max1)
print(max2)
print(max3)
print(max1+max2+max3)  
f.close()
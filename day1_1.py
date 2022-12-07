f = open("inputs/day1.txt", "r")
print(f.readline())
max = 0
current = 0;
for x in f:
  if x == '\n':
    if current > max:
        max = current
    current = 0
    continue
  current += int(x)


print(max)
  
f.close()
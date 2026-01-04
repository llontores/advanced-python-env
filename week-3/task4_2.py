a = 0
b = 0
R = 5

points = [(1,2), (6,1), (0,0)]
count = 0

for x, y in points:
    if (x-a)**2 + (y-b)**2 <= R*R:
        count = count + 1

print(count)

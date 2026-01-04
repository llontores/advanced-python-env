A = 1
B = 2
C = 3
D = 4

num = A * D
den = B * C

while den != 0:
    num, den = den, num % den

print(num)

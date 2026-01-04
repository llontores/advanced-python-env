a1 = 3
b1 = 4
a2 = 6
b2 = 8

h1 = (a1*a1 + b1*b1) ** 0.5
h2 = (a2*a2 + b2*b2) ** 0.5

print(h1)
print(h2)

if h1 > h2:
    print("First bigger")
else:
    print("Second bigger")

eq = input()
a = eq[0]
op = eq[1]
b = eq[2]
c = eq[4]

if a == 'x':
    if op == '+': print(int(c) - int(b))
    else: print(int(c) + int(b))
elif b == 'x':
    if op == '+': print(int(c) - int(a))
    else: print(int(a) - int(c))
else: # c == 'x'
    if op == '+': print(int(a) + int(b))
    else: print(int(a) - int(b))
a = input()
b = input()
n, m = len(a), len(b)

shifts = []
temp_b = b
for _ in range(m):
    temp_b = temp_b[1:] + temp_b[0]
    is_new = True
    for s in shifts:
        if s == temp_b:
            is_new = False
    if is_new:
        shifts.append(temp_b)

count = 0
for i in range(n - m + 1):
    substring = a[i:i+m]
    for s in shifts:
        if substring == s:
            count += 1
            break
print(count)
N = int(input())

if N >= 1:
    total = sum(range(1, N + 1))
else:
    total = sum(range(N, 1 + 1))

print(total)

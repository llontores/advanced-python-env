m = int(input())
arr = []

for i in range(m):
    arr.append(int(input()))

print(arr)

arr[0], arr[-1] = arr[-1], arr[0]

print(arr)

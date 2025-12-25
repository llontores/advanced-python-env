s = input()
target1 = ">>-->"
target2 = "<--<<"
count = 0
for i in range(len(s) - 4):
    if s[i:i+5] == target1 or s[i:i+5] == target2:
        count += 1
print(count)
text = input()
words = text.split()
result = ""

for w in words:
    letters = list(w)
    letters.sort()
    result = result + "".join(letters) + " "

print(result)

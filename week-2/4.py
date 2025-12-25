line1 = input().split()
n, m = int(line1[0]), int(line1[1])
text = input()

unique_words = []
for i in range(n - m + 1):
    word = text[i:i+m]
    found = False
    for uw in unique_words:
        if uw == word:
            found = True
            break
    if not found:
        unique_words.append(word)

print(len(unique_words))
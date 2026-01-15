file = open("text.txt", "r")
text = file.read()
file.close()

lines = text.split("\n")
words = text.split()

result = open("analysis.txt", "w")
result.write("Lines: " + str(len(lines)) + "\n")
result.write("Words: " + str(len(words)))
result.close()

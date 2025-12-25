items = input().split()
counts = {}

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print("Purchase frequency:")
for item in counts:
    print(item + ": " + str(counts[item]))

most_popular = ""
max_c = 0
for item in counts:
    if counts[item] > max_c:
        max_c = counts[item]
        most_popular = item
print("Most popular item:", most_popular)

once = []
for item in counts:
    if counts[item] == 1:
        once.append(item)
print("Purchased once:", " ".join(once))

items_list = []
for item in counts:
    items_list.append([item, counts[item]])

for i in range(len(items_list)):
    for j in range(len(items_list) - 1):
        if items_list[j][1] < items_list[j+1][1]:
            items_list[j], items_list[j+1] = items_list[j+1], items_list[j]

print("Sorted by frequency:")
for pair in items_list:
    print(pair[0], pair[1])
import common.parser as parse

tokens = parse.get_ints(1)

first = []
second = []
for token in tokens:
    first += [ token[0] ]
    second += [ token[1] ]

first.sort()
second.sort()

sum = 0
for i in range(0, len(first)):
    sum += abs(first[i] - second[i])

print(sum)

occurences = {}
for i in second:
    if i not in occurences:
        occurences[i] = 0

    occurences[i] += 1

newsum = 0
for i in first:
    if i not in occurences:
        continue

    newsum += i * occurences[i]

print(newsum)

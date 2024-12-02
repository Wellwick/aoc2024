import common.parser as parse

int_tokens = parse.get_ints(2)

def appropriate_differ(row : list[int]):
    last = row[0]
    for i in row[1:]:
        diff = abs(i - last)
        if diff < 1 or diff > 3:
            return False
        
        last = i
    
    return True

def is_ordered(row : list[int]):
    ascending = row[0] < row[1]
    for i in range(1, len(row) - 1):
        if (row[i] < row[i+1]) != ascending:
            return False
        
    return True

valid = 0
for row in int_tokens:
    if appropriate_differ(row) and is_ordered(row):
        valid += 1

print(valid)

# Time to add problem dampener

newvalid = 0

def get_variants(row : list[int]) -> list[list[int]]:
    variants = []
    for i in range(0, len(row)):
        variant = []
        if i > 0:
            variant += row[:i]
        if i < len(row):
            variant += row[i+1:]

        variants += [ variant ]

    return variants

for row in int_tokens:
    if appropriate_differ(row) and is_ordered(row):
        newvalid += 1
        continue

    variants = get_variants(row)
    for variant in variants:
        if appropriate_differ(variant) and is_ordered(variant):
            newvalid += 1
            break

print(newvalid)
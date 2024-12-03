import re

import common.parser as parse

strings = parse.get_lines(3)

# We're looking for regexes which match mul\(([1-9][0-9]*|0),([1-9][0-9]*|0)\)
sum = 0
for string in strings:
    pairs = re.findall('mul\(([1-9][0-9]*|0),([1-9][0-9]*|0)\)', string)
    for pair in pairs:
        sum += int(pair[0]) * int(pair[1])

print(sum)

# Lets get rid of cases of all data between don't()s and do()
enabled = True
newstrings = []
for string in strings:
    current_string = string
    dont_pos = 0
    while True:
        if enabled:
            found_dont = re.search('don\'t\(\)', current_string)
            if found_dont != None:
                dont_pos = found_dont.start()
                enabled = False
            else:
                # Continue to next line, the rest of the line is safe
                break
        else:
            found_do = re.search('do\(\)', current_string[dont_pos:])
            if found_do != None:
                current_string = current_string[:dont_pos] + current_string[dont_pos+found_do.end():]
                enabled = True
            else:
                # We continue to be disabled, cull the rest of the line and move to next
                current_string = current_string[:dont_pos]
                break
    
    newstrings += [ current_string ]

newsum = 0

for string in newstrings:
    pairs = re.findall('mul\(([1-9][0-9]*|0),([1-9][0-9]*|0)\)', string)
    for pair in pairs:
        newsum += int(pair[0]) * int(pair[1])

print(newsum)

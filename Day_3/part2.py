import re

data = ''
with open('input.txt', 'r') as file:
    for line in file:
        data += line.strip() + ' '

valid_multipliers = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

processing = True
multiplied_sums = 0

for match in valid_multipliers:
    if "do()" in match:
        processing = True
    elif "don't()" in match:
        processing = False
    elif processing:
        a, b = map(int, re.findall(r"\d+", match))
        multiplied_sums += a * b

print("Multiplied sums:", multiplied_sums)

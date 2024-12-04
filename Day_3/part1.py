import re

data = []

with open('input.txt', 'r') as file:
    for line in file:
            data.append(line.strip())

# find all instances of mul(n,n) in the list
valid_multipliers = re.findall(r'mul\((\d+),(\d+)\)', str(data))

multiplied_sums = 0
#loop through the list of valid multipliers and multiply them
for i in valid_multipliers:
    a, b = map(int, i)
    multiplied_sums += a * b

print(multiplied_sums)
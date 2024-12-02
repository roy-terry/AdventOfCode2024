def day_one_part_one(file_path):
    list1 = []
    list2 = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                num1, num2 = map(int, line.split())
                list1.append(num1)
                list2.append(num2)

    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance


#print(day_one_part_one('input/day1/test.txt'))
print(day_one_part_one('input/day1/day1.txt'))
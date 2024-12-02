from collections import Counter

def calculate_similarity_score(list1, list2):
    counter = Counter(list2)
    similarity_score = sum(key * counter[key] for key in list1)

    return similarity_score

def day_one_part_two(file_path):
    list1 = []
    list2 = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                num1, num2 = map(int, line.split())
                list1.append(num1)
                list2.append(num2)

    return calculate_similarity_score(list1, list2)

#print(day_one_part_two('input/day1/test.txt'))
print(day_one_part_two('input/day1/day1.txt'))
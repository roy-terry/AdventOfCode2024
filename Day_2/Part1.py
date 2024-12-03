def day_two_part_one(file_path):
    reports = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                reports.append(list(map(int, line.split())))

    safe_count = 0
    for report in reports:
        is_descending = all(
            report[i] >= report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
            for i in range(len(report) - 1)
        )

        is_ascending = all(
            report[i] <= report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
            for i in range(len(report) - 1)
        )

        if is_descending or is_ascending:
            safe_count += 1

    print("Number of safe reports:", safe_count)
    return safe_count

day_two_part_one('../input/day2/input.txt')
def is_safe(report):
    is_descending = all(
        report[i] >= report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )

    is_ascending = all(
        report[i] <= report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )

    return is_descending or is_ascending

def is_safe_by_removing_one(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True

    return False

def day_two_part_two(file_path):
    reports = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                reports.append(list(map(int, line.split())))

    safe_count = 0
    for report in reports:
        if is_safe(report) or is_safe_by_removing_one(report):
            safe_count += 1

    print("Number of safe reports:", safe_count)
    return safe_count

day_two_part_two('../input/day2/input.txt')
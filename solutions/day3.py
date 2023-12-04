from collections import defaultdict

part_numbers = []
gears = defaultdict(list)

with open("inputs/day3.txt") as f:
    schema = [[char for char in line] for line in f.readlines()]
    for i, row in enumerate(schema):
        number, is_part, gear = "", False, None
        for j, char in enumerate(row):
            if char.isdigit():
                number += char
            else:
                if is_part:
                    part_numbers.append(int(number))
                    gears[gear].append(int(number))
                number, is_part, gear = "", False, None
                continue
            checks = []
            if i > 0:
                checks.append([i - 1, j])
                if j > 0:
                    checks.append([i - 1, j - 1])
                if j < len(schema[0]) - 1:
                    checks.append([i - 1, j + 1])
            if i < len(schema) - 1:
                checks.append([i + 1, j])
                if j > 0:
                    checks.append([i + 1, j - 1])
                if j < len(schema[0]) - 1:
                    checks.append([i + 1, j + 1])
            if j > 0:
                checks.append([i, j - 1])
            if j < len(schema[0]) - 1:
                checks.append([i, j + 1])
            for check in checks:
                if (not schema[check[0]][check[1]].isdigit()) and (
                    schema[check[0]][check[1]] not in [".", "\n"]
                ):
                    is_part = True
                    if schema[check[0]][check[1]] == "*":
                        gear = tuple(check)
                    break

print(sum([numbers[0] * numbers[1] for numbers in gears.values() if len(numbers) == 2]))

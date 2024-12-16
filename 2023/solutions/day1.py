import re

calibrations = []
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("inputs/day1.txt") as f:
    for line in f.readlines():
        positions = []
        for number, numeric in numbers.items():
            for m in re.finditer(number, line):
                positions.append((numeric, m.start()))
            for m in re.finditer(numeric, line):
                positions.append((numeric, m.start()))
        positions.sort(key=lambda position: position[1])
        calibrations.append(int(positions[0][0] + positions[-1][0]))

print(sum(calibrations))

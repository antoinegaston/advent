from collections import Counter

import numpy as np

with open("day2/test.txt") as file:
    input = [[int(num) for num in line.split(" ")] for line in file]

# part1
diff = [np.diff(level) for level in input]
increasing = [(level >= 1) & (level <= 3) for level in diff]
decreasing = [(level <= -1) & (level >= -3) for level in diff]
output = sum(map(all, increasing)) + sum(map(all, decreasing))

# part2
increasing_safe = 0
for i, level in enumerate(increasing):
    if np.False_ in level:
        index = list(level).index(np.False_)
        if Counter(level)[np.False_] == 1:
            if (index == 0) or (index == len(level) - 1):
                increasing_safe += 1
                continue
            else:
                interval = input[i][index + 1] - input[i][index - 1]
            if 1 <= interval <= 3:
                increasing_safe += 1
        elif (Counter(level)[np.False_] == 2) and (level[index + 1] == np.False_):
            if index == 0:
                interval = input[i][index + 2] - input[i][index]
            elif index == len(level) - 1:
                interval = input[i][index] - input[i][index - 2]
            else:
                interval = input[i][index + 1] - input[i][index - 1]
            if 1 <= interval <= 3:
                increasing_safe += 1


decreasing_safe = 0
for i, level in enumerate(decreasing):
    if np.False_ in level:
        index = list(level).index(np.False_)
        if Counter(level)[np.False_] == 1:
            if (index == 0) or (index == len(level) - 1):
                decreasing_safe += 1
                continue
            else:
                interval = input[i][index + 1] - input[i][index - 1]
            if -3 <= interval <= -1:
                decreasing_safe += 1
        elif (Counter(level)[np.False_] == 2) and (level[index + 1] == np.False_):
            if index == 0:
                interval = input[i][index + 2] - input[i][index]
            elif index == len(level) - 1:
                interval = input[i][index] - input[i][index - 2]
            else:
                interval = input[i][index + 1] - input[i][index - 1]
            if -3 <= interval <= -1:
                decreasing_safe += 1


print(output + increasing_safe + decreasing_safe)

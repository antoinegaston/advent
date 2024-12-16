from collections import Counter

import numpy as np

input = np.loadtxt("day1/input.csv", delimiter=",")

# part1
output = sum(abs(np.sort(input[:, 0]) - np.sort(input[:, 1])))

# part2
counter = Counter(input[:, 1])
output = sum([num * counter[num] for num in input[:, 0]])

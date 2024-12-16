import re

import numpy as np

with open("day3/input.txt") as file:
    input = file.read()

# part1
print(
    sum(
        [
            np.prod(
                list(map(int, match.removeprefix("mul(").removesuffix(")").split(",")))
            )
            for match in re.findall(r"mul\([0-9]+,[0-9]+\)", input)
        ]
    )
)

# part2
muls = [
    (
        np.prod(
            list(
                map(
                    int,
                    input[slice(*match.span(0))]
                    .removeprefix("mul(")
                    .removesuffix(")")
                    .split(","),
                )
            )
        ),
        match.start(0),
    )
    for match in re.finditer(r"mul\([0-9]+,[0-9]+\)", input)
]
dos = [(True, match.start(0)) for match in re.finditer(r"do\(\)", input)]
donts = [(False, match.start(0)) for match in re.finditer(r"don't\(\)", input)]
enabled = True
total = 0
for element in sorted(muls + dos + donts, key=lambda x: x[1]):
    if isinstance(element[0], bool):
        enabled = element[0]
    else:
        if enabled:
            total += element[0]
print(total)

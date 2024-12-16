def get_neighbors(
    seed: tuple[int, int], value: int, map: dict[tuple[int, int], int]
) -> set[tuple[int, int]]:
    return {
        position
        for position in [
            (seed[0] - 1, seed[1]),
            (seed[0] + 1, seed[1]),
            (seed[0], seed[1] - 1),
            (seed[0], seed[1] + 1),
        ]
        if (position in map) and (map[position] == value + 1)
    }


def iterate(
    seed: tuple[int, int],
    value: int,
    map: dict[tuple[int, int], int],
) -> None:
    global count
    if value < 9:
        neighbors = get_neighbors(seed, value, map)
        for neighbor in neighbors:
            iterate(neighbor, map[neighbor], map)
    else:
        count += 1


if __name__ == "__main__":
    with open("day10/input.txt") as file:
        input = {
            (i, j): int(value) if value != "." else 10
            for i, line in enumerate(file.readlines())
            for j, value in enumerate(line.removesuffix("\n"))
        }

    seeds = {position for position, value in input.items() if value == 0}
    score = 0
    while seeds:
        seed = seeds.pop()
        value = 0
        count = 0
        iterate(seed, value, input)
        score += count
    print(score)

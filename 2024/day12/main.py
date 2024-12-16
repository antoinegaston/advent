def get_neighbors(
    seed: tuple[int, int], value: str, to_explore: dict[tuple[int, int], str]
) -> set[tuple[int, int]]:
    return {
        position
        for position in [
            (seed[0] - 1, seed[1]),
            (seed[0] + 1, seed[1]),
            (seed[0], seed[1] - 1),
            (seed[0], seed[1] + 1),
        ]
        if (position in to_explore) and (to_explore[position] == value)
    }


def get_limits(
    seed: tuple[int, int], value: str, to_explore: dict[tuple[int, int], str]
) -> set[tuple[int, int, str]]:
    return {
        (seed[0], seed[1], direction)
        for position, direction in {
            (seed[0] - 1, seed[1]): "T",
            (seed[0] + 1, seed[1]): "B",
            (seed[0], seed[1] - 1): "L",
            (seed[0], seed[1] + 1): "R",
        }.items()
        if (position not in to_explore) or (to_explore[position] != value)
    }


def compute_perimeter(limits: set[tuple[int, int, str]]) -> int:
    perimeter = 0
    while limits:
        i, j, value = limits.pop()
        perimeter += 1
        if value in {"T", "B"}:
            left_offset = 1
            right_offset = 1
            while (neighbor := (i, j - left_offset, value)) in limits:
                left_offset += 1
                limits.remove(neighbor)
            while (neighbor := (i, j + right_offset, value)) in limits:
                right_offset += 1
                limits.remove(neighbor)
        elif value in {"L", "R"}:
            top_offset = 1
            bottom_offset = 1
            while (neighbor := (i - top_offset, j, value)) in limits:
                top_offset += 1
                limits.remove(neighbor)
            while (neighbor := (i + bottom_offset, j, value)) in limits:
                bottom_offset += 1
                limits.remove(neighbor)
    return perimeter


if __name__ == "__main__":
    with open("day12/input.txt") as file:
        input = [line.removesuffix("\n") for line in file.readlines()]
    all_cells = {
        (i, j): value for i, row in enumerate(input) for j, value in enumerate(row)
    }
    to_explore = all_cells.copy()
    price = 0
    while to_explore:
        seed, value = to_explore.popitem()
        neighbors = get_neighbors(seed, value, to_explore)
        limits = get_limits(seed, value, to_explore)
        exploring = neighbors.copy()
        explored = {seed}
        while exploring:
            seed = exploring.pop()
            neighbors = get_neighbors(seed, value, all_cells)
            limits |= get_limits(seed, value, all_cells)
            exploring = exploring.union(neighbors) - explored
            explored.add(seed)
        to_explore = {
            key: value for key, value in to_explore.items() if key not in explored
        }
        area = len(explored)
        perimeter = compute_perimeter(limits)
        price += area * perimeter
    print(price)

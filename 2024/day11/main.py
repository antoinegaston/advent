from collections import defaultdict

known_iterations = {0: 1}


def iterate(stone: int) -> int | tuple[int, int]:
    """
    - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    if stone in known_iterations:
        return known_iterations[stone]
    elif len(str(stone)) % 2 == 0:
        left = int(str(stone)[: len(str(stone)) // 2])
        right = int(str(stone)[len(str(stone)) // 2 :])
        known_iterations[stone] = (left, right)
        return left, right
    else:
        new_stone = stone * 2024
        known_iterations[stone] = new_stone
        return new_stone


def blink(stones: dict[int, int]) -> list[int]:
    new_stones = stones.copy()
    for stone, count in stones.items():
        iteration = iterate(stone)
        if isinstance(iteration, int):
            new_stones[iteration] += count
        else:
            for result in iteration:
                new_stones[result] += count
        new_stones[stone] -= count
    return new_stones


def main(input: list[int], nb_iterations: int) -> tuple[list[int], list[int]]:
    stones = defaultdict(int)
    for stone in input:
        stones[stone] = 1
    for _ in range(nb_iterations):
        stones = blink(stones)
    return sum(stones.values())


if __name__ == "__main__":
    with open("day11/test.txt") as file:
        input = list(map(int, file.read().split(" ")))
    print(main(input, 75))

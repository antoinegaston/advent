import re
import numpy as np

# part1
cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
possible_games = set()

with open("inputs/day2.txt") as f:
    for i, game in enumerate(f.readlines()):
        possible_games.add(i + 1)
        for cube_set in game.removeprefix(f"Game {i+1}:").split(";"):
            if i + 1 in possible_games:
                for cube_draw in cube_set.split(","):
                    number = "".join(re.findall(r"\d+", cube_draw))
                    color = re.findall("[A-z]+", cube_draw).pop()
                    if int(number) > cubes[color]:
                        possible_games.remove(i + 1)
                        break

print(sum(possible_games))

# part2
powers = []

with open("inputs/day2.txt") as f:
    for i, game in enumerate(f.readlines()):
        mini_nb_cubes = {"red": 0, "green": 0, "blue": 0}
        for cube_set in game.removeprefix(f"Game {i+1}:").split(";"):
            for cube_draw in cube_set.split(","):
                number = "".join(re.findall(r"\d+", cube_draw))
                color = re.findall("[A-z]+", cube_draw).pop()
                if mini_nb_cubes[color] < int(number):
                    mini_nb_cubes[color] = int(number)
        powers.append(np.prod(list(mini_nb_cubes.values())))

print(sum(powers))

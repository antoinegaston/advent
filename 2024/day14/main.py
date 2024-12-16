import re
from collections import defaultdict

import numpy as np
from pydantic import BaseModel


class Robot(BaseModel):
    position: tuple[int, int]
    velocity: tuple[int, int]

    @classmethod
    def from_tuple(cls, data: list[str]) -> "Robot":
        return cls(
            position=(data[0], data[1]),
            velocity=(data[2], data[3]),
        )


class Map(BaseModel):
    height: int
    width: int
    robots: list[Robot]

    @property
    def robots_dict(self) -> dict[tuple[int, int], list[Robot]]:
        robots = defaultdict(list)
        for robot in self.robots:
            robots[robot.position].append(robot)
        return robots

    def iterate(self) -> None:
        for robot in self.robots:
            x, y = robot.position
            dx, dy = robot.velocity
            robot.position = ((x + dx) % self.width, (y + dy) % self.height)

    def plot(self) -> str:
        robots = self.robots_dict
        return "\n".join(
            [
                "".join(
                    [
                        str(len(robots[x, y])) if (x, y) in robots else "."
                        for x in range(self.width)
                    ]
                )
                for y in range(self.height)
            ]
        )

    @property
    def quadrant_height(self) -> int:
        return int(self.height / 2)

    @property
    def quadrant_width(self) -> int:
        return int(self.width / 2)

    def quadrants(self) -> tuple[list[Robot], list[Robot], list[Robot], list[Robot]]:
        top_left = []
        top_right = []
        bottom_left = []
        bottom_right = []
        for robot in self.robots:
            x, y = robot.position
            if x < self.quadrant_width:
                if y < self.quadrant_height:
                    top_left.append(robot)
                elif y >= self.height % 2 + self.quadrant_height:
                    bottom_left.append(robot)
            elif x >= self.width % 2 + self.quadrant_width:
                if y < self.quadrant_height:
                    top_right.append(robot)
                elif y >= self.height % 2 + self.quadrant_height:
                    bottom_right.append(robot)
        return len(top_left), len(top_right), len(bottom_left), len(bottom_right)

    def compute_entropy(self) -> int:
        robots = self.robots_dict
        return sum(
            [
                sum(
                    np.abs(
                        np.diff(
                            [
                                len(robots[x, y]) if (x, y) in robots else 0
                                for x in range(self.width)
                            ]
                        )
                    )
                )
                for y in range(self.height)
            ]
        )


if __name__ == "__main__":
    with open("day14/input.txt") as file:
        map = Map(
            width=101,
            height=103,
            robots=[
                Robot.from_tuple(re.findall(r"-?\d+", line))
                for line in file.readlines()
            ],
        )
    for i in range(100000):
        map.iterate()
        entropy = map.compute_entropy()
        if entropy < 800:
            print(i, map.plot())

import re

from pydantic import BaseModel


class Prize(BaseModel):
    x: int
    y: int

    @classmethod
    def from_str(cls, string: str, offset: int = 0):
        x, y = re.findall(r"\d+", string)
        return cls(x=int(x) + offset, y=int(y) + offset)


class Button(BaseModel):
    cost: int
    x: int
    y: int

    @classmethod
    def from_str(cls, string: str, cost: int):
        x, y = re.findall(r"\d+", string)
        return cls(cost=cost, x=x, y=y)


class Machine(BaseModel):
    A: Button
    B: Button
    prize: Prize

    @classmethod
    def from_str(cls, string: str, offset: int = 0):
        A, B, prize = string.split("\n")
        A = Button.from_str(A, cost=3)
        B = Button.from_str(B, cost=1)
        prize = Prize.from_str(prize, offset=offset)
        return cls(A=A, B=B, prize=prize)

    @property
    def B_tokens(self) -> float:
        return (self.prize.x * self.A.y - self.prize.y * self.A.x) / (
            self.B.x * self.A.y - self.B.y * self.A.x
        )

    @property
    def A_tokens(self) -> float:
        return (self.prize.x - self.B.x * self.B_tokens) / self.A.x

    @property
    def is_winnable(self) -> bool:
        return self.A_tokens % 1 == 0 and self.B_tokens % 1 == 0

    @property
    def cost(self) -> int | None:
        if self.is_winnable:
            return self.A.cost * self.A_tokens + self.B.cost * self.B_tokens
        return None


if __name__ == "__main__":
    with open("day13/input.txt") as file:
        machines = [
            Machine.from_str(machine, offset=10000000000000)
            for machine in file.read().removesuffix("\n").split("\n\n")
        ]
    print(sum(machine.cost for machine in machines if machine.is_winnable))

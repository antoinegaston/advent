cards = {}


with open("inputs/day4.txt") as f:
    for i, line in enumerate(f.readlines()):
        if i + 1 in cards:
            cards[i + 1] += 1
        else:
            cards[i + 1] = 1
        guessed = 0
        cleaned_line = (
            line.replace("Card", "").replace(f"{i+1}:", "").removesuffix("\n")
        )
        winning, hand = cleaned_line.split("|")
        winning = {int(number) for number in winning.split(" ") if number != ""}
        hand = {int(number) for number in hand.split(" ") if number != ""}
        for number in winning:
            if number in hand:
                guessed += 1
        if guessed > 0:
            for index in range(guessed):
                if i + 1 + index + 1 in cards:
                    cards[i + 1 + index + 1] += cards[i + 1] * 1
                else:
                    cards[i + 1 + index + 1] = cards[i + 1] * 1


print(sum(cards.values()))

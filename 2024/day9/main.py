if __name__ == "__main__":
    with open("day9/test.txt") as file:
        input = file.read().removesuffix("\n")
    blocks = []
    for i, char in enumerate(input):
        if i % 2 == 0:
            blocks.append((i, str(i // 2) * int(char)))
        else:
            if int(char) > 0:
                blocks.append((i, "." * int(char)))
    reversed_blocks = [(i, block) for (i, block) in blocks if "." not in block][::-1]
    reordered_blocks = []
    for i, (_, block) in enumerate(blocks):
        print(i, block)
        if "." in block:
            for j, (k, moving_block) in enumerate(reversed_blocks):
                if (diff := len(block) - len(moving_block)) >= 0:
                    reordered_blocks.append(moving_block)
                    if diff > 0:
                        blocks.insert(i + 1, (i + 1, "." * diff))
                    reversed_blocks.pop(j)
                    blocks.remove((k, moving_block))
                    break
            if j == len(reversed_blocks) - 1:
                reordered_blocks.append(block)
        else:
            reordered_blocks.append(block)
    print(reordered_blocks)

with open("day4/test.txt") as file:
    input = [line.removesuffix("\n") for line in file.readlines()]

# part1
xmas = "XMAS"
count = {}
for i, line in enumerate(input):
    for j, char in enumerate(line):
        for word in [xmas, xmas[::-1]]:  # forward and backward
            index = word.index(char)

            # horizontal
            temp = {(i, j)}
            for k in range(index):
                if j - k < 0:
                    break
                if input[i][j - k] == word[index - k]:
                    temp.add((i, j - k))
            for k in range(len(word) - 1 - index):
                if j + k >= len(input[i]):
                    break
                if input[i][j + k] == word[index + k]:
                    temp.add((i, j + k))
            if len(temp) == len(word):
                count[frozenset(temp)] = True

            # # vertical
            # temp = set()
            # drop = False
            # for k in range(index):
            #     if input[i - k][j] != word[index - k]:
            #         drop = True
            #         break
            #     else:
            #         temp.add((i - k, j))
            # for k in range(len(word) - 1 - index):
            #     if input[i + k][j] != word[index + k]:
            #         drop = True
            #         break
            #     else:
            #         temp.add((i + k, j))
            # if not drop:
            #     count[temp] = True

            # # diagonal
            # temp = set()
            # drop = False
            # for k in range(index):
            #     if input[i - k][j - k] != word[index - k]:
            #         drop = True
            #         break
            #     else:
            #         temp.add((i - k, j - k))
            # for k in range(len(word) - 1 - index):
            #     if input[i + k][j + k] != word[index + k]:
            #         drop = True
            #         break
            #     else:
            #         temp.add((i + k, j + k))
            # if not drop:
            #     count[temp] = True
print(count)

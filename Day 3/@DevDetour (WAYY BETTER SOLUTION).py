def main():
    with open("input.txt", "r") as f:
        lines = [i.strip().__add__(".") for i in f.readlines()]

    maxR = len(lines)
    maxC = len(lines[0])
    nums = "1234567890"

    def isAdjacent(r, c, lines):
        dirs = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
            [1, 1]
        ]

        for d in dirs:
            newR = r + d[0]
            newC = c + d[1]
            if 0 <= newR < maxR and 0 <= newC < maxC and lines[newR][newC] not in nums and lines[newR][newC] != ".":
                return True
        return False

    total = 0
    currNum = ""
    numAdjacent = False
    for r in range(maxR):
        for c in range(maxC):
            if lines[r][c] in nums:
                currNum += lines[r][c]
                numAdjacent = numAdjacent or isAdjacent(r, c, lines)
            else:
                if numAdjacent:
                    total += int(currNum)
                currNum = ""
                numAdjacent = False
    print(total)

if __name__ == "__main__":
    main()
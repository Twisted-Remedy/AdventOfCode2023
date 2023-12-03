def main():
    with open("input.txt", "r") as f:
        lines = [i.strip().split(":")[1][1:] for i in f]

    total_sum = 0
    for idx, x in enumerate(lines):
        handfuls = x.split(";")
        max_cubes = {"red": 0,
                     "green": 0,
                     "blue": 0}

        for h in handfuls:
            cubes = h.split(",")

            for c in cubes:
                c = c.strip()
                num = int(c.split(" ")[0])
                colour = c.split(" ")[1]
                if max_cubes[colour] < num:
                    max_cubes[colour] = num

        total_sum += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
    print(total_sum)
if __name__ == "__main__":
    main()
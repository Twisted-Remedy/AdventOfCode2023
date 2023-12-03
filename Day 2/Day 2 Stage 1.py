def main():
    with open("input.txt", "r") as f:
        lines = [i.strip().split(":")[1][1:] for i in f]

    game_id_sum = 0
    max_red = 12
    max_green = 13
    max_blue = 14

    for idx, x in enumerate(lines):
        handfuls = x.split(";")
        valid = True
        for h in handfuls:
            current_cubes = {"red": 0,
                             "green": 0,
                             "blue": 0}
            cubes = h.split(",")

            for c in cubes:
                c = c.strip()
                num = int(c.split(" ")[0])
                colour = c.split(" ")[1]
                current_cubes[colour] += num

            if current_cubes.get('red', 0) > max_red:
                valid = False
                continue
            if current_cubes.get('green', 0) > max_green:
                valid = False
                continue
            if current_cubes.get('blue', 0) > max_blue:
                valid = False
                continue

        if valid:
            game_id_sum += (idx+1)
    print(game_id_sum)
if __name__ == "__main__":
    main()
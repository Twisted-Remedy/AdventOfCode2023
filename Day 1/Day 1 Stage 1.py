def main():
    total = 0
    with open("input.txt", "r")as f:
        for i in f:
            line_content = i.strip()
            line_numbers = [c for c in line_content if c.isnumeric()]
            total += int(line_numbers[0] + line_numbers[-1])
    print(total)

if __name__ == "__main__":
    main()
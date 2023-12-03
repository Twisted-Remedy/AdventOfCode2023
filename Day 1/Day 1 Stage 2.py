digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def main():
    total = 0
    with open("input.txt", "r")as f:
        for i in f:
            line_content = i.strip()
            line_numbers = [c for c in translate(line_content) if c.isnumeric()]
            total += int(line_numbers[0] + line_numbers[-1])
    print(total)

def translate(line: str):
    for num, name in enumerate(digit_names):
        line = line.replace(name, f"{name}{num}{name}")
    return line

if __name__ == "__main__":
    main()
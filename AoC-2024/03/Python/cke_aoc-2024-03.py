import re

PATTERN = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

def find_matches(line):
    matches = re.finditer(PATTERN, line)
    return [match.group(1) + "," + match.group(2) for match in matches]

def calc_sum(found_muls):
    line_sum = 0
    for mul in found_muls:
        numbers = mul.split(",")
        line_sum += int(numbers[0]) * int(numbers[1])
    return line_sum

def main():
    print("Advent of Code 2024 - cke - day 3")

    with open("../input.txt") as f:
        lines = f.readlines()

        total_sum = 0

        for line in lines:
            found_muls=find_matches(line)
            total_sum += calc_sum(found_muls)

        print("Total sum: ", total_sum)

if __name__ == "__main__":
    main()
import re

PATTERN = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
DO_PATTERN = r"do\(\)"
DONT_PATTERN = r"don't\(\)"

def find_ctrl_positions(line):
    """Find positions of do( and don't( controls"""
    do_pos = [match.start() for match in re.finditer(DO_PATTERN, line)]
    dont_pos = [match.start() for match in re.finditer(DONT_PATTERN, line)]
    return do_pos, dont_pos

def find_mul_matches(line):
    """Find all mul patterns with their positions"""
    matches = re.finditer(PATTERN, line)
    return [(match.start(), match.group(1) + "," + match.group(2)) for match in matches]

def validate_match_position(match_pos, do_positions, dont_positions):
    """Check if match is valid based on control positions"""
    valid_do = any(do_pos < match_pos for do_pos in do_positions)
    invalid_dont = any(do_pos < dont_pos < match_pos 
                      for do_pos in do_positions 
                      for dont_pos in dont_positions)
    print(f"valid_do: {valid_do}, invalid_dont: {invalid_dont}")
    return valid_do and not invalid_dont

def find_matches(line):
    """Find valid mul matches based on control positions"""
    mul_matches = find_mul_matches(line)
    do_pos, dont_pos = find_ctrl_positions(line)
    
    valid_matches = []
    for pos, match in mul_matches:
        recent_do = max([p for p in do_pos if p < pos] + [-1])
        recent_dont = max([p for p in dont_pos if p < pos] + [-1])
        
        if recent_do > recent_dont or (recent_do == -1 and recent_dont == -1):
            valid_matches.append(match)
    
    return valid_matches

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
            matches=find_matches(line)
            total_sum += calc_sum(matches)

        print("Total sum: ", total_sum)

if __name__ == "__main__":
    main()
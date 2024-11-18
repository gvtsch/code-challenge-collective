import re

SPECIAL_CHARACTERS = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
PART_1 = False
PART_2 = True

def is_symbol(symbols):
    for symbol in symbols:
        for char in symbol:
            if char in SPECIAL_CHARACTERS:
                return True
    return False

def check_for_numbers(parts, position):

    pass

def check_for_parts(parts, idx):
    zahl = 0
    
    if len(parts) == 3:
        matches = re.finditer(r'\d+', parts[1])
        positions = [(match.start(), match.end()-1) for match in matches]
        if not positions:
            print("No numbers found")
            return 0

        for position in positions:
            symbol = [
                parts[0][max(0,position[0]-1):min(position[1]+2, len(parts[0])-1)],
                parts[1][max(0,position[0]-1)],
                parts[1][min(position[1]+1, len(parts[1])-1)],
                parts[2][max(0,position[0]-1):min(position[1]+2, len(parts[0])-1)]
            ]

            if is_symbol(symbol):
                zahl += int(parts[1][position[0]:position[1]+1])

    elif len(parts) == 2:
        part = parts[idx]
        matches = re.finditer(r'\d+', part)
        positions = [(match.start(), match.end()-1) for match in matches]

        for position in positions:
            if idx == 0:
                symbol = [
                    parts[0][max(0,position[0]-1)],
                    parts[0][min(position[1]+2,len(parts[0])-1)],
                    parts[1][max(0,position[0]-1):min(position[1]+2, len(parts[0])-1)]
                ]

            else:
                symbol = [
                    parts[1][max(0, position[0]-1)],
                    parts[1][min(position[1]+1, len(parts[0])-1)],
                    parts[0][max(0, position[0]-1):min(position[1]+2, len(parts[1]))]
                ]
                        
            if is_symbol(symbol):
                zahl += int(part[position[0]:position[1]+1])
                   
    else:
        print("Unexpected number of lines in parts")

    return zahl

def find_gear(parts, idx):
    print(f"Parts: {parts}")

    if len(parts) == 3:
        matches = re.finditer(r'\*', parts[1])
        positions = [match.start() for match in matches]
        if positions:
            position = positions[0]
            check_for_numbers(parts, position)

    elif len(parts) == 2:
        part = parts[idx]
        matches = re.finditer(r'\*', part)
        positions = [(match.start(), match.end()-1) for match in matches]
        print(f"Positions: {positions}")


def main():
    lines = []
    filename = "../input_short.txt"
    total_sum = 0

    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        i = 0
        while i < len(lines):
            print(f"Line {i}: {lines[i]}")
            if i == 0:
                idx = 0
                parts = lines[i:i+2]
                if PART_1:
                    total_sum += check_for_parts(parts, idx)
                if PART_2:
                    find_gear(parts, idx)
                i += 1
            elif i == len(lines) - 1:
                idx = 1
                parts = lines[i-1:i+1]
                if PART_1:
                    total_sum += check_for_parts(parts, idx)
                if PART_2:
                    find_gear(parts, idx)
                i += 1
            else:
                parts = lines[i-1:i+2]
                if PART_1:
                    total_sum += check_for_parts(parts, idx)
                if PART_2:
                    find_gear(parts, idx)
                i += 1
            
            
        print(total_sum)
           
if __name__ == "__main__":
    main()
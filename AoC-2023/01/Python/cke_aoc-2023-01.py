def change_char_to_digit(line):
    char_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    digits = []
    for i in range(len(line)):
        for word, digit in char_to_digit.items():
            if line[i:].startswith(word):
                digits.append(digit)
        if line[i].isdigit():
            digits.append(line[i])
    return ''.join(digits)

def main():
    # read in the file "input.txt" and print out the first line
    with open("input.txt") as file:
        calibration = []
        for line in file:
            line = change_char_to_digit(line)
            print(line)
            for char in line:
                if char.isdigit():
                    first = char
                    break
            for char in reversed(line):
                if char.isdigit():
                    last = char
                    break
            print(f"Calibration: {first} + {last}")
            calibration.append(first + last)

    print(f"Sum of calibrations: {sum(map(int, calibration))}")

if __name__ == "__main__":
    main()
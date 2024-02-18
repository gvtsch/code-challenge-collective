# read in the file "input.txt" and print out the first line
with open("input.txt") as file:
    calibration = []
    for line in file:

        for char in line:
            if char.isdigit():
                first = char
                break
        for char in reversed(line):
            if char.isdigit():
                last = char
                break
        calibration.append(first + last)

print(f"Sum of calibrations: {sum(map(int, calibration))}")

PATTERNS = ["XMAS", "SAMX"]

def find_horizontal_patterns(lines):
    cnt=0
    for line in lines:
        for pattern in PATTERNS:
            start = 0
            while start < len(line):
                pos = line.find(pattern, start)
                if pos == -1:
                    break
                #print(f"Found pattern '{pattern}' in line: {line} at position {pos}")
                start = pos + 1
                cnt+=1
    return cnt

def find_vertical_patterns(lines):
    cnt=0
    for i in range(len(lines[0])):
        column = "".join([line[i] for line in lines])
        for pattern in PATTERNS:
            start = 0
            while start < len(column):
                pos = column.find(pattern, start)
                if pos == -1:
                    break
                #print(f"Found pattern '{pattern}' in column: {column} at position {pos}")
                start = pos + 1
                cnt+=1
    return cnt

def find_diagonal_patterns(lines):
    cnt=0
    num_rows = len(lines)
    num_cols = len(lines[0])

    # Check diagonals from top-left to bottom-right
    for diag in range(num_rows + num_cols - 1):
        diagonal = []
        for row in range(max(0, diag - num_cols + 1), min(num_rows, diag + 1)):
            col = diag - row
            diagonal.append(lines[row][col])
        diagonal = "".join(diagonal)
        for pattern in PATTERNS:
            start = 0
            while start < len(diagonal):
                pos = diagonal.find(pattern, start)
                if pos == -1:
                    break
                #print(f"Found pattern '{pattern}' in diagonal: {diagonal} at position {pos}")
                start = pos + 1
                cnt+=1

    # Check diagonals from top-right to bottom-left
    for diag in range(num_rows + num_cols - 1):
        diagonal = []
        for row in range(max(0, diag - num_cols + 1), min(num_rows, diag + 1)):
            col = num_cols - 1 - (diag - row)
            diagonal.append(lines[row][col])
        diagonal = "".join(diagonal)
        for pattern in PATTERNS:
            start = 0
            while start < len(diagonal):
                pos = diagonal.find(pattern, start)
                if pos == -1:
                    break
                #print(f"Found pattern '{pattern}' in diagonal: {diagonal} at position {pos}")
                start = pos + 1
                cnt+=1
    return cnt

def find_x_mas(lines):
    grid = [list(line) for line in lines]
    cnt = 0

    patterns = [
        ('M', 'S', 'A', 'M', 'S'),
        ('S', 'S', 'A', 'M', 'M'),
        ('M', 'M', 'A', 'S', 'S'),
        ('S', 'M', 'A', 'S', 'M')
    ]

    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            for i, (c1, c2, c3, c4, c5) in enumerate(patterns):
                if (grid[row][col] == c1 and grid[row][col + 2] == c2 and
                    grid[row + 1][col + 1] == c3 and
                    grid[row + 2][col] == c4 and grid[row + 2][col + 2] == c5):
                    cnt+=1
    return cnt

def main():
    print("Advent of Code 2024 - cke - day 4")

    with open("../input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        
        amount = 0

        if all(len(line) == len(lines[0]) for line in lines):
            amount+=find_horizontal_patterns(lines)
            amount+=find_vertical_patterns(lines)
            amount+=find_diagonal_patterns(lines)
            print(f"Found {amount} patterns.")

            amount_x_mas=find_x_mas(lines)
            print(f"Found {amount_x_mas} X-MAS patterns")

        else:
            print("Lines are of different lengths.")
        

if __name__ == "__main__":
    main()
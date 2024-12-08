
PATTERNS = ["XMAS", "SAMX"]

def find_horizontal_patterns(lines):
    """
    Einfach die Patterns suchen und hochzählen.
    """
    pass

def find_vertical_patterns(lines):
    """
    Die Patterns in den Spalten suchen. Dazu das grid drehen.
    """
    pass

def find_diagonal_patterns(lines):
    """
    Die Patterns in den Diagonalen suchen.
    Wenn ich das richtig verstehe, dann kann ich die Lines aneinander hängen 
    und dann die Patterns mit entsprechenden Schritten suchen.
    """
    pass

def main():
    print("Advent of Code 2024 - cke - day 4")

    with open("../input_short.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        

        if all(len(line) == len(lines[0]) for line in lines):
            print(lines)

        else:
            print("Lines are of different lengths.")
        

if __name__ == "__main__":
    main()
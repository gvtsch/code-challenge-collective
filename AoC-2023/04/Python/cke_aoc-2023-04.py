def check_win_amount(line): 
    line = [x for x in line.strip().split(" ")[2:] if x]
    pipe_index = line.index('|')
    lose = line[:pipe_index]
    gewinne = line[pipe_index+1:]
    n = sum(1 for los in lose if los in gewinne)
    return n if 'n' in locals() else 0

def calc_sum(n):
    los_sum = 1
    for i in range(n-1):
        los_sum *= 2
    return los_sum

def main():
    print("Hello, Advent of Code 2023 - Day 4!")

    with open("../input.txt", 'r') as file:
        lines = file.readlines()

        total_sum = 0

        for line in lines:

            amount = check_win_amount(line)
            if amount != 0:
                total_sum += calc_sum(amount)

        print(total_sum)


if __name__ == "__main__":
    main()
PART_2 = True
PART_1 = True

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

def process_cards(lines):
    card_counts = {i: 1 for i in range(len(lines))}
    
    for idx, line in enumerate(lines):
        matches = check_win_amount(line)
        current_copies = card_counts[idx]
        
        for j in range(matches):
            next_card = idx + j + 1
            if next_card < len(lines):
                card_counts[next_card] += current_copies
    
    return sum(card_counts.values())

def main():
    print("Hello, Advent of Code 2023 - Day 4!")

    with open("../input.txt", 'r') as file:
        lines = file.readlines()
        total_sum = 0

        if PART_1:
            for line in lines:
                amount = check_win_amount(line)
                if amount != 0:
                    total_sum += calc_sum(amount)
            print(f"Part 1 Total: {total_sum}")
            
        if PART_2:
            total_cards = process_cards(lines)
            print(f"Part 2 Total Cards: {total_cards}")


if __name__ == "__main__":
    main()
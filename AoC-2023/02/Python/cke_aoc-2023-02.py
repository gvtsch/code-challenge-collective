def possible_game_check(sub_parts):
    for sub_part in sub_parts:
        parts = sub_part.split(',')
        for part in parts:
            quantity, color = part.split()
            quantity = int(quantity)
            if (color == 'red' and quantity > 12) or \
               (color == 'blue' and quantity > 14) or \
               (color == 'green' and quantity > 13):
                return False
    return True

def fewest_possible_balls(sub_parts):
    color_lists = {'red': [], 'blue': [], 'green': []}
    for sub_part in sub_parts:
        parts = sub_part.split(',')
        for part in parts:
            quantity, color = part.split()
            quantity = int(quantity)
            if color in color_lists:
                color_lists[color].append(quantity)
    
    min_balls = {color: max(color_lists[color]) if color_lists[color] else 0 for color in color_lists}
    multiplied_values = 1

    print(min_balls)

    for value in min_balls.values():
        multiplied_values *= value

    return multiplied_values
            

def main():
    with open("../input.txt", 'r') as file:
        lines = file.readlines()

    game_sum = sum(range(1, 101))
    fewest_balls_game_sum = 0

    for line in lines:
        game_no, sub_parts = line.strip().split(':', 1)
        game_no = int(game_no.split()[1])
        sub_parts = sub_parts.split(';')

        if not possible_game_check(sub_parts):
           game_sum -= game_no

        fewest_balls_game_sum += fewest_possible_balls(sub_parts)

    print(game_sum)
    print(fewest_balls_game_sum)

if __name__ == "__main__":
    main()
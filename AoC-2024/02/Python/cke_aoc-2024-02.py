def is_monotonic(sequence):
    is_increasing = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
    is_decreasing = all(sequence[i] >= sequence[i+1] for i in range(len(sequence)-1))
    return is_increasing or is_decreasing

def is_distance_valid(sequence):
    distances = [abs(int(sequence[i]) - int(sequence[i+1])) for i in range(len(sequence)-1)]
    return all((distance <= 3 and distance >= 1) for distance in distances)

def check_sequence_with_one_removal(sequence):
    if is_monotonic(sequence) and is_distance_valid(sequence):
        return True
        
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i+1:] # Das Element an der Stelle i wird entfernt und quasi jede Kombination wird getestet
        if is_monotonic(modified_sequence) and is_distance_valid(modified_sequence):
            return True
            
    return False

def main():
    print("Hello, Advent of Code 2024 - Day 2!")
    
    with open("../input.txt", 'r') as file:
        lines = file.readlines()
        safe_reports_number = 0

        for line in lines:
            line = list(map(int, line.split()))
            if check_sequence_with_one_removal(line):
                safe_reports_number += 1
                
        print(safe_reports_number)    

if __name__ == "__main__":
    main()
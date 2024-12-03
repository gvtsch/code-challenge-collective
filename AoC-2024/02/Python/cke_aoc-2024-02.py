
def check_monotonic(sequence):
    is_increasing = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
    is_decreasing = all(sequence[i] >= sequence[i+1] for i in range(len(sequence)-1))
    return is_increasing or is_decreasing

def check_distance(sequence):
    distances = [abs(int(sequence[i]) - int(sequence[i+1])) for i in range(len(sequence)-1)]
    if all((distance <= 3 and distance >= 1) for distance in distances):
        return True


def main():
    print("Hello, Advent of Code 2024 - Day 2!")
    
    with open("../input.txt", 'r') as file:
        lines = file.readlines()

        safe_reports_number = 0

        for line in lines:
            line = list(map(int, line.split()))
            if check_monotonic(line):
                if check_distance(line):
                    safe_reports_number += 1
                
        print(safe_reports_number)    
        

if __name__ == "__main__":
    main()
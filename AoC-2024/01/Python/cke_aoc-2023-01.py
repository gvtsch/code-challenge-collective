
def sort_column(lines):
    first_entries, second_entries = [], []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            first_entries.append(int(parts[0]))
            second_entries.append(int(parts[1]))
    return first_entries, second_entries

def calc_dist(first_entries, second_entries):
    dist = 0
    for i in range(len(first_entries)):
        dist += abs(first_entries[i] - second_entries[i])
    return dist

def find_appeareances(first_entries, second_entries):
    appeareances = []
    for number in first_entries:
        second_entries.count(number)
        appeareances.append(second_entries.count(number))
    return appeareances

def calc_similarity(first_entries, appeareances):
    similarity_score = 0
    for i in range(len(first_entries)):
        similarity_score += appeareances[i] * first_entries[i]
    return similarity_score

def main():
    print("Hello, Advent of Code 2024 - Day 1!")

    with open("../input.txt", 'r') as file:
        lines = file.readlines()

    first_entries, second_entries = sort_column(lines)
    distance = calc_dist(sorted(first_entries), sorted(second_entries))
    appeareances = find_appeareances(first_entries, second_entries)
    similarity_score = calc_similarity(first_entries, appeareances)
    
    print(f"Distance: {distance}")
    print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()
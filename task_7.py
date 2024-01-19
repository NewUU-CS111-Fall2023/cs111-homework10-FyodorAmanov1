from collections import Counter

def min_rabbits(answers):
    # Count the occurrences of each answer
    answer_counts = Counter(answers)

    # Calculate the minimum number of rabbits in the forest
    total_rabbits = 0
    for answer, count in answer_counts.items():
        # Calculate the number of cliques with size (answer + 1)
        cliques = (count + answer) // (answer + 1)
        # Calculate the total number of rabbits in these cliques
        total_rabbits += cliques * (answer + 1)

    return total_rabbits

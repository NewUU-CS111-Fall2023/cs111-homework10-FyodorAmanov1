import random

def generate_random_3sat_formula(num_variables, num_clauses):
    if num_variables <= 0 or num_clauses <= 0 or num_variables % 3 != 0:
        raise ValueError("Invalid input. Number of variables should be a multiple of 3, and both should be positive.")

    formula = []
    variables = list(range(1, num_variables + 1))

    for _ in range(num_clauses):
        # Randomly select three distinct variables for each clause
        clause = random.sample(variables, 3)

        # Randomly negate some of the variables
        for i in range(random.randint(0, 3)):
            clause[i] *= -1

        formula.append(clause)

    return formula

# Example usage:
num_variables = 9  # Should be a multiple of 3
num_clauses = 15

random_3sat_formula = generate_random_3sat_formula(num_variables, num_clauses)
print("Random 3-SAT Formula:")
for clause in random_3sat_formula:
    print(clause)

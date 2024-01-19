def evaluate_cnf_formula(cnf_formula, assignment):
    for clause in cnf_formula:
        clause_satisfied = False
        for literal in clause:
            variable, is_negated = abs(literal), literal < 0
            assigned_value = assignment.get(variable, None)

            if assigned_value is not None and (assigned_value == (not is_negated)):
                clause_satisfied = True
                break

        if not clause_satisfied:
            return False

    return True

def brute_force_sat_solver(cnf_formula):
    num_variables = max(abs(literal) for clause in cnf_formula for literal in clause)
    for i in range(2 ** num_variables):
        assignment = {variable: bool(i & (1 << (variable - 1))) for variable in range(1, num_variables + 1)}
        if evaluate_cnf_formula(cnf_formula, assignment):
            return assignment
    return None

# Example usage:
cnf_formula = [[1, 2, -3], [-1, -2, 3], [2, -3]]
result = brute_force_sat_solver(cnf_formula)

if result is not None:
    print("SATisfiable. Truth assignment:", result)
else:
    print("Not SATisfiable.")

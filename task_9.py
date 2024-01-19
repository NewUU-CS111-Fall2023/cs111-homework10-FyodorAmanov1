def is_satisfied(cnf_formula, truth_assignment):
    for clause in cnf_formula:
        clause_satisfied = False
        for literal in clause:
            variable, is_negated = abs(literal), literal < 0
            assigned_value = truth_assignment.get(variable, None)

            if assigned_value is not None and (assigned_value == (not is_negated)):
                clause_satisfied = True
                break

        if not clause_satisfied:
            return False

    return True
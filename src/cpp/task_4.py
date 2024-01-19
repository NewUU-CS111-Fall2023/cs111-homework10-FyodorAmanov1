def unary_multiplication_turing_machine(tape):
    # Initialize tape head position, state, and other variables
    tape_head = 0
    state = "q0"

    # Define transitions and states
    transitions = {
        # Move right until the first separator is reached
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "c"): ("q1", "c", "R"),

        # Move right and skip zeros in the first number
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "0"): ("q2", "0", "R"),

        # Move right until the second separator is reached
        ("q2", "1"): ("q2", "1", "R"),
        ("q2", "c"): ("q3", "c", "R"),

        # Move right and skip zeros in the second number
        ("q3", "1"): ("q3", "1", "R"),
        ("q3", "0"): ("q4", "0", "L"),

        # Move left until the end of the first number is reached
        ("q4", "1"): ("q4", "1", "L"),
        ("q4", "c"): ("q5", "c", "L"),

        # Move left and replace the separator with a zero
        ("q5", "1"): ("q5", "0", "L"),
        ("q5", "0"): ("q6", "0", "R"),

        # Move right while propagating the carry and adding the second number
        ("q6", "1"): ("q6", "0", "R"),
        ("q6", "c"): ("q_accept", "c", "S")
    }

    # Perform the simulation
    while state != "q_accept":
        symbol = tape[tape_head]
        current_transition = transitions.get((state, symbol), None)

        if current_transition is None:
            print("Invalid transition. Halting.")
            break

        # Update tape and head position based on the transition
        tape[tape_head] = current_transition[1]
        tape_head += 1 if current_transition[2] == "R" else -1
        state = current_transition[0]

    print(tape)
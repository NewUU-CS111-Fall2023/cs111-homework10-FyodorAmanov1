def unary_addition_turing_machine(tape):
    # Initialize tape head position, state, and other variables
    tape_head = 0
    state = "q0"
    carry = 0

    # Define transitions and states
    transitions = {
        ("q0", "1"): ("q0", "1", "R"),  # Move right while reading 1 in the first number
        ("q0", "0"): ("q1", "0", "R"),  # Move to q1 when reaching the separator "0"

        ("q1", "1"): ("q1", "0", "L"),  # Move left while replacing 1 with 0 in the first number
        ("q1", "0"): ("q2", "1", "L"),  # Move to q2 when reaching the end of the first number

        ("q2", "1"): ("q2", "1", "L"),  # Move left while skipping the second number
        ("q2", "0"): ("q3", "0", "L"),  # Move to q3 when reaching the separator "0" of the second number

        ("q3", "1"): ("q3", "1", "L"),  # Move left while adding 1 to the carry
        ("q3", "0"): ("q4", "0", "R"),  # Move to q4 when reaching the end of the second number

        ("q4", "1"): ("q4", "0", "R"),  # Move right while replacing 1 with 0 in the second number
        ("q4", "0"): ("q5", "1", "R"),  # Move to q5 when reaching the end of the second number

        ("q5", "1"): ("q5", "1", "R"),  # Move right while propagating the carry
        ("q5", "0"): ("q_accept", "0", "S")  # Move to the accept state when both numbers are processed
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


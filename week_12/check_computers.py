def check_computers():
    computers = []  # initial value

    # iterate & check for 5 computers
    for number in range(1, 6):

        # prompt the user to classify each computer
        # A - Available, U - Used, M - Maintenance
        status = input(f"Computer {number} Status (A/U/M): ").upper()

        computers.append(status)

    return computers
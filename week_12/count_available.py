def count_available(computers):

    available = 0  # initial value

    for computer in computers:

        if computer == "A":
            available += 1

    return available
from ticket import create_ticket
from display import display_ticket


def main():
    # Get ticket information
    ticket = create_ticket()

    # Display the ticket
    display_ticket(ticket)


if __name__ == "__main__":
    main()
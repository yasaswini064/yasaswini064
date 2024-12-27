class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Ticket:
    ticket_counter = 1

    def __init__(self, passenger, train_name, source, destination):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.passenger = passenger
        self.train_name = train_name
        self.source = source
        self.destination = destination

    def __str__(self):
        return (
            f"Ticket ID: {self.ticket_id}\n"
            f"Passenger: {self.passenger}\n"
            f"Train: {self.train_name}\n"
            f"Source: {self.source}\n"
            f"Destination: {self.destination}"
        )


class RailwayReservationSystem:
    def __init__(self):
        self.tickets = []

    def book_ticket(self, name, age, gender, train_name, source, destination):
        passenger = Passenger(name, age, gender)
        ticket = Ticket(passenger, train_name, source, destination)
        self.tickets.append(ticket)
        print(f"\nTicket booked successfully! Ticket ID: {ticket.ticket_id}")

    def view_tickets(self):
        if not self.tickets:
            print("\nNo tickets booked yet.")
        else:
            print("\nBooked Tickets:")
            for ticket in self.tickets:
                print(ticket)
                print("-" * 40)

    def cancel_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                self.tickets.remove(ticket)
                print(f"\nTicket ID {ticket_id} canceled successfully!")
                return
        print(f"\nTicket ID {ticket_id} not found.")


def main():
    system = RailwayReservationSystem()

    while True:
        print("\nRailway Reservation System Menu:")
        print("1. Book Ticket")
        print("2. View Tickets")
        print("3. Cancel Ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))
            gender = input("Enter passenger gender: ")
            train_name = input("Enter train name: ")
            source = input("Enter source station: ")
            destination = input("Enter destination station: ")
            system.book_ticket(name, age, gender, train_name, source, destination)
        elif choice == "2":
            system.view_tickets()
        elif choice == "3":
            ticket_id = int(input("Enter Ticket ID to cancel: "))
            system.cancel_ticket(ticket_id)
        elif choice == "4":
            print("Exiting Railway Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


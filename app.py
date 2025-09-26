import hashlib
import json
from time import time

# Block class to define each individual block in the blockchain
class Block:
    def __init__(self, ticket_id, event_name, event_date, previous_hash=''):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.timestamp = time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Calculate the hash of the block using SHA-256
    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Blockchain class to define the blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_tickets = []

        # Genesis Block (the first block in the chain)
        self.create_new_block(previous_hash='1', ticket_id="GENESIS", event_name="Genesis Event", event_date="2025-09-25")

    # Method to create a new block
    def create_new_block(self, ticket_id, event_name, event_date, previous_hash):
        new_block = Block(ticket_id, event_name, event_date, previous_hash)
        self.chain.append(new_block)
        return new_block

    # Add a ticket purchase (block) to the chain
    def add_ticket(self, ticket_id, event_name, event_date):
        previous_block = self.chain[-1]
        return self.create_new_block(ticket_id, event_name, event_date, previous_block.hash)

    # Verify the validity of a ticket (check if it's in the blockchain)
    def verify_ticket(self, ticket_id):
        for block in self.chain:
            if block.ticket_id == ticket_id:
                return True  # Ticket found
        return False  # Ticket not found

    # Display the blockchain
    def display_chain(self):
        for block in self.chain:
            print(f"Ticket ID: {block.ticket_id} | Event: {block.event_name} | Date: {block.event_date} | Hash: {block.hash}")

# Function to simulate ticket purchase and verification
def simulate_ticket_system():
    # Initialize the blockchain
    blockchain = Blockchain()

    while True:
        print("\nBlockchain-based Event Ticketing System")
        print("1. Purchase a ticket")
        print("2. Verify a ticket")
        print("3. View all tickets")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            ticket_id = input("Enter Ticket ID: ")
            event_name = input("Enter Event Name: ")
            event_date = input("Enter Event Date (YYYY-MM-DD): ")
            
            # Add ticket to blockchain
            blockchain.add_ticket(ticket_id, event_name, event_date)
            print(f"Ticket purchased! Ticket ID: {ticket_id} for event: {event_name}")
        
        elif choice == "2":
            ticket_id = input("Enter Ticket ID to verify: ")
            
            # Verify the ticket validity
            if blockchain.verify_ticket(ticket_id):
                print("Ticket is valid.")
            else:
                print("Invalid ticket. It might be a fake.")
        
        elif choice == "3":
            # Display all tickets in the blockchain
            blockchain.display_chain()
        
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the ticketing system
if __name__ == "__main__":
    simulate_ticket_system()

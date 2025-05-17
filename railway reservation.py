import random
class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkpassword(self, password):
        return self.password == password

account = [
    Account("user1", "password1"),
    Account("user1", "password2")
]

class Traindetails():
    def __init__(self, Train_number, source, destination, seats):
        self.Train_number = Train_number
        self.source = source
        self.destination = destination
        self.seats = seats

    def infor(self):
        print(f"\nTrain Number: {self.Train_number}") 
        print(f"Source: {self.source}") 
        print(f"Destination: {self.destination}") 
        print(f"Available Seats: {self.seats}") 

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(10000, 99999))
            self.seats -= num_tickets
            return pnr_list    

class Passenger_details():
    def __init__(self, Name, age, gender, mobile_no):
        self.Name = Name
        self.age = age
        self.gender = gender
        self.mobile_no = mobile_no

    def display_info(self):
        print(f"    Name       : {self.Name}")
        print(f"    Age        : {self.age}")
        print(f"    Gender     : {self.gender}")
        print(f"    Mobile No. : {self.mobile_no}")   

class Ticket():
    def __init__(self, Train, source, destination, passenger, pnr_no):
        self.Train = Train
        self.source = source
        self.destination = destination
        self.passenger = passenger
        self.pnr_no = pnr_no

    def display_info(self): 
        print("\n" + "="*40)
        print("            TRAIN TICKET")
        print("            HAPPY JOURNEY") 
        print("="*40)
        print(f"Train Number : {self.Train.Train_number}")    
        print(f"Source       : {self.source}")
        print(f"Destination  : {self.destination}")
        print(f"PNR Number   : {self.pnr_no}")
        print("-"*40)
        for p in self.passenger:
            p.display_info()
        print("="*40 + "\n")

# Login System
loginaccount = None
while True:  
    print("\n1. Create New Account\n2. Login")
    choice = input("Enter the number: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        account.append(Account(username, password))
        print("Account created successfully.") 
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in account:
            if user.username == username and user.checkpassword(password):
                loginaccount = user   
                break       
        if loginaccount is None:
            print("Invalid username or password.")
        else:
            print(f"Login successful. Welcome, {loginaccount.username}!")
            break
    else:
        print("Invalid choice.")

# Train Info
if loginaccount is not None:
    Trains = [
        Traindetails("8688", "Hyderabad", "Vijayawada", 15),
        Traindetails("9849", "Guntur", "Kurnool", 21),
        Traindetails("6303", "Hyderabad", "Goa", 22),     
        Traindetails("12345", "Vizag", "Delhi", 32),
    ]                 
    print("\nAvailable Trains:")
    for Train in Trains:
        Train.infor()  

# Booking
while True:
    try:
        Trainnumber = input("\nEnter the train number to book: ")
        no_of_tickets = int(input("Enter number of tickets: "))
        if no_of_tickets <= 0:
            raise ValueError("Number of tickets should be greater than 0.")
        for Train in Trains:
            if Train.Train_number == Trainnumber:
                if no_of_tickets > Train.seats:
                    raise ValueError("Selected number of tickets exceeds available seats.")
                break
        else:
            raise ValueError("Invalid train number.")
        break  
    except ValueError as e:
        print(f"Invalid input: {e}")

Train = None
for T in Trains:
    if T.Train_number == Trainnumber:
        Train = T
        break

if Train is None:
    print("Invalid train number.")
else:
    Passengers = []
    for i in range(no_of_tickets):
        print(f"\nEnter details for Passenger {i+1}")
        while True:
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            mobile = int(input("Mobile No.: "))
            passenger = Passenger_details(name, age, gender, mobile)
            Passengers.append(passenger)
            break

    pnrlist = Train.book_tickets(no_of_tickets)
    if pnrlist is None:
        print("Tickets not available.")
    else:
        print("\nBooking Successful!\nGenerating tickets...")
        for i in range(no_of_tickets):
            ticket = Ticket(Train, Train.source, Train.destination, [Passengers[i]], pnrlist[i])    
            ticket.display_info()

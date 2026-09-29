# Railway Ticket Booking System
import random
import os
file_name = "booking.txt"
trains = {"12345":["Aditya Sharma Express","Gwalior","Reshampura","1:10","6:45",900,50],"12346":["Duronto Express","Nagpur","Mumbai","4:15","9:30",800,65],"69069":["Harshit Express","Karandi","Bhusdapur","9:44","20:00",700,70],"11001":["Kerala Express","Delhi","Kerela","3:15","23.45",1200,80], "12809": ["Mumbai Mail", "Tatanagar", "Bhopal", "08:15", "06:30", 1200, 50],"12175": ["Chambal Express", "Gwalior", "Bhopal", "14:30", "21:45", 500, 45],"18237": ["Chhattisgarh Express", "Bilaspur", "Bhopal", "20:10", "09:30", 900, 60],"12001": ["Shatabdi Express", "New Delhi", "Bhopal", "06:00", "14:00", 700, 40],"12951": ["Mumbai Rajdhani", "Mumbai", "New Delhi", "17:00", "08:35", 1380, 35]}
bookings = {}
# Load old bookings
def load_data():
    if not os.path.exists(file_name):
        return
    f =open(file_name, "r")
    for line in f:
        x = line.strip().split("|")
        if len(x) == 9:
            pnr = x[0]
            bookings[pnr] = {"train": x[1],"name": x[2],"age": x[3],"gender": x[4],"class": x[5],"num": int(x[6]),"fare": float(x[7]),"status": x[8]}
# Save bookings
def save_data():
    f = open(file_name, "w")
    for pnr in bookings:
        b = bookings[pnr]
        line = (pnr + "|" +b["train"] + "|" + b["name"] + "|" + b["age"] + "|" + b["gender"] + "|" + b["class"] + "|" + str(b["num"]) + "|" + str(b["fare"]) + "|" + b["status"] + "\n")
        f.write(line)
    f.close()
# Generate PNR
def get_pnr():
    while True:
        pnr = str(random.randint(1000000000, 9999999999))
        if pnr not in bookings:
            return pnr
# Show all trains
def show_trains():
    print("\n" + "=" * 75)
    print("                         TRAIN LIST")
    print("=" * 75)
    print("No.            Name                        From           To             Seats")
    print("-" * 75)
    for no in trains:
        t = trains[no]
        print(no, "   ",t[0], " " * (20 - len(t[0])),t[1], " " * (10 - len(t[1])),t[2], " " * (10 - len(t[2])),t[6])
# Show one train
def train_details(no):
    t = trains[no]
    print("\nTrain Number :", no)
    print("Train Name   :", t[0])
    print("From         :", t[1])
    print("To           :", t[2])
    print("Departure    :", t[3])
    print("Arrival      :", t[4])
    print("Distance     :", t[5], "km")
    print("Seats        :", t[6])
# Search train
def search_train():
    print("\n----- SEARCH TRAIN -----")
    frm = input("From: ").lower()
    to = input("To: ").lower()
    found = False
    for no in trains:
        t = trains[no]
        if t[1].lower() == frm and t[2].lower() == to:
            train_details(no)
            found = True
    if not found:
        print("No train found.")
# Calculate fare
def fare(dist, cls, num):
    if cls == "Sleeper":
        rate = 1
    elif cls == "3A":
        rate = 2
    elif cls == "2A":
        rate = 3
    else:
        rate = 4
    return dist * rate * num
# Book ticket
def book():
    print("\n----- BOOK TICKET -----")
    show_trains()
    tn = input("\nEnter train number: ")
    if tn not in trains:
        print("Wrong train number.")
        return
    t = trains[tn]
    if t[6] == 0:
        print("No seats available.")
        return
    name = input("Passenger name: ")
    while True:
        try:
            age = int(input("Age: "))
            if age > 0:
                break
            print("Enter correct age.")
        except:
            print("Enter a number.")
    gender = input("Gender: ")
    print("\n1. Sleeper")
    print("2. 3A")
    print("3. 2A")
    print("4. 1A")
    c = input("Choose class: ")
    if c == "1":
        cls = "Sleeper"
    elif c == "2":
        cls = "3A"
    elif c == "3":
        cls = "2A"
    elif c == "4":
        cls = "1A"
    else:
        print("Wrong choice.")
        return
    while True:
        try:
            num = int(input("Number of passengers: "))
            if num > 0 and num <= t[6]:
                break
            print("Not enough seats.")
        except:
            print("Enter a number.")
    total = fare(t[5], cls, num)
    print("\nTotal fare:", total)
    ans = input("Confirm booking? (Y/N): ").upper()
    if ans != "Y":
        print("Booking cancelled.")
        return
    pnr = get_pnr()
    bookings[pnr] = {"train": tn,"name": name,"age": str(age),"gender": gender,"class": cls,"num": num,"fare": total,"status": "CONFIRMED"}
    t[6] = t[6] - num
    save_data()
    print("\nTicket booked successfully!")
    print("PNR:", pnr)
    print("Train:", t[0])
    print("Passenger:", name)
    print("Class:", cls)
    print("Passengers:", num)
    print("Fare:", total)
# Display one booking
def show_booking(pnr):
    b = bookings[pnr]
    t = trains[b["train"]]
    print("\n" + "=" * 45)
    print("                 TICKET")
    print("=" * 45)
    print("PNR        :", pnr)
    print("Name       :", b["name"])
    print("Age        :", b["age"])
    print("Gender     :", b["gender"])
    print("Train      :", t[0])
    print("From       :", t[1])
    print("To         :", t[2])
    print("Class      :", b["class"])
    print("Passengers :", b["num"])
    print("Fare       :", b["fare"])
    print("Status     :", b["status"])
    print("=" * 45)
# View all bookings
def my_bookings():
    print("\n----- MY BOOKINGS -----")
    if len(bookings) == 0:
        print("No bookings found.")
        return
    found = False
    for pnr in bookings:
        if bookings[pnr]["status"] == "CONFIRMED":
            show_booking(pnr)
            found = True
    if not found:
        print("No active bookings.")
# Check PNR
def check_pnr():
    pnr = input("\nEnter PNR: ")
    if pnr in bookings:
        show_booking(pnr)
    else:
        print("PNR not found.")
# Cancel ticket
def cancel():
    print("\n----- CANCEL TICKET -----")
    pnr = input("Enter PNR: ")
    if pnr not in bookings:
        print("PNR not found.")
        return
    b = bookings[pnr]
    if b["status"] == "CANCELLED":
        print("Ticket already cancelled.")
        return
    show_booking(pnr)
    ans = input("Cancel ticket? (Y/N): ").upper()
    if ans != "Y":
        print("Cancellation stopped.")
        return
    b["status"] = "CANCELLED"
    tn = b["train"]
    trains[tn][6] = trains[tn][6] + b["num"]
    refund = b["fare"] * 0.90
    save_data()
    print("\nTicket cancelled.")
    print("Refund:", round(refund, 2))
# Main program
load_data()
while True:
    print("\n")
    print("=" * 50)
    print("       RAILWAY TICKET BOOKING SYSTEM")
    print("=" * 50)
    print("1. View Trains")
    print("2. Search Train")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. My Bookings")
    print("6. Check PNR")
    print("7. Train Details")
    print("0. Exit")
    print("=" * 50)
    choice = input("Enter choice: ")
    if choice == "1":
        show_trains()
    elif choice == "2":
        search_train()
    elif choice == "3":
        book()
    elif choice == "4":
        cancel()
    elif choice == "5":
        my_bookings()
    elif choice == "6":
        check_pnr()
    elif choice == "7":
        show_trains()
        no = input("\nEnter train number: ")
        if no in trains:
            train_details(no)
        else:
            print("Wrong train number.")
    elif choice == "0":
        save_data()
        print("\nThank you for using the Railway Ticket Booking System!")
        print("Have a safe journey!")
        break
    else:
        print("Invalid choice.")

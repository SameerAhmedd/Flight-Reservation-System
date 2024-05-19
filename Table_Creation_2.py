import sqlite3

def create_connection():
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Customer(ID INTEGER PRIMARY KEY , First_Name , Last_Name, email , phone_number )")
    cur.execute("CREATE TABLE IF NOT EXISTS Flight(flight_id INTEGER PRIMARY KEY, ID INTEGER REFERENCES Customer(ID), Country , City , Date_ , DepartureTime_ , departure_port , destination_port  )")
    cur.execute("CREATE TABLE IF NOT EXISTS Seats(ID, Flight_ID , Class_Type , Price, Seat )")
    con.commit()
    return con, cur


#insertion

def insert_customer_data(data):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.executemany("INSERT INTO Customer (ID , First_Name , Last_Name, email , phone_number ) VALUES (? ,?, ?, ? ,?)", data)
    con.commit()
    con.close()



def insert_Destination_data(data):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.executemany("INSERT INTO Flight (flight_id, ID, Country , City , Date_ , DepartureTime_ , departure_port , destination_port) VALUES (?,?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()
    con.close()





def insert_Ticket_data(data):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.executemany("INSERT INTO Seats(ID, Flight_ID , Class_Type , Price, Seat ) VALUES (?,?, ?, ?,?)", data)
    con.commit()
    con.close()

#fetching

def fetch_customer_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Customer WHERE ID = ?", (ID,))   
    result = cur.fetchall()
    con.close()

    return result

def fetch_Destination_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Flight WHERE ID = ?", (ID,))   
    result = cur.fetchall()
    con.close()

    return result
    
def fetch_Ticked_data():
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("SELECT Seat FROM Seats")
    result = cur.fetchall()
    con.close()

    return result


def fetch_Destination_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Flight WHERE ID = ?", (ID,))   
    result = cur.fetchall()
    con.close()

    return result

def fetch_ALL_Ticked_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Seats WHERE ID = ?", (ID,))   
    result = cur.fetchall()
    con.close()

    return result



def Delete_Destination_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Flight WHERE ID = ?", (ID,))
    con.commit()
    con.close()


def Delete_customer_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Customer WHERE ID = ?", (ID,))
    con.commit()
    con.close()

def Delete_seat_data(ID):
    con = sqlite3.connect("Airplane.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Seats WHERE ID = ?", (ID,))
    con.commit()
    con.close()

# dummy_ticket_data = [
#     (1, 4, 'Economy', 200, 'button-1'),
#     (2, 5, 'Business', 500, 'button-2'),
#     (3, 6, 'Economy', 150, 'button-3'),
#     # Add more dummy data as needed
# ]
    
create_connection()

# insert_Ticket_data(dummy_ticket_data)







# -- Flights Table
# CREATE TABLE Flights (
#     flight_id INTEGER PRIMARY KEY,
#     departure_airport_code INTEGER,
#     arrival_airport_code INTEGER,
#     departure_time TEXT NOT NULL,
#     arrival_time TEXT NOT NULL,
#     available_seats INTEGER NOT NULL
#     -- Other relevant flight details here
# );

# -- Reservations Table
# CREATE TABLE Reservations (
#     reservation_id INTEGER PRIMARY KEY,
#     flight_id INTEGER REFERENCES Flights(flight_id),
#     id_no INTEGER REFERENCES Users(id_no),
#     seat_number TEXT NOT NULL,
#     reservation_date TEXT NOT NULL
#     -- Other reservation details here
# );
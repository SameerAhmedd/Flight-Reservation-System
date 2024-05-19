import sqlite3
# adding comments for aawaiz bbgurl
#con=connection for db (also doubles for if the db isnt there it creates one)
#we will remove comments from final submission :3

con = sqlite3.connect("Airplane.db")

#cursor to execute and fetch sql quries
cur = con.cursor()

#input all for these will come from the js file ID gen im leaving in js aswell for nwo entering manually

cur.execute("CREATE TABLE IF NOT EXISTS Customer(ID,First_Name,Last_Name)")
cur.execute("CREATE TABLE IF NOT EXISTS Destination(ID,Flight_ID,Country,City,Date_,Time_)")
cur.execute("CREATE TABLE IF NOT EXISTS Ticked(ID,Flight_ID,Class_Type,Price)")




#2 ways of inseting either through this(using this because looks more managable)

data = [
    (123, name, "Noor"),
    (321, name, "lmaao"),
    (421, name, "ali"),
]
cur.executemany("INSERT INTO Customer VALUES(?, ?, ?)", data)

#or this choose whtv u prefer

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)


# remember to always commit after inserting <3(v imp)
con.commit()




#to fetch what is coming for the check your booking section
res = cur.execute("SELECT First_Name FROM Customer")

result = res.fetchall()

print("Inserted data:")
for row in result:
    print(row)




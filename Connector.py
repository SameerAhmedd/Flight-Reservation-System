from flask import Flask, render_template, request, jsonify, redirect, url_for

from Table_Creation_2 import create_connection, insert_customer_data, insert_Destination_data, fetch_Destination_data, fetch_customer_data, Delete_Destination_data, Delete_customer_data, fetch_Ticked_data, insert_Ticket_data, fetch_ALL_Ticked_data, Delete_seat_data

from email_sender import emailsender

def unpack_destination_data(destination_data):
    if destination_data:
        row = destination_data[0]
        return row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
    else:
        # Return default values when data is not available
        return None, None, None, None, None, None, None, None

def unpack_customer_data(customer_data):
    if customer_data:
        row = customer_data[0]
        return row[0], row[1], row[2], row[3], row[4]
    else:
        # Return default values when data is not available
        return None, None, None, None, None

def unpack_seat_data(seat_data):
    if seat_data:
        row = seat_data[0]
        return row[0], row[1], row[2], row[3], row[4]
    else:
        # Return default values when data is not available
        return None, None, None, None, None
    
# Importing Flask to create a Flask-based application
# render_template is used to render HTML templates
# request is used to handle incoming HTTP requests
# jsonify is used to create a JSON response

app = Flask(__name__, template_folder='templates', static_folder='static')

# __name__ is a special variable in Python that represents the current module
# The template_folder and static_folder are specified so Flask knows where to look for templates and static files
# In this case, 'templates' is the folder for HTML templates, and 'static' is the folder for static files (e.g., JS, CSS)

@app.route('/')
def tester():
    return render_template('tester.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/bookings')
def bookings():
    return render_template('checkbookings.html')

@app.route('/airplane')
def airplane():
    return render_template('airplane.html')

# When a user visits the root URL, the tester function is executed
# Inside the function, render_template is used to render the 'tester.html' template
# This means that when someone accesses the root URL, they will see the content of 'tester.html'

@app.route('/submit_name', methods=['POST'])
def submit_name():
    if request.method == 'POST':
        # When a POST request is made to this URL, the submit_name function is executed

        # Retrieve form data from the request
        Table_name = request.form.get('Table_name')
        entered_name1 = request.form.get('First_name')
        entered_name2 = request.form.get('Last_name')
        id = request.form.get('ID')
        tel_num = request.form.get('phone_number')
        elec_mail = request.form.get('email')
        Seat_no = request.form.get('Seat')
        
        flight__id = request.form.get('flight_id')
        Country = request.form.get('Country')
        City = request.form.get('City')
        date = request.form.get('Date_')
        Time = request.form.get('DepartureTime_')
        destinationAirport = request.form.get('destination_port')
        departureAirport = request.form.get('departure_port')

        print(f"Received names: {Table_name}, {entered_name1}, {entered_name2}, {id}, {tel_num}, {elec_mail}, {date}, {Country}, {City}, {Time}, {destinationAirport}, {departureAirport}, {Seat_no}")

        # Insert data into the Customer table
        insertion_data = [
            (id, entered_name1, entered_name2, elec_mail, tel_num),
        ]
        insert_customer_data(insertion_data)

        # Insert data into the Destination table
        insertion_data = [
            (flight__id, id, Country, City, date, Time, destinationAirport, departureAirport),
        ]
        insert_Destination_data(insertion_data)

        seat_number = int(Seat_no.split('-')[1])

        # Check if the seat_number falls within the range of 1-24
        if 1 <= seat_number <= 24:
            class_type = "First Class"
            price = "950"
        elif 25 <= seat_number <= 48:
            class_type = "Business Class"
            price = "550"
        else:
            class_type = "Economy Class"
            price = "250"
        
        # Insert data into the Ticket table
        insertion_data = [
            (id, flight__id, class_type, price, Seat_no),
        ]
        insert_Ticket_data(insertion_data)

        try:
            # Assuming emailsender is defined elsewhere in your code
            # Define reciever, message, and other variables here
            reciever = elec_mail
            message = (f'Subject: Smeer Airlines.\nDear {entered_name1} {entered_name2}, \n\n'
                       f'Your Flight has Been Booked. Your Flight Details Are: '
                       f'Booking ID: {id}, Flight ID: {flight__id}, Your Seat No is: {seat_number}, '
                       f'Your Departure Time is: {Time}, Your Destination Airport is: {destinationAirport}, '
                       f'\n\n Flight To: {Country}, {City}. Your Total Price is: {price} for {class_type}.')
            emailsender(reciever, message, entered_name1, entered_name2, id, seat_number, Time, destinationAirport, Country, City, price, class_type, flight__id, date, departureAirport)

        except Exception as e:
            print(f"An error occurred: {e}")
            # Handle the error as needed, e.g., log it, inform the user, etc.

        # Return a JSON response indicating success
        return jsonify({'message': 'Booking successfully made!'})

@app.route('/data_getter', methods=['POST'])
def data_getter():
    if request.method == 'POST':
        # When a POST request is made to this URL, the data_getter function is executed

        id = request.form.get('ID')
        print(f"Received ID: {id}")

        # Fetch data from the Customer table
        customer_data = fetch_customer_data(id)
        # Fetch data from the Destination table
        destination_data = fetch_Destination_data(id)
        # Fetch data from the Ticket table
        seat_data = fetch_ALL_Ticked_data(id)

        # Unpack the fetched data
        flightID, ID, Country, City, Date, Time, Air, Air2 = unpack_destination_data(destination_data)
        ID, First_Name, Last_Name, email, phone_number = unpack_customer_data(customer_data)
        ID, flightID, Class, Price, Seat = unpack_seat_data(seat_data)

        # Print fetched data for debugging purposes
        if destination_data:
            print("Destination data found:")
            for row in destination_data:
                print(row)
        else:
            print("No destination data found for the specified ID.")

        if customer_data:
            print("Customer data found:")
            for row in customer_data:
                print(row)
        else:
            print("No customer data found for the specified ID.")

        if seat_data:
            print("Seat data found:")
            for row in seat_data:
                print(row)
        else:
            print("No seat data found for the specified ID.")

        # Return the fetched data as a JSON response
        return jsonify({
            'flightID': flightID,
            'ID': ID,
            'Country': Country,
            'City': City,
            'Date': Date,
            'Time': Time,
            'Air': Air,
            'Air2': Air2,
            'First_Name': First_Name,
            'Last_Name': Last_Name,
            'email': email,
            'phone_number': phone_number,
            'Class': Class,
            'Price': Price,
            'Seat': Seat
        })

@app.route('/deleter', methods=['POST'])
def deleter():
    if request.method == 'POST':
        # When a POST request is made to this URL, the deleter function is executed

        id = request.form.get('ID')
        print(f"Received ID: {id}")

        # Delete data from the Customer table
        Delete_customer_data(id)
        # Delete data from the Destination table
        Delete_Destination_data(id)
        # Delete data from the Seat table
        Delete_seat_data(id)

        # Return a JSON response indicating success
        return jsonify({'deleted': 'deleted'})

@app.route('/fetch_seat_data')
def fetch_seat_data():
    # Fetch seat data from the database
    seat_data = fetch_Ticked_data()
    # Extract seat numbers from the fetched data
    seats = [seat[0] for seat in seat_data]
    print(seats)

    # Return the seat data as a JSON response
    return jsonify(seats)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

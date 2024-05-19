import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def emailsender(reciever,message,entered_name1,entered_name2,id,seat_number,Time,destinationAirport,Country,City,price,class_type,flight__id,date,departureAirport):
    server = smtplib.SMTP('smtp.office365.com',587)
    server.ehlo()
    server.starttls()
    server.login('smearairlines@outlook.com', 'sameerishere123')
    server.Subject = 'Flight Booking Info'
    server.BodyFormat = 1
    sender="smearairlines@outlook.com"




    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email with Graphics</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: black;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: white;
                text-align: center;
            }}
            .message {{
                color: white;
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="message">
                <h1>Flight Booking Confirmation</h1>
                <p>Dear {entered_name1} {entered_name2},</p>
                <p>Your flight has been booked successfully. Here are the details:</p>
                <ul>
                    <li><strong>Booking ID:</strong> {id}</li>
                    <li><strong>Flight ID:</strong> {flight__id}</li>
                    <li><strong>Seat No:</strong> {seat_number}</li>
                    <li><strong>Departure Date:</strong> {date}</li>                   
                    <li><strong>Departure Time:</strong> {Time}</li>
                    <li><strong>Departure Airport:</strong> {departureAirport}</li>                    
                    <li><strong>Destination Airport:</strong> {destinationAirport}</li>
                    <li><strong>Flight From:</strong> {Country}, {City}</li>
                    <li><strong>Total Price:</strong> {price}</li>
                    <li><strong>Class:</strong> {class_type}</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """



    # Create the HTML part
    html_part = MIMEText(html_content.format(message_body=message,departureAirport=departureAirport,date=date,entered_name1=entered_name1,entered_name2=entered_name2,id=id,seat_number=seat_number,Time=Time,destinationAirport=destinationAirport,Country=Country,City=City,price=price,class_type=class_type,flight__id=flight__id), 'html')

    # Create the multipart message
    message = MIMEMultipart()
    message.attach(html_part)
    #Adding a newline before the body text fixes the missing message body
    server.sendmail(sender,reciever,message.as_string())
    server.quit()



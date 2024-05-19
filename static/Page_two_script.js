document.addEventListener("DOMContentLoaded", function () {
    const burgerMenu = document.querySelector(".burger-menu");
    const navLinks = document.querySelector(".nav-links");

    var Country = localStorage.getItem('Country');
    var City = localStorage.getItem('City');
    var date = localStorage.getItem('date');
    var passengers = localStorage.getItem('passengers');



    function generateUniqueRandomNumber() {
        const timestamp = new Date().getTime();
      
        const randomNum = Math.floor(Math.random() * 1000);
      
        const uniqueNumber = timestamp + randomNum;
      
        return uniqueNumber;
    }


    
    // Set values in the new form
    document.getElementById('departureAirport').value = Country;
    document.getElementById('destinationAirport').value = City;
    document.getElementById('departureDate2').value = date;
    document.getElementById('passengers2').value = passengers;

    let passengersLeft = parseInt(passengers); // Number of passengers left to book

    const Customer = document.getElementById("Customer");

    Customer.addEventListener("submit", function (event) {
        event.preventDefault();

        const FlightId = generateUniqueRandomNumber();


        var seatno = localStorage.getItem('seat_num');

        const firstName = document.getElementById("firstName");
        const lastName = document.getElementById("lastName");
        const email = document.getElementById("email");
        const phoneNum = document.getElementById("phoneNumber");
        const identificationNum = document.getElementById("identificationNumber");

        const destair = document.getElementById("destinationAirport");
        const depair = document.getElementById("departureAirport");
        const time = document.getElementById("departureTime");


        const timeofdep = time.value;
        const airdest = destair.value;
        const airdep = depair.value;


        const Table_name = Customer;
        const First_name = firstName.value;
        const Last_Name = lastName.value;
        const Email = email.value;
        const phoneNumber = phoneNum.value;
        const identificationNumber = identificationNum.value;


        const formData = new FormData(Customer);
        
        formData.append("First_name", First_name);
        formData.append("Last_name", Last_Name);
        formData.append("ID", identificationNumber);
        formData.append("phone_number", phoneNumber);

        formData.append("Country", Country);
        formData.append("City", City);
        formData.append("Date_", date);
        formData.append("flight_id", FlightId);

        formData.append("DepartureTime_", timeofdep);
        formData.append("departure_port", airdest);
        formData.append("destination_port", airdep);
        formData.append("Seat", seatno);

        

        formData.append("Table_name", "Customer");

        // const City = departureCity.value;

        fetch('/submit_name', {
            method: 'POST',

            body: formData            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Data received:", data);

            passengersLeft--;

            if (passengersLeft > 0) {
                alert(`Passenger ${parseInt(passengers) - passengersLeft} Booked`);
                firstName.value = "";
                lastName.value = "";
                email.value = "";
                phoneNum.value = "";
                identificationNum.value = "";
            } else {
                document.querySelector(".container").style.display = "none";

                alert("All passengers booked,Please Check Your Email(Spam Folder)");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

    });


    const airButton = document.getElementById("Drake_Glizzy");

    // Adding an event listener to the button
    airButton.addEventListener("click", function(event) {
        event.preventDefault();


        // Specify the URL and size of the smaller window
        var url = "/airplane";
        var width = 800;
        var height = 1200;
      
            // Calculate the position of the smaller window to center it on the screen
        var left = (screen.width - width) / 2;
        var top = (screen.height - height) / 2;
      
            // Open the smaller window
        window.open(url, "SmallerWindow", "width=" + width + ",height=" + height + ",left=" + left + ",top=" + top);
    });

      


    burgerMenu.addEventListener("click", function () {
        navLinks.classList.toggle("show");
    });
});

window.addEventListener("resize", function () {
    var myDiv = document.getElementById("sign-up");
    if (window.innerWidth <= 768) {
        // Screen width is smaller or equal to 768 pixels
        myDiv.classList.remove("sign-up");
        myDiv.classList.remove("scrolled-button");
    } else {
        // Screen width is greater than 768 pixels
        if (
            !myDiv.classList.contains("sign-up") ||
            !myDiv.classList.contains("scrolled-button")
        ) {
            // Add the class back if it's not present
            myDiv.classList.add("sign-up");
            myDiv.classList.add("scrolled-button");
        }
    }
});

function scrollToElement(id) {
    var element = document.getElementById(id);

    if (element) {
        element.scrollIntoView({ behavior: "smooth" });
    }
}

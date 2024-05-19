document.addEventListener("DOMContentLoaded", function () {
    const burgerMenu = document.querySelector(".burger-menu");
    const navLinks = document.querySelector(".nav-links");



    const Customer = document.getElementById("Customer");

    Customer.addEventListener("submit", function (event) {
        event.preventDefault();


        const identificationNum = document.getElementById("identificationNumber");

        const identificationNumber = identificationNum.value;


        const formData = new FormData(Customer);
        
        formData.append("ID", identificationNumber);


        formData.append("Table_name", "Customer");


        fetch('/data_getter', {
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
    

            const First_Name = data['First_Name'];
            const Last_Name = data['Last_Name'];
            const email = data['email'];
            const phone_number = data['phone_number'];
            const Country = data['Country'];
            const City = data['City'];
            const Time = data['Time'];
            const Date = data['Date'];
            const Air = data['Air'];
            const Air2 = data['Air2'];

            const Class = data['Class'];
            const Price = data['Price'];
            const Seat = data['Seat'];

            if (data['First_Name'] !== null && data['Last_Name'] !== null && data['email'] !== null && data['phone_number'] !== null && data['Country'] !== null && data['City'] !== null && data['Time'] !== null && data['Date'] !== null && data['Air'] !== null && data['Air2'] !== null && data['Class'] !== null && data['Price'] !== null && data['Seat'] !== null) {

            document.getElementById("firstName").value = First_Name;
            document.getElementById("lastName").value = Last_Name;
            document.getElementById("email").value = email;
            document.getElementById("phoneNumber").value = phone_number;
            document.getElementById("departureCountry").value = Country;
            document.getElementById("Destination_City").value = City;
            document.getElementById("departureTime").value = Time;
            document.getElementById("departureDate2").value = Date;
            document.getElementById("departureAirport").value = Air;
            document.getElementById("destinationAirport").value = Air2;
            document.getElementById("Class").value = Class;
            document.getElementById("Price").value = Price;
            document.getElementById("Seat").value = Seat;
            

            } else {
                document.getElementById("firstName").value = null;
                document.getElementById("lastName").value = null;
                document.getElementById("email").value = null;
                document.getElementById("phoneNumber").value = null;
                document.getElementById("departureCountry").value = null;
                document.getElementById("Destination_City").value = null;
                document.getElementById("departureTime").value = null;
                document.getElementById("departureDate2").value = null;
                document.getElementById("departureAirport").value = null;
                document.getElementById("destinationAirport").value = null;
                document.getElementById("Class").value = null;
                document.getElementById("Price").value = null;
                document.getElementById("Seat").value = null;

                alert("No Such Data Found");

            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    });

    const delButton = document.getElementById("delete");

    // Adding an event listener to the button
    delButton.addEventListener("click", function(event) {
        event.preventDefault();

        const identificationNum = document.getElementById("identificationNumber");

        const identificationNumber = identificationNum.value;


        const formData = new FormData(Customer);
        
        formData.append("ID", identificationNumber);


        formData.append("Table_name", "Customer");
        fetch('/deleter', {
            method: 'POST',
    
            body: formData            
        })
        .then(data => {
            console.log("Data received:", data);

            alert("Data Deleted");
        })
        .catch((error) => {
            console.error("Error:", error);
        });
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

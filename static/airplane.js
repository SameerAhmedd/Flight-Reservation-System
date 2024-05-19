function fetchSeatDataAndUpdateButtons() {
    fetch('/fetch_seat_data')  
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(seatNumbers => {
            console.log("Seat numbers received:", seatNumbers);

            seatNumbers.forEach(seatId => {
                const button = document.getElementById(seatId);
                if (button) {
                    button.style.backgroundColor = "red"; 
                }
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

fetchSeatDataAndUpdateButtons();



function changeColor(id) {
    const button = document.getElementById(id);
    
    if (button.style.backgroundColor == "green") {
        button.style.backgroundColor = "red";

        localStorage.setItem('seat_num', id);

    } else {
        button.style.backgroundColor = "green";
    }
}



function closeWindow() {
    window.close();
  }
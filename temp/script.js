document.addEventListener("DOMContentLoaded", function () {
    const nameForm = document.getElementById("nameForm");
    const resultDiv = document.getElementById("result");

    nameForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const nameInput = document.getElementById("name");
        const enteredName = nameInput.value;

        fetch('/submit_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'name': enteredName })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
        });

        nameInput.value = '';
    });
});


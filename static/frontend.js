document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('companyForm');
    const resultContainer = document.getElementById('result');
    const outputBox = document.getElementById('outputBox'); // The output box for displaying the report
    const loadingImage = document.getElementById('loadingImage'); // Reference to the loading image element

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const companyName = document.getElementById('companyName').value;
        resultContainer.textContent = ''; // Clear any previous results
        outputBox.innerHTML = ''; // Clear the output box
        outputBox.style.display = 'none'; // Hide the output box initially

        const submitButton = form.querySelector('button[type="submit"]');
        submitButton.disabled = true; // Disable the submit button to prevent multiple submissions
        loadingImage.style.display = 'block'; // Show loading image

        fetch('/run-script', {
            method: 'POST',
            body: JSON.stringify({ company: companyName }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            submitButton.disabled = false; // Re-enable the submit button
            loadingImage.style.display = 'none'; // Hide loading image

            if (data.reportContent) {
                outputBox.innerHTML = data.reportContent; // Use innerHTML to parse the HTML content
                outputBox.style.display = 'block'; // Display the output box with the report content
            } else {
                resultContainer.textContent = data.message; // Show the message in the result container
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultContainer.textContent = 'An error occurred: ' + error;
            submitButton.disabled = false; // Re-enable the submit button in case of error
            loadingImage.style.display = 'none'; // Hide loading image even if there's an error
        });
   

    });
});

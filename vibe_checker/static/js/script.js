document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const sentimentResult = document.querySelector(".result");

    if (!form || !sentimentResult) {
        console.error("Form or result element not found.");
        return;
    }

    // Add an event listener to the form submission
    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Get the text input value
        const textInput = document.querySelector("textarea").value;

        // Simple validation
        if (!textInput.trim()) {
            alert("Please enter some text for analysis.");
            return;
        }

        sentimentResult.textContent = "Analyzing sentiment...";
        sentimentResult.style.display = "block";

        // Send the form data to the server
        fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `text=${encodeURIComponent(textInput)}`,
        })
            .then((response) => response.text())
            .then((data) => {
                // Update the sentiment result
                sentimentResult.innerHTML = data;

                // Optionally, display the chart if it's available
                const chart = document.querySelector("#chart");
                if (chart) {
                    chart.style.display = "block";
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                sentimentResult.textContent = "An error occurred while analyzing sentiment.";
            });
    });
});

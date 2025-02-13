setInterval(() => {
    fetch('/get-updated-stocks')
        .then(response => response.json())
        .then(data => {
            // Update table rows dynamically
        });
}, 5000);  // Update every 5 seconds

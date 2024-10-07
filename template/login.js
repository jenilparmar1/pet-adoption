function toggle(){
    var x = document.getElementById("password");

    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const usernameOrEmail = 'jenilparmar1';
    const password = '1234';

    // Send a POST request to the Flask server for login verification
    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'username': usernameOrEmail,
            'password': password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirect to index.html if the credentials are correct
            console.log("Received JSON response from server:", data); // Debugging info
            window.location.href = data.redirect_url;
        } else {
            // Display an error message if the credentials are incorrect
            document.getElementById('error-message').textContent = data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('error-message').textContent = 'Server error, please try again later.';
    });
});
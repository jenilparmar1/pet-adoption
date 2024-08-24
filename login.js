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

    const usernameOrEmail = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Sample hardcoded credentials for demonstration
    const credentials = {
        username: 'jenilparmar1',
        email: 'jenilparmar1@gmail.com',
        password: '1234'
    };

    // Check if the provided username/email and password match the hardcoded credentials
    if ((usernameOrEmail === credentials.username || usernameOrEmail === credentials.email) && password === credentials.password) {
        // Redirect to index.html if the credentials are correct
        window.location.href = 'index.html';
    } else {
        // Display an error message if the credentials are incorrect
        document.getElementById('error-message').textContent = 'Invalid username/email or password.';
    }
});

// Toggle password visibility
function togglePassword() {
const passwordField = document.getElementById('password');
const toggleIcon = document.querySelector('.toggle-password-icon');

if (passwordField.type === 'password') {
    passwordField.type = 'text';
    toggleIcon.textContent = '🫣'; // Change to 'hide' icon
    } else {
    passwordField.type = 'password';
    toggleIcon.textContent = '😵‍💫'; // Change back to 'show' icon
    }
}
const loginForm = document.getElementById('loginForm');
const loginButton = document.getElementById('LoginButton');

// Add event listener to handle form submission
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission

    // Get the email and password values from the input fields
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Prepare the data to send in the POST request
    const data = {
        email: email,
        password: password
    };

    // Make the POST request using fetch
    fetch('http://127.0.0.1:8000', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // You can include an authorization token if needed
            //'Authorization': 'Bearer your-token-here'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
        console.log('Success:', data);
        // Handle successful login, e.g., redirect or show a message
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle errors, e.g., display an error message
    });
});

// Highlight input field with an error
function highlightError(inputId) {
    const inputElement = document.getElementById(inputId);
    if (inputElement) {
        inputElement.style.border = "solid red"; // Highlight the border
    }
}

// Clear error highlights (optional)
function clearError(inputId) {
    const inputElement = document.getElementById(inputId);
    if (inputElement) {
        inputElement.style.border = ""; // Reset the border
    }
}

// Toggle password visibility
function togglePassword() {
    const passwordField = document.getElementById('password');
    const toggleIcon = document.querySelector('.toggle-password-icon');
    
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        if (toggleIcon) toggleIcon.textContent = '🫣'; // Change to 'hide' icon
    } else {
        passwordField.type = 'password';
        if (toggleIcon) toggleIcon.textContent = '😵‍💫'; // Change back to 'show' icon
    }
}

// Handle form submission
async function handleLogin(event) {
    event.preventDefault(); // Prevent default form submission

    // Get the email and password values
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Clear previous errors
    clearError('email');
    clearError('password');

    const data = { email, password };

    try {
        // Send POST request to login endpoint
        const response = await fetch('http://127.0.0.1:8000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json();
        // Handle server validation errors
        if (responseData.message === "Invalid Email") {
            highlightError("email");
        } else if (responseData.message === "Invalid Password") {
            highlightError("password");
        }

        // If the response contains a token, store it in localStorage
        if (responseData.token) {
            localStorage.setItem("jwtToken", responseData.token);

            // Send GET request to the home endpoint
            const homeResponse = await fetch('http://127.0.0.1:8000/home/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${responseData.token}`,
                },
            });

            if (!homeResponse.ok) {
                throw new Error(`HTTP error! Status: ${homeResponse.status}`);
            }

            const homeData = await homeResponse.json();

            // Redirect to the received URL
            if (homeData.url) {
                window.location.href = homeData.url;
            } else {
                console.error("No redirect URL found in response");
            }
        } else {
            console.error("No token found in the response");
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

// Add event listener to the login form
document.getElementById('loginForm').addEventListener('submit', handleLogin);

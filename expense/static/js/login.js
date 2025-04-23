document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const errorMessageDiv = document.getElementById('error-message');
    const togglePasswordCheckbox = document.getElementById('toggle-passwords');
    const passwordInput = document.getElementById('password');

    // Handle form submission
    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        errorMessageDiv.textContent = '';

        // Collect form data
        let email = document.getElementById('email').value;
        if (email) {
            email = email.replace(" ", ""); // Remove all spaces from email
        }

        const formData = {
            email: email,
            password: passwordInput.value
        };

        try {
            // Send AJAX request to backend
            const response = await fetch(loginForm.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Include CSRF token
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            // Handle response
            if (response.ok && result.message) {
                // Success: Redirect or show success message
                alert(result.message); // Replace with better UI notification if needed
                window.location.href = '/dashboard'; // Redirect to dashboard or home page
            } else {
                // Display error message from backend
                errorMessageDiv.textContent = result.error || 'Invalid email or password.';
                errorMessageDiv.style.display = 'block';
            }
        } catch (error) {
            // Handle network or other unexpected errors
            errorMessageDiv.textContent = 'Network error. Please try again later.';
            errorMessageDiv.style.display = 'block';
            console.error('Error:', error);
        }
    });

    // Handle "Show Password" toggle
    togglePasswordCheckbox.addEventListener('change', () => {
        const type = togglePasswordCheckbox.checked ? 'text' : 'password';
        passwordInput.type = type;
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
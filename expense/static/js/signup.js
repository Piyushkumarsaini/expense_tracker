document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');
    const errorMessageDiv = document.getElementById('error-message');
    const togglePasswordsCheckbox = document.getElementById('toggle-passwords');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirm_password');

    // Handle form submission
    signupForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        errorMessageDiv.textContent = '';

        // Collect form data
        const formData = {
            username: document.getElementById('username').value,
            email: document.getElementById('email').value,
            password: passwordInput.value,
            confirm_password: confirmPasswordInput.value
        };

        try {
            // Send AJAX request to backend
            const response = await fetch(signupForm.action, {
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
                alert(result.message); // You can replace this with a better UI notification
                window.location.href = '/login'; // Redirect to login page
            } else {
                // Display error message from backend
                errorMessageDiv.textContent = result.error || 'An unexpected error occurred.';
                errorMessageDiv.style.display = 'block';
            }
        } catch (error) {
            // Handle network or other unexpected errors
            errorMessageDiv.textContent = 'Network error. Please try again later.';
            errorMessageDiv.style.display = 'block';
            console.error('Error:', error);
        }
    });

    // Handle "Show Passwords" toggle
    togglePasswordsCheckbox.addEventListener('change', () => {
        const type = togglePasswordsCheckbox.checked ? 'text' : 'password';
        passwordInput.type = type;
        confirmPasswordInput.type = type;
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
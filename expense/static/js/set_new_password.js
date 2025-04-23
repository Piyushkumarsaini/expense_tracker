document.addEventListener('DOMContentLoaded', () => {
    const setnewpassword = document.getElementById('set-new-password');
    const errorMessageDiv = document.getElementById('error-message');
    const togglePasswordCheckbox = document.getElementById('toggle-passwords');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirm_password');

    // Handle form submission
    setnewpassword.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        errorMessageDiv.textContent = '';

        const formData = {
            password: passwordInput.value,
            confirm_password: confirmPasswordInput.value
        };

        try {
            // Send AJAX request to backend
            const response = await fetch(setnewpassword.action, {
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
                window.location.href = '/login'; // Redirect to dashboard or home page
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

    // Handle "Show Password" toggle
    togglePasswordCheckbox.addEventListener('change', () => {
        const type = togglePasswordCheckbox.checked ? 'text' : 'password';
        const style = window.getComputedStyle(passwordInput); // Preserve current style
        passwordInput.type = type;
        confirmPasswordInput.type = type;
        // Force reflow to maintain layout
        passwordInput.style.width = style.width;
        confirmPasswordInput.style.width = style.width;
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
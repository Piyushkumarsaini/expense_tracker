document.addEventListener('DOMContentLoaded', () => {
    const verifyemail = document.getElementById('verify-email');
    const errorMessageDiv = document.getElementById('error-message');
    const email = document.getElementById('email');


    // Handle form submission
    verifyemail.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        errorMessageDiv.textContent = '';

        const formData = {
            email: email.value,
        };

        try {
            // Send AJAX request to backend
            const response = await fetch(verifyemail.action, {
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
                window.location.href = '/reset_password/'; // Redirect to reset new password page
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
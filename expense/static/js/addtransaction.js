document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-transaction-form');
    const errorMessageDiv = document.getElementById('error-message');
    const successMessageDiv = document.getElementById('success-message');
    const totalIncomeSpan = document.getElementById('total-income');
    const totalExpenseSpan = document.getElementById('total-expense');
    const totalSpan = document.getElementById('total');


    if (!form) {
        console.error('Form with ID "add-transaction-form" not found');
        return;
    }
    
    if (paymentMethodSelect) {
        paymentMethodSelect.addEventListener('change', () => {
            const selectedValue = paymentMethodSelect.value;
    
            if (selectedValue === '__view_all__') {
                const hiddenOptions = paymentMethodSelect.querySelectorAll('.hidden-method');
                hiddenOptions.forEach(opt => {
                    opt.style.display = 'block';
                });
    
                // Remove "View All Methods" option
                const viewAllOption = document.getElementById('view-all-option');
                if (viewAllOption) {
                    viewAllOption.remove();
                }
    
                // ✅ Delay reset so it doesn’t block rendering
                setTimeout(() => {
                    paymentMethodSelect.selectedIndex = 0;
                }, 10); // 10ms is enough
            }
        });
    }
    
    // Handle form submission
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        // Clear previous messages
        errorMessageDiv.textContent = '';
        successMessageDiv.textContent = '';
        errorMessageDiv.style.display = 'none';
        successMessageDiv.style.display = 'none';

        // Collect form data
        const formData = {
            type: document.getElementById('type').value,
            category: document.getElementById('category').value,
            payment_method: document.getElementById('payment_method').value,
            amount: document.getElementById('amount').value,
            description: document.getElementById('description').value || ''
        };

        try {
            // Send AJAX request to backend
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                const result = await response.json();
                errorMessageDiv.textContent = result.error || 'An unexpected error occurred.';
                errorMessageDiv.style.display = 'block';
                return;
            }

            // If the view returns a rendered template, handle the full HTML response
            const text = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');
            const newTotalIncome = doc.getElementById('total-income')?.textContent || totalIncomeSpan.textContent;
            const newTotalExpense = doc.getElementById('total-expense')?.textContent || totalExpenseSpan.textContent;
            const newTotal = doc.getElementById('total')?.textContent || totalSpan.textContent;
            const newSuccessMessage = doc.getElementById('success-message')?.textContent;

            // Update DOM with new values
            if (totalIncomeSpan) totalIncomeSpan.textContent = newTotalIncome;
            if (totalExpenseSpan) totalExpenseSpan.textContent = newTotalExpense;
            if (totalSpan) totalSpan.textContent = newTotal;
            if (successMessageDiv && newSuccessMessage) {
                successMessageDiv.textContent = newSuccessMessage;
                successMessageDiv.style.display = 'block';
            }

            // Optionally clear the form
            form.reset();
        } catch (error) {
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
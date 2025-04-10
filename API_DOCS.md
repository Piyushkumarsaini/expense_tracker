# 📄 Expense Tracker API Documentation

This document contains all the API endpoints for the Expense Tracker project built with Django. Each API is explained with its request format, response format, and usage.

---

## 🔁 API Flow Order

1. Signup – `/signup/`  
2. Login – `/login/`  
3. Change Password – `/changepassword/`  
4. Add Income – `/income/`  
5. Show Income – `/income/<int:user_id>`  
6. Delete Income – `/income/<int:user_id>/delete/<int:income_id>`  
7. Update Income – `/income/<int:user_id>/update/<int:income_id>`  
8. Add Expense – `/expense/`  
9. Show Expense – `/expense/<int:user_id>`  
10. Delete Expense – `/expense/<int:user_id>/delete/<int:expense_id>`  
11. Update Expense – `/expense/<int:user_id>/update/<int:expense_id>`  
12. Get Total – `/total/<int:user_id>`

---

## 📌 API Endpoints

### 1. ✅ Signup
- **URL**: `/signup/`
- **Method**: `POST`
- **Request Body**:
```json
{
  "username": "zahul",
  "email": "zahul01@gmail.com",
  "password": "123234",
  "confirmpassword": "123234"
}

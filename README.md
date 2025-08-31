.

# 💰 Expense Tracker – Django Project
This Django project allows users to manage their income, expenses, and budgets.
It includes features such as category-wise tracking, selection of payment methods, and user authentication for a secure and personalized experience

---

## 🚀 Features

- 👤 User Registration and Management
- 💸 Add and Categorize Expenses
- 💰 Add and Categorize Incomes
- 🎯 Set Budgets for Expense Categories
- 💳 Multiple Payment Methods
- 📊 Expense & Income History Tracking
- 📅 Automatic Date/Time Logging

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite
- **Tools**: Django Admin, ORM, Migrations

---

## 🗂️ Models Overview

### 👤 `User`
Stores user account info:
- `username`, `email`, `password`
- `date`, `time` (auto-created)

### 💰 `Income`
Tracks income records:
- Linked to `User` and `IncomeCategory`
- Stores `amount`, `category_id`, `date`, `time` (auto-created)


### 📈 `IncomeCategory`
Stores names of income types (e.g. Salary, Bonus)

### 💸 `Expense` 
Tracks expenses:
- Linked to `User`, `ExpenseCategory`, `PaymentMethod`
- Contains `amount`, `category_id`, `payment_method_id`, `description`, `date`, `time` (auto-created)

### 🧾 `ExpenseCategory`
Stores names of expense types (e.g. Food, Travel)

### 💳 `PaymentMethod`
Stores available payment methods (e.g. Cash, Card)

### 🎯 `Budget`
Users can set a limit for a specific expense category

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/Piyushkumarsaini/expense_tracker.git
cd expense_tracker
```

2. **Create Virtual Environment**
```venv
python -m venv venv
```
3. **Activate Virtual Environment**
```venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install Dependencies**
```
pip install -r requirements.txt
```

5. **Run Migrations**
```
python manage.py makemigrations
python manage.py migrate
```

6. **Run the Server**
```
python manage.py runserver
```



## 📁 Project Structure

```
expense_tracker/
├── expense_tracker/             # Project Configuration + Root Files
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Root URL configuration
│   └── wsgi.py

├── expense/                     # Main App
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                # All data models
│   ├── tests.py
│   ├── urls.py                  # App URL routing
│   ├── view/                    # Views split by feature
│   │   ├── budget.py
│   │   ├── changepassword.py
│   │   ├── expense.py
│   │   ├── expensecategory.py
│   │   ├── income.py
│   │   ├── incomecategory.py
│   │   ├── login.py
│   │   ├── payment_method.py
│   │   ├── signup.py
│   │   ├── totale.py
│   │   └── __pycache__/
│   └── __pycache__/

├── db.sqlite3                   # SQLite Database
├── manage.py                    # Django manager script
├── venv/                        # Virtual Environment
├── screenshort/
├── .gitignore
├── API_DOCS.md                  # API Documentation
├── requirements.txt             # Installed packages
└── README.md                    # Project Overview
```

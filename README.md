This Django project allows users to manage their income, expenses, and budgets.
It includes features such as category-wise tracking, selection of payment methods, and user authentication for a secure and personalized experience.

# 💰 Expense Tracker – Django Project

A simple yet powerful Expense Tracker built with Django that allows users to manage their incomes, expenses, and budgets efficiently.

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
- Stores `amount`, `category`, `date`, `time`

### 📈 `IncomeCategory`
Stores names of income types (e.g. Salary, Bonus)

### 💸 `Expense`
Tracks expenses:
- Linked to `User`, `ExpenseCategory`, `PaymentMethod`
- Contains `amount`, `category`, `payment_method`, `description`, `date`, `time`

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
git clone https://github.com/Piyushkumarsaini/expense_teacker.git
cd expense_teacker

Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt


Run Migrations
python manage.py makemigrations
python manage.py migrate

Run the Server
python manage.py runserver



📁 Project Structure

├── expense/                          # Main App
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                     # All data models
│   ├── tests.py
│   ├── urls.py                       # URL routing
│   ├── view/                         # Views folder (split by feature)
│   │   ├── budget.py                 # Budget logic
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
│
├── expense_tracker/                 # Project Configuration + Root Files
│   ├── __init__.py
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # Root URL configuration
│   ├── db.sqlite3                   # SQLite Database
│   ├── manage.py                    # Django manager script
│   ├── venv/                        # Virtual Environment
│   └── README.md                    # Project Documentation




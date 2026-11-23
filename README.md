# 💰 Expense Tracker

### 📌 Project Overview

Expense Tracker is a web-based application developed using **Python and Flask** to help users manage and track their daily expenses. It provides a simple and user-friendly interface to add, view, search, edit, and delete expense records.

### 🛠️ Technologies Used

- 🐍 **Python** – Backend programming
- 🌐 **Flask** – Web framework
- 🍃 **MongoDB** – Database management
- 🔗 **PyMongo** – MongoDB connectivity
- 🧱 **HTML** – Webpage structure
- 🎨 **CSS** – Styling and layout

### ✨ Features

- ➕ Add new expenses
- 📋 View all recorded expenses
- 🔍 Search expenses by title and category
- ✏️ Edit existing expense details
- 🗑️ Delete expense records
- 🧮 Calculate the total number of expenses
- 💵 Calculate the total amount spent

### 📂 Project Structure

```text
Expense-Tracker/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   └── view.html
│
├── static/
│   └── style.css
│
└── README.md
```

### 🗄️ Database

This project uses **MongoDB** to store expense records.

- **Database Name:** `expense_tracker`
- **Collection Name:** `expenses`

### ⚙️ Installation and Setup

**1. Install Python**

Make sure Python is installed on your system.

**2. Install MongoDB**

Install MongoDB and ensure that the MongoDB server is running.

**3. Install Required Packages**

Open the terminal in your project folder and execute:

```bash
pip install flask pymongo
```

**4. Run the Application**

```bash
python app.py
```

**5. Open in Browser**

Open the local URL displayed in your terminal (usually `http://127.0.0.1:5000/`).

### 🎯 Project Purpose

This project was developed as an academic project to gain practical experience in Python web development, Flask framework, MongoDB connectivity, and CRUD operations.

### 👩‍💻 Developed By

**Gargi Nalavade**  
🎓 MSc Computer Science

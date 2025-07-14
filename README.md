# 🍽️ Mobile Restaurant Menu App with Kivy

A Python mobile-style GUI application built with [Kivy](https://kivy.org/) that allows users to select food items, view their prices, and calculate the total bill. The app also sends the bill summary to an email address via `yagmail`.

---

## 📸 Preview

![Reference Project Screenshot](https://github.com/Kyara0797/Mobile-Application-with-Python-and-send-emails/blob/main/Reference_Project_Restaurant_Pay_and_Email.png?raw=true)

---

## ✨ Features

- Interactive spinner to choose food items
- Add/remove items dynamically
- Scrollable view with food and price table
- Pop-up summary of total cost
- Email sending functionality with total bill amount
- Custom design using background images and colors

---

## 🚀 Technologies Used

- Python 3
- [Kivy](https://kivy.org/)
- [yagmail](https://github.com/kootenpv/yagmail) for sending emails

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/Kyara0797/Mobile-Application-with-Python-and-send-emails.git)
cd your-repo-name
```
## 2. **Create and activate a virtual environment**
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

## 3.  **Install the requirements**
pip install -r requirements.txt

▶️ **Run the App**
python mobile_application.py

📧 Email Setup
To enable email sending, the app uses a Gmail account. Make sure:

You have allowed App Passwords

You have replaced the hardcoded password and email with your own credentials (or better, use environment variables).

🛡️ Security Warning
Never expose your real email credentials in the code. Use environment variables or a .env file in combination with python-dotenv.

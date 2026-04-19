# QUICK-FIX-PROJECT

# 🔧 QuickFix - Home Services Marketplace

QuickFix is a modern, interactive web application built entirely in Python using **Streamlit**. Inspired by platforms like Urban Company, it serves as a conceptual frontend for a home service marketplace where users can book professionals for AC repair, cleaning, plumbing, and more.

## ✨ Features

- **User Authentication:** Fully functional mock login and sign-up system with dynamic Customer ID generation.
- **Smart Search & Filters:** Browse services via a search bar or click on category buttons (Appliance, Cleaning, Repair, Beauty) to instantly filter results.
- **Shopping Cart System:** Add multiple services to a cart, view the dynamic total price, and manage your selections.
- **Secure Checkout Flow:** A multi-step mock checkout requiring delivery address, schedule selection, and payment method.
- **Partner Portal:** A dedicated application form for professionals wanting to join the QuickFix platform.
- **Session Management:** The app remembers your cart and login status across different pages using Streamlit's Session State.

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Frontend Framework:** [Streamlit](https://streamlit.io/)
- **Data:** Mock JSON/Dictionary data handling

## 🚀 How to Run Locally

Follow these steps to get the QuickFix app running on your local machine:

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/quickfix.git](https://github.com/your-username/quickfix.git)
cd quickfix
2. Create a virtual environment (Recommended)

Bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies

Bash
pip install streamlit
4. Run the application

Bash
streamlit run app.py
The app will automatically open in your default web browser at http://localhost:8501.

📁 Project Structure
Plaintext
quickfix/
│
├── app.py               # Main Streamlit application file
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
🧠 Future Enhancements
Connect to a real backend (Node.js/Express or Python/FastAPI) and database (MongoDB/PostgreSQL).

Add integration for real payment gateways (Stripe/Razorpay).

Implement a live tracking dashboard for booked services.

Allow users to leave actual reviews and ratings.

🤝 Contributing
Contributions, issues, and feature requests are welcome!

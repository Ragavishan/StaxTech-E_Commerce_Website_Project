🛒 **StaxTech E-Commerce Website Project**

Welcome to the StaxTech E-Commerce Website — a simple yet powerful online store built with Flask and SQLite!
This project showcases a full-stack web app where users can register, browse products, add items to a cart, and leave reviews. 🚀

✨ Features
🔐 User Authentication: Register, login, and logout securely

🛍️ Product Catalog: Browse products with images, descriptions, and prices

🛒 Shopping Cart: Add/remove products and review cart contents

💳 Checkout Flow: Simulated payment and order confirmation

⭐ Product Reviews: Leave ratings and comments for products

💾 SQLite Database: Persistent storage for users, products, and reviews


🚀 Getting Started
1. Clone this repository
bash
Copy code
git clone https://github.com/Ragavishan/StaxTech-E-Commerce-Website-project-1.git
cd StaxTech-E-Commerce-Website-project-1
2. Create a virtual environment (recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install Flask
4. Run the application
bash
Copy code
python app.py   🛒

🗂️ Database Info
The app auto-creates products.db on first run

Contains tables for products, users, and reviews

Comes preloaded with example products

🎯 How to Use
Create a new account or log in with existing credentials

Browse products on the homepage

Click a product for detailed view and reviews

Add your favorite products to the cart

Manage cart contents and proceed to checkout

After payment, your cart will be cleared

Log out when you’re done

⚠️ Important Notes
Passwords are stored in plain text — not safe for production!

Consider adding password hashing and security best practices before deployment

Product images are linked externally for demonstration purposes only

📄 License
This project is licensed under the MIT License. 

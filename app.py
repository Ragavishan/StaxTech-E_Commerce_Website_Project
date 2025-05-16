from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Connection
def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize Database (Run once)
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS products 
                    (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, image TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS users 
                    (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS reviews 
                    (id INTEGER PRIMARY KEY, product_id INTEGER, username TEXT, rating INTEGER, comment TEXT)''')
    conn.execute("DELETE FROM products")  # Clear existing products
    conn.execute("INSERT INTO products (name, description, price, image) VALUES ('Laptop', 'High-performance laptop', 750.00, 'https://assets.mediamodifier.com/mockups/5b053bb8306e03fd32cc5e78/ecommerce-laptop-mockup-with-a-shopping-cart.jpg')")
    conn.execute("INSERT INTO products (name, description, price, image) VALUES ('Headphones', 'Noise-canceling headphones', 120.00, 'https://cdn.dribbble.com/userupload/7092498/file/original-0f5c93117695edf02efad37f65980d08.jpg?resize=400x0')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    reviews = conn.execute('SELECT * FROM reviews WHERE product_id = ?', (product_id,)).fetchall()
    conn.close()
    if not product:
        return redirect(url_for('index'))
    return render_template('product_detail.html', product=product, reviews=reviews)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    
    if product:
        cart = session.get('cart', [])
        cart.append(dict(product))
        session['cart'] = cart
    
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    session['cart'] = [item for item in cart if item['id'] != product_id]
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    cart_items = session.get('cart', [])
    return render_template('checkout.html', cart_items=cart_items)

@app.route('/process_payment')
def process_payment():
    flash("Payment Successful!")
    session.pop('cart', None)  # Clear cart after checkout
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            pass
        conn.close()
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Run once to initialize DB
    app.run(debug=True)

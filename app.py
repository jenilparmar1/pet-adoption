from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('petdb.db')  # Adjust the path as needed
    conn.row_factory = sqlite3.Row  # Enable row access by name
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        state = request.form['state']
        
        # Connect to the database and insert the user data
        conn = get_db_connection()
        conn.execute('INSERT INTO users (name, username, email, password, state) VALUES (?, ?, ?, ?, ?)',(name, username, email, password, state))
        conn.commit()
        conn.close()
        
        # Redirect to the login page on VS Code Live Server
        return redirect("http://127.0.0.1:5500/template/login.html")
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username_or_email = request.form['username']
            password = request.form['password']
            
            print(f"Received login attempt with username/email: {username_or_email}")  # Debugging info

            conn = get_db_connection()
            user = conn.execute('SELECT * FROM users WHERE (username = ? OR email = ?) AND password = ?', 
                                (username_or_email, username_or_email, password)).fetchone()
            conn.close()
            
            if user:
                print("Login successful!")  # Debugging info
                return jsonify(success=True, redirect_url='http://127.0.0.1:5500/index.html')
                print("Sending JSON response:", response.get_json())  # Debugging info
                return response
            else:
                print("Invalid username/email or password.")  # Debugging info
                return jsonify(success=False, error="Invalid username/email or password.")
                print("Sending JSON response:", response.get_json())  # Debugging info
                return response
        except Exception as e:
            print(f"Error: {e}")  # Debugging info for any errors
            return jsonify(success=False, error="An internal server error occurred.")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

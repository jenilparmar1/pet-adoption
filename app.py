from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

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
        return redirect("http://127.0.0.1:5500/login.html")
    
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to DB and create table (run once)
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS joining_form (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT
            -- Add other fields as per your form
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nomination')
def nomination():
    return render_template('nomination_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    # Fetch other form fields similarly

    # Save to database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO joining_form (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

    return redirect(url_for('nomination'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)


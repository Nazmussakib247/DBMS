from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Leave empty if no password is set
    'database': 'railway_booking'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Create tables if they don't exist
def initialize_database():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL UNIQUE,
                    email VARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    password VARCHAR(100) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trains (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    destination VARCHAR(100) NOT NULL,
                    train_name VARCHAR(100) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    train_id INT,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    coach VARCHAR(10) NOT NULL,
                    seat VARCHAR(10) NOT NULL,
                    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (train_id) REFERENCES trains(id)
                )
            ''')
            conn.commit()
        except Error as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()
            conn.close()

# Initialize the database
initialize_database()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
                user = cursor.fetchone()
                if user:
                    session['username'] = username
                    session['user_id'] = user['id']
                    return redirect(url_for('destinations'))
                else:
                    return render_template('login.html', error='Invalid username or password')
            except Error as e:
                print(f"Error during login: {e}")
                return render_template('login.html', error='Database error')
            finally:
                cursor.close()
                conn.close()
        else:
            return render_template('login.html', error='Database connection error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    'INSERT INTO users (username, email, age, password) VALUES (%s, %s, %s, %s)',
                    (username, email, age, password)
                )
                conn.commit()
                return redirect(url_for('login'))
            except mysql.connector.IntegrityError:
                return render_template('register.html', error='Username already exists')
            except Error as e:
                print(f"Error during registration: {e}")
                return render_template('register.html', error='Database error')
            finally:
                cursor.close()
                conn.close()
        else:
            return render_template('register.html', error='Database connection error')
    return render_template('register.html')

@app.route('/destinations', methods=['GET', 'POST'])
def destinations():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        destination = request.form['destination']
        session['destination'] = destination
        return redirect(url_for('trains'))
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT DISTINCT destination FROM trains')
            destinations = [row[0] for row in cursor.fetchall()]
            return render_template('destinations.html', destinations=destinations)
        except Error as e:
            print(f"Error fetching destinations: {e}")
            return "Database error"
        finally:
            cursor.close()
            conn.close()
    else:
        return "Database connection error"

@app.route('/trains', methods=['GET', 'POST'])
def trains():
    if 'username' not in session or 'destination' not in session:
        return redirect(url_for('login'))
    destination = session['destination']
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute('SELECT * FROM trains WHERE destination = %s', (destination,))
            available_trains = cursor.fetchall()
            if request.method == 'POST':
                train_id = request.form['train']
                session['train_id'] = train_id
                return redirect(url_for('book_ticket'))
            return render_template('trains.html', trains=available_trains)
        except Error as e:
            print(f"Error fetching trains: {e}")
            return "Database error"
        finally:
            cursor.close()
            conn.close()
    else:
        return "Database connection error"

@app.route('/book_ticket', methods=['GET', 'POST'])
def book_ticket():
    if 'username' not in session or 'train_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        user_id = session['user_id']
        train_id = session['train_id']
        name = request.form['name']
        age = request.form['age']
        coach = request.form['coach']
        seat = request.form['seat']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    'INSERT INTO bookings (user_id, train_id, name, age, coach, seat) VALUES (%s, %s, %s, %s, %s, %s)',
                    (user_id, train_id, name, age, coach, seat)
                )
                conn.commit()
                return redirect(url_for('success'))
            except Error as e:
                print(f"Error booking ticket: {e}")
                return "Database error"
            finally:
                cursor.close()
                conn.close()
        else:
            return "Database connection error"
    
    return render_template('book_ticket.html')

@app.route('/success')
def success():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            # Fetch the latest booking
            cursor.execute('SELECT * FROM bookings WHERE user_id = %s ORDER BY id DESC LIMIT 1', (session['user_id'],))
            booking = cursor.fetchone()

            # Fetch user details
            cursor.execute('SELECT * FROM users WHERE id = %s', (session['user_id'],))
            user = cursor.fetchone()

            return render_template('success.html', booking=booking, user=user)
        except Error as e:
            print(f"Error fetching booking details: {e}")
            return "Database error"
        finally:
            cursor.close()
            conn.close()
    else:
        return "Database connection error"

@app.route('/booking_history')
def booking_history():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            # Fetch all bookings for the user
            cursor.execute('''
                SELECT bookings.*, trains.destination, trains.train_name 
                FROM bookings 
                JOIN trains ON bookings.train_id = trains.id 
                WHERE user_id = %s
                ORDER BY booking_date DESC
            ''', (session['user_id'],))
            bookings = cursor.fetchall()

            # Fetch user details
            cursor.execute('SELECT * FROM users WHERE id = %s', (session['user_id'],))
            user = cursor.fetchone()

            return render_template('booking_history.html', bookings=bookings, user=user)
        except Error as e:
            print(f"Error fetching booking history: {e}")
            return "Database error"
        finally:
            cursor.close()
            conn.close()
    else:
        return "Database connection error"

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    session.pop('destination', None)
    session.pop('train_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
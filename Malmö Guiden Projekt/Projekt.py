from flask import Flask, render_template, request, redirect, url_for, session
import json
import hashlib

app = Flask(__name__, static_url_path='/static')

app = Flask(__name__)

""" users = {} """

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password, salt = hash_password(password)
        if register_user(username, email, hashed_password, salt):
            return redirect('/')
        else:
            return "Användarnamnet är upptaget"
    return render_template('register.html')

def register_user(username, email, hashed_password, salt):
    """ global users """
    with open('Malmö Guiden Projekt/static/users.json', 'r') as file:
        users = dict(json.load(file))
    if username in users:
        return False # användaren finns redan
    users[username] = {
        'email': email,
        'password': hashed_password,
        'salt': salt
    }
    with open('Malmö Guiden Projekt/static/users.json', 'w') as file:
        json.dump(users, file, indent=4)
    return True # användaren har registrerats

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ global users """
    if request.method == 'POST':
        # Hämta användarnamn och lösenord från formuläret
        username = request.form['username']
        password = request.form['password']

        with open('Malmö Guiden Projekt/static/users.json', 'r') as file:
            users = dict(json.load(file))
        # Kontrollera om användarnamnet och lösenordet matchar en användare i JSON-filen
        if username in users and users[username]['password'] == hashlib.sha256((password + users[username]['salt']).encode('utf-8')).hexdigest():
            # Spara användarnamnet som en session-variabel och gå till startsidan
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            # Om användarnamnet eller lösenordet är felaktigt, visa ett felmeddelande
            return render_template('login.html', error='Felaktigt användarnamn eller lösenord')

    return render_template('login.html')

def hash_password(password):
    # Skapa en slumpmässig sträng (salt) för att öka säkerheten
    salt = "randomstring"
    # Kombinera lösenord och salt
    salted_password = password + salt
    # Skapa hash med SHA-256 algoritmen
    hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
    # Returnera hashvärdet och saltet
    return hashed_password, salt

@app.route('/dashboard')
def dashboard():
    # Kontrollera om användaren är inloggad genom att kolla om session-variabeln är satt
    if 'username' in session:
        # Hämta användaruppgifter från JSON-filen
        user = session['username']
        return render_template('dashboard.html', user=user)
    else:
        # Om användaren inte är inloggad, gå till inloggningssidan
        return redirect(url_for('login'))

@app.route('/sevardheter')
def sevardheter():
    return render_template('sevardheter.html')

@app.route('/boenden')
def boenden():
    return render_template('boenden.html')

@app.route('/restauranger')
def restauranger():
    return render_template('restauranger.html')

@app.route('/shopping')
def shopping():
    return render_template('shopping.html')

@app.route('/evenemang')
def evenemang():
    return render_template('evenemang.html')

@app.route('/uteliv')
def uteliv():
    return render_template('uteliv.html')

@app.route('/kultur')
def kultur():
    return render_template('kultur.html')

@app.route('/dolda-parlor')
def dolda_parlor():
    return render_template('dolda_parlor.html')

@app.route('/sport')
def sport():
    return render_template('sport.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.secret_key = 'mysecretkey'
    app.run(debug=True)

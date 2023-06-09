#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions
import re

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/storeRecords.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)
order = {}

@app.route('/search', methods=['POST'])
def perform_search():
    search_query = request.form['search']
    search_results = db.execute("SELECT * FROM inventory WHERE item_name LIKE :query", {"query": f"%{query}%"}).fetchall()
    return render_template('results.html', results=search_results)

@app.route('/search')
def search():
    query = request.args.get('search')
    # Perform search logic on your data store
    results = perform_search(query)
    return render_template('results.html', results=results)

@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        sessions.add_new_session(username, db)
        return render_template('home.html', products=products, sessions=sessions)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html')


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/storeRecords.db: adds a new user to the database
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    
    
    user_session = sessions.get_session(username)
    for item in products:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)

    user_session.submit_cart()

    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)

@app.route('/payment')
def payment_page():
    """
    Renders the Payment page when the user is at the 'payment' endpoint

    args:
        - None
    
    returns:
        - None
    
    modifies:
        - sessions: adds payment info 
    """

    return render_template('payment.html')
@app.route('/finish', methods=['POST'])
def payment():
    """
    Renders the Payment page when the user is at the 'payment' endpoint with a post request

 v    args:
        - None
    
    returns:
        - None
    
    modifies:
        - None
    """
    
    card_num = re.sub('[^0-9]','',request.form['card number'])
    exp_date = re.sub('[^0-9]','',request.form['exp date'])
    

    if(len(card_num) != 16 or len(exp_date) != 4 or int(exp_date[2:]) < 23 or len(request.form['CVV']) != 3 or len(request.form['zip']) != 5 ):
        return render_template('payment.html')
    return render_template('finish.html', order = order)
    

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)

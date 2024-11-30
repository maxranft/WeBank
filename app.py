from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webank.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create database tables when the app starts
with app.app_context():
    db.create_all()

# Route for Home Page
@app.route('/')
def home():
    from models import User  # Importing inside route to avoid circular import
    user = User.query.first()  # Fetch first user for demo
    return render_template('home.html', user=user)

# Route for Marketplace
@app.route('/marketplace')
def marketplace():
    from models import NFT  # Importing inside route
    nft_list = NFT.query.all()  # Fetch all NFTs
    return render_template('marketplace.html', nft_list=nft_list)


# Route for Login
@app.route('/login')
def login():
    return render_template('login.html')

return app
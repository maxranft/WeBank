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

# Route for Wallet
@app.route('/wallet')
def wallet():
    from models import Wallet  # Importing inside route
    user = Wallet.query.first()  # Assuming we have a Wallet model for users
    wallet_balances = [
        {"name": "Bitcoin", "symbol": "BTC", "amount": user.bitcoin_balance},
        {"name": "Ethereum", "symbol": "ETH", "amount": user.ethereum_balance},
        {"name": "USDC", "symbol": "USDC", "amount": user.usdc_balance},
    ]
    return render_template('wallet.html', wallet_balances=wallet_balances)

# Route for Login
@app.route('/login')
def login():
    return render_template('login.html')

# Route for Signup
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
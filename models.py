from app import db  # This will work because db is initialized after Flask app starts

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

# Define NFT model
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define Wallet model
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bitcoin_balance = db.Column(db.Float, default=0.0)
    ethereum_balance = db.Column(db.Float, default=0.0)
    usdc_balance = db.Column(db.Float, default=0.0)

    user = db.relationship('User', backref=db.backref('wallet', lazy=True))

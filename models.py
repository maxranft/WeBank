from app import db

# User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    # Relationships
    transactions = db.relationship('Transaction', backref='user', lazy=True)
    wallet = db.relationship('Wallet', uselist=False, backref='user')  # One-to-One relationship

    def __repr__(self):
        return f'<User {self.username}>'

# Transaction model
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Options: "deposit" or "withdrawal"
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Transaction {self.type} - Amount: {self.amount}>'

# Wallet model
class Wallet(db.Model):
    __tablename__ = 'wallets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Wallet UserID: {self.user_id} - Balance: {self.balance}>'

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref('nfts', lazy=True))

    def __repr__(self):
        return f"<NFT {self.name}>"

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('wallet', lazy=True))

    def __repr__(self):
        return f"<Wallet User {self.user_id} Balance {self.balance}>"

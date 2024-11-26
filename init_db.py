from app import db
from models import User, NFT, Wallet

# Create the tables if they do not exist
db.create_all()

# Add some initial data for testing
user = User(username="john_doe", email="john@example.com", password="password123")
db.session.add(user)
db.session.commit()

# Add some NFTs
nft1 = NFT(title="CryptoArt 1", image_url="https://example.com/nft1.jpg", price=2.5)
nft2 = NFT(title="CryptoArt 2", image_url="https://example.com/nft2.jpg", price=3.0)
db.session.add(nft1)
db.session.add(nft2)
db.session.commit()

# Add a wallet for the user
wallet = Wallet(user_id=user.id, bitcoin_balance=1.5, ethereum_balance=10.0, usdc_balance=500.0)
db.session.add(wallet)
db.session.commit()

# Initialize the database
def init_db():
    with db.engine.connect() as conn:
        db.create_all()  # Create tables

if __name__ == "__main__":
    init_db()
    print("DB Initialization tables created successfully")


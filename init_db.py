from app import create_app
from extensions import db

# Create the app
app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()
    print("Database initialized!")
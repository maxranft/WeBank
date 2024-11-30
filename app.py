from flask import Flask, render_template
from extensions import db
from models import User, NFT, Wallet

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webank.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/wallet")
    def wallet():
        return render_template("wallet.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webank.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session and flash messages

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Models
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)

        def __repr__(self):
            return f'<User {self.username}>'

    # Routes
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/wallet")
    def wallet():
        return render_template("wallet.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/nfts")
    def nfts():
        return render_template("nfts.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            username = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            confirm_password = request.form["confirm_password"]

            # Validate form data
            if password != confirm_password:
                flash("Passwords do not match", "danger")
                return redirect(url_for("signup"))

            # Check if user already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email already in use", "warning")
                return redirect(url_for("signup"))

            # Hash the password and create a new user
            hashed_password = generate_password_hash(password, method="sha256")
            new_user = User(username=username, email=email, password=hashed_password)

            # Add to the database
            db.session.add(new_user)
            db.session.commit()

            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for("login"))

        return render_template("signup.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            # Fetch user from the database
            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                # Store user ID in the session
                session["user_id"] = user.id
                flash("Logged in successfully!", "success")
                return redirect(url_for("home"))
            else:
                flash("Invalid email or password", "danger")

        return render_template("login.html")


    return app

# Create the Flask app instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
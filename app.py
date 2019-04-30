from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from posts.routes import posts
from users.routes import users
from main.routes import main


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.register_blueprint(posts)
app.register_blueprint(users)
app.register_blueprint(main)

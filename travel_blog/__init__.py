from travel_blog.config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    from travel_blog.posts.routes import posts
    from travel_blog.users.routes import users
    from travel_blog.main.routes import main
    app.register_blueprint(posts)
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app

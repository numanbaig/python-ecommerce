from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.Config')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

def register_blueprints():
    from routes.auth import auth_bp
    from routes.products import products_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    register_blueprints()
    app.run(debug=True)
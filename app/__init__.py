from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api 
from flask_cors import CORS # autorizar o acesso
app = Flask(__name__)
CORS(app)
api = Api(app)
#configuração com banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud4.db'
db = SQLAlchemy(app)
from app.models.products import Products
with app.app_context():
    db.create_all()

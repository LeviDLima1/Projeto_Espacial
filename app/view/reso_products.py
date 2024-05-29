from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.products import Products

#para adicionar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str)
argumentos.add_argument('data_lancamento', type=)
argumentos.add_argument()
argumentos.add_argument()
argumentos.add_argument()
argumentos.add_argument()
argumentos.add_argument()
argumentos.add_argument()
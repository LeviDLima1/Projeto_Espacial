from flask import jsonify
from flask_restful import Resource, reqparse
from datetime import datetime
from app.models.products import Products

#para adicionar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str, required=True, help="O name nao pode ficar em branco!")
argumentos.add_argument('data_lancamento', type=lambda x: datetime.strptime(x, '%Y-%m-%d').date(), required=True, help="Data_lancamento nao pode ficar em branco!")
argumentos.add_argument('destino', type=str, required=True, help="O destino nao pode ficar em branco!")
argumentos.add_argument('estado_missao', type=str, required=True, help="O estado_missao nao pode ficar em branco!")
argumentos.add_argument('tripulacao', type=str, required=True, help="A tripulacao nao pode ficar em branco!")
argumentos.add_argument('carga_util', type=str, required=True, help="A carga_util nao pode ficar em branco!")
argumentos.add_argument('duracao_missao', type=int, required=True, help="A duracao_missao nao pode ficar em branco!")
argumentos.add_argument('missao_custo', type=float, required=True, help="O missao_custo nao pode ficar em branco!")
argumentos.add_argument('missao_status', type=str, required=True, help="O missao_status nao pode ficar em branco!")

from flask import jsonify
from flask_restful import Resource, reqparse
from datetime import datetime
from app.models.products import Products
import re

#para adicionar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str, required=True, help="O name nao pode ficar em branco!")
argumentos.add_argument('data_lancamento', type=lambda x: datetime.strptime(x, '%Y-%m-%d').date(), required=True, help="Data_lancamento nao pode ficar em branco!")
argumentos.add_argument('destino', type=str, required=True, help="O destino nao pode ficar em branco!")
argumentos.add_argument('estado_missao', type=str, required=True, help="O estado_missao nao pode ficar em branco!")
argumentos.add_argument('tripulacao', type=str, required=True, help="A tripulacao nao pode ficar em branco!")
argumentos.add_argument('carga_util', type=str, required=True, help="A carga_util nao pode ficar em branco!")
argumentos.add_argument('duracao_missao', type=str, required=True, help="A duracao_missao nao pode ficar em branco!")
argumentos.add_argument('missao_custo', type=float, required=True, help="O missao_custo nao pode ficar em branco!")
argumentos.add_argument('missao_status', type=str, required=True, help="O missao_status nao pode ficar em branco!")

#para atualizar
argumentos_update = reqparse.RequestParser() #definir os argumentos da solicitação HTTP
argumentos_update.add_argument('id', type=int, required=True, help="O id nao pode ficar em branco!")
argumentos_update.add_argument('name', type=str, required=True, help="O name nao pode ficar em branco!")
argumentos_update.add_argument('data_lancamento', type=lambda x: datetime.strptime(x, '%Y-%m-%d').date(), required=True, help="Data_lancamento nao pode ficar em branco!")
argumentos_update.add_argument('destino', type=str, required=True, help="O destino nao pode ficar em branco!")
argumentos_update.add_argument('estado_missao', type=str, required=True, help="O estado_missao nao pode ficar em branco!")
argumentos_update.add_argument('tripulacao', type=str, required=True, help="A tripulacao nao pode ficar em branco!")
argumentos_update.add_argument('carga_util', type=str, required=True, help="A carga_util nao pode ficar em branco!")
argumentos_update.add_argument('duracao_missao', type=str, required=True, help="A duracao_missao nao pode ficar em branco!")
argumentos_update.add_argument('missao_custo', type=float, required=True, help="O missao_custo nao pode ficar em branco!")
argumentos_update.add_argument('missao_status', type=str, required=True, help="O missao_status nao pode ficar em branco!")

#deletar
argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('id', type=int, required=True, help="O id nao pode ficar em branco!")

def parse_duration(duration_str):
    pattern = re.compile(r'^\d+\s*dias,\s*\d+\s*horas,\s*\d+\s*minutos$')
    if not pattern.match(duration_str):
        raise ValueError("Formato de duração inválido. Use o formato 'X dias, Y horas, Z minutos")
    
    days, hours, minutes = 0, 0, 0
    for part in duration_str.split(','):
        if 'dias' in part:
            days = int(part.split()[0])
        elif 'horas' in part:
            hours = int(part.split()[0])
        elif 'minutos' in part:
            minutes = int(part.split()[0])
    return days * 86400 + hours * 3600 + minutes * 60

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")
    
class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            try:
                duracao_missao_segundos = parse_duration(datas['duracao_missao'])
            except ValueError as e:
                return jsonify({'status': 400, 'msg': str(e)}), 400
            Products.save_products(self, datas['name'], datas['data_lancamento'], datas['destino'], datas['estado_missao'], datas['tripulacao'], datas['carga_util'], duracao_missao_segundos, datas['missao_custo'], datas['missao_status'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class ProductUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            try:
                duracao_missao_segundos = parse_duration(datas['duracao_missao'])
            except ValueError as e:
                return jsonify({'status': 400, 'msg': str(e)}), 400
            Products.update_products(self, datas['id'], 
            datas['name'], datas['data_lancamento'], datas['destino'], datas['estado_missao'], datas['tripulacao'], datas['carga_util'], duracao_missao_segundos, datas['missao_custo'], datas['missao_status'])
            return {"message": 'Products update successfully!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class ProductDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            Products.delete_products(self, datas['id'])
            return {"message": 'Products delete successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
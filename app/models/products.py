from app import db
from datetime import timedelta

class Products(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    data_lancamento = db.Column(db.Date())
    destino = db.Column(db.String(255))
    estado_missao = db.Column(db.String(255))
    tripulacao = db.Column(db.String(255))
    carga_util = db.Column(db.String(255))
    duracao_missao = db.Column(db.Integer())
    missao_custo = db.Column(db.Numeric(20, 2))
    missao_status = db.Column(db.Text())


    def __init__(self, name, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, missao_custo, missao_status):
        self.name = name
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.estado_missao = estado_missao
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao_missao = duracao_missao
        self.missao_custo = missao_custo
        self.missao_status = missao_status

    def save_products(self, name, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, missao_custo, missao_status):
        try:
            add_banco = Products(name, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, missao_custo, missao_status)
            print(add_banco)
            db.session.add(add_banco) 
            db.session.commit()
        except Exception as e:
            print(e)

    def update_products(self, id, name, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, missao_custo, missao_status):
        try:
            db.session.query(Products).filter(Products.id==id).update({"name":name,"data_lancamento":data_lancamento,"destino":destino,"estado_missao":estado_missao,"tripulacao":tripulacao,"carga_util":carga_util,"duracao_missao":duracao_missao,"missao_custo":missao_custo,"missao_status":missao_status})
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)

    def delete_products(self, id):
        try:
            db.session.query(Products).filter(Products.id==id).delete()
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)

    def __repr__(self):
        duracao = timedelta(seconds=self.duracao_missao)
        dias = duracao.days
        horas, resto = divmod(duracao.seconds, 3600)
        minutos = resto // 60
        
        duracao_formatada = f"{dias} dias, {horas} horas, {minutos} minutos"
        return f"<Products(id={self.id}, name='{self.name}', duracao_missao='{duracao_formatada}')>"

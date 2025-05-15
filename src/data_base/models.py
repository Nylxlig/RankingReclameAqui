from src.data_base import db

class TopicModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    topic_name = db.Column(db.String(100))
    topic_companies = db.Column(db.ARRAY(db.Integer), nullable = True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'topic_name': self.topic_name,
            'topic_companies': self.topic_companies
        }

class CompanyModel(db.Model):
    __tablename__ = 'company_model'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    link = db.Column(db.String(100), nullable = False)
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "link": self.link}
    
class CompanyInfoModel(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    id_company = db.Column(db.Integer, db.ForeignKey('company_model.id'))
    reclamacao = db.Column(db.String(20), nullable = True)

    def to_dict(self):
        return{
            "id":self.id,
            "id_company": self.id_company,
            "reclamacao": self.reputacao
        }

class CompanyInfoModel_reserva(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    id_company = db.Column(db.Integer, db.ForeignKey('company_model.id'))
    site_name = db.Column(db.String(100), nullable = True)
    reputacao = db.Column(db.String(20), nullable = True)
    recebeu_qtd = db.Column(db.String(10), nullable = True) 
    aguardam_resposta = db.Column(db.String(10), nullable = True) 
    reclamacoes_avaliadas = db.Column(db.String(10), nullable = True) 
    nota_media_semestre = db.Column(db.String(10), nullable = True) 
    tempo_medio_resposta = db.Column(db.String(20), nullable = True) 
    respondeu_qtd_porcento = db.Column(db.String(10), nullable = True) 
    nota_media_consumidores = db.Column(db.String(10), nullable = True) 
    voltariam_negocio_porcento = db.Column(db.String(10), nullable = True) 
    resolveu_reclamacoes_recebidas_porcento = db.Column(db.String(10), nullable = True)

    def to_dict(self):
        return {
            "id": self.id,
            "site_name" :self.site_name,
            "reputacao": self.reputacao,
            "recebeu_qtd": self.recebeu_qtd,
            "aguardam_resposta": self.aguardam_resposta,
            "reclamacoes_avaliadas": self.reclamacoes_avaliadas,
            "nota_media_semestre": self.nota_media_semestre,
            "tempo_medio_resposta": self.tempo_medio_resposta,
            "respondeu_qtd_porcento": self.respondeu_qtd_porcento,
            "nota_media_consumidores": self.nota_media_consumidores,
            "voltariam_negocio_porcento": self.voltariam_negocio_porcento,
            "resolveu_reclamacoes_recebidas_porcento": self.resolveu_reclamacoes_recebidas_porcento,
        }
    
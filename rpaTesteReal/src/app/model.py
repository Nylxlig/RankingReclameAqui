from src.app.database import db

class TopicModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    topic_name = db.Column(db.String(100))
    topic_companies = db.Column(db.String(500), nullable = True)
    
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
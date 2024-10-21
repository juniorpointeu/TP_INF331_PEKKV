from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class candidat(db.Model):
    __tablename__ = 'candidats'

    id = db.Column(db.Integer, primary_key=True)
    sexe = db.Column(db.String(10))
    age = db.Column(db.Integer)
    annees_experience = db.Column(db.Integer)
    mention_bac = db.Column(db.String(50))
    mention_licence = db.Column(db.String(50))
    specialite_licence = db.Column(db.String(50))
    dernier_diplome = db.Column(db.String(50))
    langues_parlees = db.Column(db.String(100))
    connaissance_softwares = db.Column(db.String(100))
    experience_management = db.Column(db.Integer)
    stage_effectue = db.Column(db.Boolean)
    recrute = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Candidat {self.id}>'

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models.DAO import candidat  # Assurez-vous que Candidat est correctement importé

app = Flask(__name__,template_folder='app/views/templates')
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html') 

# Vous pouvez ajouter d'autres routes ici selon vos besoins

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/site_commerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Produit(db.Model):
    __tablename__ = 'produit'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boutique')
def boutique():
    tous_les_produits = Produit.query.all()
    return render_template('boutique.html', produits=tous_les_produits)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
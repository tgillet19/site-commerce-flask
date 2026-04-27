from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boutique')
def boutique():
    # Données riches pour un rendu professionnel
    items = [
        {
            'id': 1,
            'nom': 'Pack Setup Gaming', 
            'prix': 1299, 
            'desc': 'Le setup complet : PC, écran 144Hz et clavier méca.',
            'img': 'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=500'
        },
        {
            'id': 2,
            'nom': 'Casque Surround 7.1', 
            'prix': 89, 
            'desc': 'Immersion totale avec réduction de bruit active.',
            'img': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500'
        },
        {
            'id': 3,
            'nom': 'Souris Esport RGB', 
            'prix': 55, 
            'desc': 'Capteur 16000 DPI pour une précision chirurgicale.',
            'img': 'https://images.unsplash.com/photo-1527698266440-12104e498b76?w=500'
        }
    ]
    return render_template('boutique.html', produits=items)

if __name__ == '__main__':
    print("\n🚀 SERVEUR BOUTIQUE V2.0 LANCÉ")
    app.run(debug=True)
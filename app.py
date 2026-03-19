from flask import Flask

app = Flask(__name__)

@app.route('/exercice')
def exercice():
    # Remplacez par votre nom et prénom
    prenom = "Dalila"
    nom = "Ben Saada"
    return f"<h1>{prenom} {nom}</h1>"

if __name__ == '__main__':
    # L'application écoute sur le port 5000 par défaut
    # Si le port est pris, vous pouvez changer le port ici
    app.run(host='0.0.0.0', port=5600)

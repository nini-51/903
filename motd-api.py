import os
from flask import Flask, jsonify

app = Flask(__name__)

# Récupération des variables d'environnement ou valeurs par défaut
MESSAGE = os.environ.get('MESSAGE', 'Hello, world!')
APP_PORT = int(os.environ.get('APP_PORT', 5000))

# Route pour le message du jour
@app.route('/')
def motd():
    return jsonify({'message': MESSAGE})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=APP_PORT)

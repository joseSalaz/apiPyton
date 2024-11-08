# api_python.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/python', methods=['GET'])
def api_python():
    # Llama a la siguiente API en la cadena
    next_url = ""
    response = requests.get(next_url)
    data = response.json()
    
    # Agrega su propio mensaje al resultado
    data['chain'].append("Hello from Python!")
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")

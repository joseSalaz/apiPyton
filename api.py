from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/python', methods=['GET'])
def api_python():
    # Llama a la siguiente API en la cadena
    next_url = "http://www.apic.somee.com/Somee"
    response = requests.get(next_url)
    
    # Verificar si la respuesta es un texto o un JSON
    if response.status_code == 200:
        try:
            # Intentar interpretar la respuesta como JSON
            data = response.json()
        except ValueError:
            # Si no es un JSON, manejarlo como texto
            data = {"message": response.text}
        
        # Agregar su propio mensaje al resultado
        if isinstance(data, dict):
            data['chain'] = data.get('chain', []) + ["Hello from Python!"]
        
        return jsonify(data)
    else:
        return jsonify({"error": "Error al obtener datos de la API externa"}), 500

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")

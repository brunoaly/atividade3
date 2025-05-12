from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def soma():
    data = request.get_json()
    resultado = data['a'] + data['b']
    return jsonify({'resultado': resultado})

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    data = request.get_json()
    resultado = data['a'] * data['b']
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
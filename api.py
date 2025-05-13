from flask import Flask, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)

api = Api(app, version="1.0", title="Atividade 3",
          description="Atividade 3 do meu mano André")

ns = api.namespace('Operações', description='Operações matemáticas')

operation_model = api.model('Operation', {
    'num1': fields.Float(required=True, description='Primeiro número'),
    'num2': fields.Float(required=True, description='Segundo número')
})

@ns.route('/soma')
class Soma(Resource):
    @api.expect(operation_model)
    def post(self):
        """Soma dois números"""
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        return {'resultado': num1 + num2}

@ns.route('/multiplicacao')
class Multiplicacao(Resource):
    @api.expect(operation_model)
    def post(self):
        """Multiplica dois números"""
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        return {'resultado': num1 * num2}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='My API', description='A simple example API')

# Modèle de données pour la réponse
todo = api.model('Todo', {
    'id': fields.Integer,
    'task': fields.String,
})

# Ressource Todo
@api.route('/todos')
class TodoList(Resource):
    def get(self):
        # ... (logique pour récupérer la liste des tâches)
        return {'todos': todos}

    @api.expect(todo)
    def post(self):
        # ... (logique pour créer une nouvelle tâche)
        return {'message': 'Todo created'}, 201
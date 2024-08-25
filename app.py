from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}  # This should now return the JSON response without the error

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Assuming you intend to run on port 5001 in debug mode
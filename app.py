from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GetRequestReceiver(Resource):
    def get(self):
        print(f"received_data: {request.args}")
        return {'received_data': request.args}

api.add_resource(GetRequestReceiver, '/')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
from flask_restful import Resource, Api
from os import system

system("clear")
app = Flask(__name__)
api = Api(app)

class GetRequestReceiver(Resource):
    def get(self):
        #print(request.args.get('test'))
        print(request.args.to_dict())
        return {'received_dataaa': request.args}

    def post(self):
        data = request.get_json()  # Get the JSON data from the request
        print (data)
        return {'received_data': data}

api.add_resource(GetRequestReceiver, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context='adhoc')

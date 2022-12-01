from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from predict import *

app = Flask(__name__)
api = Api(app)
CORS(app)

rest = {
    'out1': 'kokok',
    'out2': 'wawaawa',
    'out3': 'duarrr',
    'out4': 'ancok'
}

class Home(Resource):
    def get(self):
        return rest, 200

    def post(self):
        # ab = request.get_json()
        return request.get_json(), 200

class Predicc(Resource):
    def post(self):
        dict_inpt = request.get_json()
        inp1 = dict_inpt['inp_1']
        inp2 = dict_inpt['inp_2']
        inp3 = dict_inpt['inp_3']
        inp4 = dict_inpt['inp_4']
        
        for i in [inp1, inp2, inp3, inp4]:
            pass

        out = {
            'out1': bait1,
            'out2': bait2,
            'out3': bait3,
            'out4': bait4
        }

        return jsonify(out), 200

api.add_resource(Home, '/')
api.add_resource(Predicc, '/predict')

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True)

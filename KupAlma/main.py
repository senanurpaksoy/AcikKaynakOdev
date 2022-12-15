from flask import Flask, request
from flask_restful import Api, Resource
import math

app = Flask(__name__)
api = Api(app)

class Kup(Resource):
    def get(self,sayi):
        return {'Kupu': sayi*sayi*sayi},200

api.add_resource(Kup, '/kup/<int:sayi>')
app.run(host="0.0.0.0", port=5000)
app.run()
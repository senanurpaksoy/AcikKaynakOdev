from flask import Flask, request
from flask_restful import Api, Resource
import math

app = Flask(__name__)
api = Api(app)

class Kup(Resource):
    def get(self,sayi):
        return {'Kupu': sayi*sayi*sayi},200

class ArmstrongSayi(Resource):
    def get(self,sayi):
        uzunluk = len(sayi)
        toplam = 0
        
        for i in range(uzunluk):
            toplam = toplam + int(sayi[i]) ** uzunluk
        
        if (toplam == int(sayi)):
            return {'Girdiginiz sayi bir amstrong sayisidir'},200
        else:
            return {'Girdiğiniz sayi bir amstrong sayisi değildir'},200
        

api.add_resource(ArmstrongSayi, '/armstrong/<int:sayi>'}        
api.add_resource(Kup, '/kup/<int:sayi>')
app.run(host="0.0.0.0", port=5000)
app.run()

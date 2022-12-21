from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Kup(Resource):
    def get(self, sayi):
        return {'Kupu': sayi * sayi * sayi}, 200


class ArmstrongSayi(Resource):
    def get(self, sayi):

        basamak = str(sayi)
        toplam = 0

        for i in basamak:
            rakam = int(i)**len(basamak)
            toplam += rakam

        if (toplam == sayi):
            x= 'Girdiginiz sayi bir amstrong sayisidir' #return {'Girdiginiz sayi bir amstrong sayisidir'}, 200
        else:
            x= 'Girdiğiniz sayi bir amstrong sayisi değildir' #return {'Girdiğiniz sayi bir amstrong sayisi değildir'}, 200
        return {'Aciklama' : x},200

class Asal(Resource):
    def get(self, sayi):
        if (sayi < 2):
            x = 'Girilen sayi asal degildir'
        elif (sayi == 2):
            x = 'Girilen sayi asaldir'
        else:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    x = 'Girilen sayi asaldir'
                    break
                else:
                    x = 'Girilen sayi asal degildir'
        return {'Sayi': x},200


api.add_resource(Asal, '/asal/<int:sayi>')
api.add_resource(ArmstrongSayi, "/armstrong/<int:sayi>")
api.add_resource(Kup, '/kup/<int:sayi>')
app.run(host="0.0.0.0", port=5000)
app.run()

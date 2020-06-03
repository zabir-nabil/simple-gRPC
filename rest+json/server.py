from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
import numpy as np
import base64


# compression
import zlib


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('imgb64', location='json', help = 'type error')
parser.add_argument('w', type = int, location='json', help = 'type error')
parser.add_argument('h', type = int, location='json', help = 'type error')


class Predict(Resource):
    def post(self):
        request.get_json(force=True)
        data = parser.parse_args()

        if data['imgb64'] == "":
            return {
                    'data':'',
                    'message':'No file found',
                    'status':'error'
                    }

        img = data['imgb64']
        w = data['w']
        h = data['h']

        data2 = img.encode()
        data2 = base64.b64decode(data2)

        #data2 = zlib.decompress(data2)

        fdata = np.frombuffer(data2, dtype=np.uint8).reshape(w, h, -1)

        if img:

            return json.dumps({
                    'mean': np.mean(fdata),
                    'channel': fdata.shape[-1], 
                    'message':'darknet processed',
                    'status':'success'
                    })
        return {
                'data':'',
                'message':'Something when wrong',
                'status':'error'
                }


api.add_resource(Predict,'/predict')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000, threaded=True)
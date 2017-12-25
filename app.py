from flask import Flask, json
from flask_restful import reqparse, abort, Api, Resource
from publicneeds import PublicNeeds

app = Flask(__name__)
api = Api(app)

class Region(Resource):
    def get(self, region):
        pubs = PublicNeeds()
        data = pubs.service_information(region=region)
        return data, 200


api.add_resource(Region, '/region/<region>')
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)

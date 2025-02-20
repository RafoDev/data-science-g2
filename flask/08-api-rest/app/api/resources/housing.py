from flask_restful import Resource, Api
from flask import request

from .. import api

api_housing = Api(api)

class HousingResource(Resource):
  def get(self):
    context = {
      "status": True,
      "message": "Listado de precios de casas"
    }
    return context
  
  def post(self):
    data = request.get_json()
    rooms = data["rooms"]
    return {"test": rooms}

api_housing.add_resource(HousingResource,"/housing")
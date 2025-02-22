from flask_restful import Resource, Api
from flask import request

from .. import api
from ..models import Housing
from ..schemas import HousingSchema

api_housing = Api(api)

class HousingResource(Resource):
  def get(self):
    data = Housing.get_all()
    data_schema = HousingSchema(many=True)

    context = {
      "status": True,
      "message": "Listado de precios de casas",
      "content": data_schema.dump(data)
    }
    
    return context
  
  def post(self):
    data = request.get_json()
    rooms = int(data["rooms"])

    housing = Housing(rooms)
    housing.save()

    data_schema = HousingSchema()

    context = {
      "status": True,
      "message": "Registro creado",
      "content": data_schema.dump(housing)
    }
    return context
  

api_housing.add_resource(HousingResource,"/housing")
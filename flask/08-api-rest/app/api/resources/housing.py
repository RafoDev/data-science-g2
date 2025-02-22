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
  
class HousingResourceDetail(Resource):
  def get(self, id):
    data = Housing.get_by_id(id)
    data_schema = HousingSchema()

    context = {
      "status": True,
      "message": "Registro encontrado",
      "content": data_schema.dump(data)
    }
    return context

  def put(self, id):
    data = request.get_json()
    rooms = int(data["rooms"])

    housing = Housing.get_by_id(id)
    housing.rooms = rooms
    housing.save()

    data_schema = HousingSchema()

    context = {
      "status": True,
      "message": "Registro actualizado",
      "content": data_schema.dump(housing)
    }
    return context
  
  def delete(self, id):
    housing = Housing.get_by_id(id)
    housing.delete()

    data_schema = HousingSchema()

    context = {
      "status": True,
      "message": "Registro eliminado",
      "content": data_schema.dump(housing)
    }
    return context

api_housing.add_resource(HousingResource,"/housing")
api_housing.add_resource(HousingResourceDetail,"/housing/<id>")
from extensions import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Housing

class HousingSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Housing
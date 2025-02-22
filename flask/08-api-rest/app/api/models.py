from ..extensions import db
from ml_model import HousingModel

class Housing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rooms = db.Column(db.Integer, nullable=False)
  price = db.Column(db.Double, nullable=True)

  def __init__(self,rooms):
    self.rooms = rooms
  
  @staticmethod
  def get_all():
    return Housing.query.all()
  
  @staticmethod
  def get_by_id(id):
    return Housing.query.get(id)
  
  def save(self):
    ml_housing = HousingModel
    self.price = ml_housing.predict(self.rooms)
    if not self.id:
      db.session.add(self)
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
from extensions import db

class Housing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rooms = db.Column(db.Integer, nullable=False)
  price = db.Column(db.Double, nullable=True)

  def __init__(self,rooms):
    self.rooms = rooms
  
  @staticmethod
  def get_all():
    return Housing.query.all()
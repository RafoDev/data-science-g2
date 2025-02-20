from flask import Blueprint, jsonify

api = Blueprint("api", __name__,url_prefix="/api")

from .resources import housing

@api.route("/")
def index():
  context = {
    "message": "api v1.0"
  }
  return jsonify(context)
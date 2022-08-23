from flask import Blueprint, jsonify

init_api = Blueprint('init_api', __name__)


@init_api.route('/', methods=['GET'])
def index():
    return jsonify('flask run sucess!')

from flask import Blueprint, jsonify, abort, request
from itsdangerous import json
import sqlalchemy
from sqlalchemy.sql.expression import false
from ..models import Player, db

bp = Blueprint('players', __name__, url_prefix='/players')

# Get a list of all players


@bp.route('', methods=['GET'])
def index():
    players = Player.query.all()
    result = []
    for p in players:
        result.append(p.serialize())
    return jsonify(result)

# Get players by ID


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Player.query.get_or_404(id)
    return jsonify(p.serialize())

# Create new player name


@bp.route('', methods=['POST'])
def create():
    if 'player_name' not in request:
        return abort(400)
    p = Player(
        player_name=request.json['player_name']
    )

    db.session.add(p)
    db.session.commit()
    return jsonify(p.serialize())

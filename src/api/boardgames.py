from flask import Blueprint, jasonify, abort, jsonify, request
from itsdangerous import json
from ..models import Boardgame, db

bp = Blueprint('boardgames', __name__, url_prefix='/boardgames')


# Get all boardgames
@bp.route('', methods=['GET'])
def index():
    boardgames = Boardgame.query.all()
    result = []
    for b in boardgames:
        result.append(b.serialize())
    return jsonify(result)

# Get boardgames by ID


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    b = Boardgame(b.serialize())

# Post a new boardgame title


@bp.route('', methods=['POST'])
def create():
    if 'game_title' not in request.json:
        return abort(400)

    b = Boardgame(
        game_title=request.json['game_title']
    )

    db.session.add(b)
    db.session.commit()
    return jsonify(b.serialize())

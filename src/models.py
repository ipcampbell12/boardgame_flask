from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# reference this file
app = Flask(__name__)

# initialize database
db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(200), nullable=False)

    def __init__(self, player_name):
        self.player_name = player_name

    def serialize(self):
        return {
            'id': self.id,
            'player_name': self.player_name
        }


class Boardgame(db.Model):
    __tablename__ = 'boardgames'
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(200), nullable=False)

    def __init__(self, game_title):
        self.game_title = game_title

    def serialize(self):
        return {
            'id': self.id,
            'game_title': self.player_name
        }


games_table = db.Table(
    'games',
    db.Column(
        'player_id', db.Integer,
        db.ForeignKey('players.id'),
        primary_key=True
    ),

    db.Column(
        'boardgame_id', db.Integer,
        db.ForeignKey('boardgames_id'),
        primary_key=True
    ),

    db.Column(
        'created_at', db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

)

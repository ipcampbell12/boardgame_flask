from app import db
from datetime import datetime



match_player = db.Table(
    'match_player',
    db.Column('match_id',db.Integer,db.ForeignKey('matches.id')),
    db.Column('player_id',db.Integer, db.ForeignKey('players.id'))
) 

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer,nullable = False, primary_key=True)
    fname = db.Column(db.String(80),nullable=False)
    lname = db.Column(db.String(80),nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    status = db.Column(db.String(10),nullable=False)
    age = db.Column(db.String(10),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    
    #matches = db.relationship('Match', secondary=match_player, backref='players')
    

    def __repr__(self):
        return '<Player %r' % self.id



class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer,nullable = False, primary_key=True)
    game = db.Column(db.String(30),nullable =False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    winner = db.Column(db.Integer, db.ForeignKey('players.id'))
    players = db.relationship('Player',secondary=match_player,backref=db.backref('matches',cascade="all, delete-orphan",single_parent=True))

    def __repr__(self):
        return '<Match %r' % self.id



class Game(db.Model):
    __tablename__ = 'boardgames'

    id = db.Column(db.Integer,nullable = False, primary_key=True)
    game = db.Column(db.String(80),nullable=False)
    game_type = db.Column(db.String(20))
    max_plyares = db.Column(db.Integer)

    







from flask import Blueprint,render_template,redirect,request,flash
from flask_smorest import abort
import sqlite3
from models import Game,Player,Match
from query import *
from app import db

views = Blueprint('views',__name__)


#go to various pages 
@views.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@views.route('/player',methods=['POST','GET']) 
def player():
    #print("I made it this far")
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        gender = request.form.get('gender')
        status = request.form.get('status')
        age = request.form.get('age')
    
        new_player = Player(fname = fname,lname=lname,gender=gender,status=status,age=age)
        #print(f"I added {new_player}")
        try:    
            db.session.add(new_player)
            db.session.commit()
            flash(f"Player {fname+' '+lname} has been created",category = 'player')
            return redirect('/player')
        except: 
            abort(404,message="There was an issue adding the player")
    else: 
        players = Player.query.order_by(Player.created).all()
        return render_template('player.html',players=players)

@views.route('/match',methods=['POST','GET']) 
def session():
    if request.method == 'GET':
        players = Player.query.order_by(Player.created).all()
        return render_template('match.html',players=players)
    if request.method == 'POST':
        
        print("I got the players")

        game = request.form.get('game')
        winner = request.form.get('winner')


        player1 = request.form.get('player1')
        player2= request.form.get('player2')
        player3 = request.form.get('player3')
        player4 = request.form.get('player4')

        player_group= db.session.query(Player).filter(Player.id.in_([player1,player2,player3,player4]))

        players = [player for player in player_group]

        new_session = Match(game=game,winner=winner,players=players)

        try: 
            db.session.add(new_session)
            db.session.commit()
            print("I add the everythign to the db")
            flash(f"A new session of {game} has been added",category = 'match')
            return redirect('/match')
        except: 
            return render_template('match.html')

    return render_template('match.html')

@views.route('/stats',methods=['GET','POST'])
def stats():
    if request.method == 'GET':
    
        #queries
        played = num_played()
        total = get_total()
        player_total = get_num_players()
        most = most_played()
        wins = most_won()
        
    
        return render_template('stats.html',played=played,total=total, player_total=player_total,most=most,wins=wins)


@views.route('/gamelog',methods=['GET','POST'])
def gamelog():
    if request.method == 'GET':
        winlog = win_log()
        return render_template('gamelog.html',winlog=winlog)




@views.route('/delete/<int:id>')
def delete_player(id):
    player_to_delete = Player.query.get_or_404(id)
    try:
        db.session.delete(player_to_delete)
        db.session.commit()
        flash(f"The player {player_to_delete.fname} has been removed", "removal")
        return redirect('/player')
    except:
        abort(404,message= "We couldn't delete that player")


@views.route('/delete_all')
def delete_all():
    try:
        db.session.query(Player).delete()
        db.session.commit()
        flash("All the players have been deleted","removal2")
        return redirect('gmail.com')
    except:
        abort(404,message= "We couldn't delete all the players")


    
@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    player = Player.query.get_or_404(id) 
    print(f"Retrieved player with id {id}")


    if request.method == 'POST':
        player.fname = request.form.get('fname')
        player.lname = request.form.get('lname')
        player.gender = request.form.get('gender')
        player.status = request.form.get('status')
        player.age = request.form.get('age')
        print(f"Updated player with id {id}")
    
        try:
            db.session.commit()
            flash(f"The player {player.fname+' '+player.lname} has been updated","updated")
            print(f"Saved player with id {id}")
            return redirect('/player')
        except:
            abort(404,message= "There was an issue updating that player")

    else:
        return render_template('update.html',player=player)



# #need to figure this one out
@views.route('/update_match/<int:id>',methods=['GET', 'POST']) 
def update_match(id):
    match = Match.query.filter_by(id).first()

    # It doesn't get this far. I don't think this function is even running.
    print(f"Retrieved match with {match} id.")
    
    if request.method == 'POST':
        

        match.game = request.form.get('game')
        match.winner = request.form.get('winner')


        match.player1 = request.form.get('player1')
        match.player2= request.form.get('player2')
        match.player3 = request.form.get('player3')
        match.player4 = request.form.get('player4')

        player_group= db.session.query(Player).filter(Player.id.in_([match.player1,match.player2,match.player3,match.player4]))

        players = [player for player in player_group]

        try: 
            db.session.commit()
            return redirect('/gamelog')
        except: 
            abort(404,message= "There was an issue updating this match")


    return render_template('update_match.html',players=players)



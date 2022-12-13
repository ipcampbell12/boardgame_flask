import sqlite3

def get_total():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()

    query = '''
    SELECT COUNT(*) FROM matches
    '''

    cursor.execute(query)
    total = cursor.fetchall()
    num = total
    print(num)

    if num: 
        return num[0]
    else:
        return []


def get_num_players():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()

    query = '''
    SELECT COUNT(*) FROM players
    '''

    cursor.execute(query)
    total = cursor.fetchall()
    num = total
    print(num)

    if num: 
        return num[0]
    else:
        return []


def most_played():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()

    query = '''
    SELECT game FROM(SELECT game, COUNT(*) AS count FROM matches
    GROUP BY game
    ORDER BY count DESC LIMIT 1) AS top;
    '''

    cursor.execute(query)
    total = cursor.fetchall()
    num = total
    print(num)

    if num:
        return num[0]
    else:
        return []

        
def num_played():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()
    
    #LOAD QUERY RESULTS
    query = '''
    SELECT p.fname || ' ' || p.lname AS name, COUNT(m.winner) AS games_played FROM players p
    JOIN match_player mp
    ON p.id = mp.player_id
    JOIN matches m 
    ON mp.match_id = m.id
    GROUP BY name
    ORDER BY games_played DESC;
    '''

    cursor.execute(query)
    result = cursor.fetchall()
    
    items = []
    for row in result:
        items.append({'name':row[0],'games_played':row[1]})

    print(items)

    if items:
        return items
    else:
        return []

def most_won():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()
    
    #LOAD QUERY RESULTS
    query = '''
    SELECT p.fname || ' ' || p.lname AS name, COUNT(m.winner) AS games_won FROM players p 
        JOIN match_player mp
        ON p.id = mp.player_id 
        JOIN matches m
        ON mp.match_id = m.id
        WHERE p.id = m.winner
        GROUP BY p.fname
        ORDER BY games_won DESC;
    '''

    cursor.execute(query)
    result = cursor.fetchall()
    
    items = []
    for row in result:
        items.append({'name':row[0],'games_won':row[1]})

    print(items)

    if items:
        return items
    else:
        return []


def win_log():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()
    
    #LOAD QUERY RESULTS
    query = '''
    SELECT strftime('%m/%d/%Y', m.date) AS Date, m.game, (pl.fname || ' ' || pl.lname) AS Winner, 
    GROUP_CONCAT(p.fname || ' ' || p.lname) AS players
    FROM matches m
    JOIN match_player mp
    ON m.id = mp.match_id
    JOIN players p 
    ON mp.player_id = p.id 
    JOIN players pl 
    ON m.winner = pl.id
    GROUP BY Date,m.game, Winner 
    ORDER BY Date DESC;
    '''

    cursor.execute(query)
    result = cursor.fetchall()
    
    items = []
    for row in result:
        items.append({'date':row[0],'game':row[1],'winner':row[2],'players':row[3]})

    print(items)

    if items:
        return items
    else:
        return []


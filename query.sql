CREATE TABLE players (
	id SERIAL,
	fname VARCHAR(100),
	lname VARCHAR(100),
	gender CHAR(15),
	wins INTEGER,
	PRIMARY KEY(id) 
);


CREATE TABLE games (
	id SERIAL,
	name VARCHAR(255),
	type CHAR(50),
	max_players INTEGER,
	PRIMARY KEY(id)
);


CREATE TABLE matches (
	id SERIAL,
	game_id INTEGER,
	winner INTEGER,
	game_date DATE DEFAULT CURRENT_DATE,
	number_of_players INTEGER,
	PRIMARY KEY(id),
	FOREIGN KEY(winner_id) REFERENCES players(id),
	FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE match_player(
	match_id INTEGER,
	player_id INTEGER,
	FOREIGN KEY(match_id) REFERENCES matches(id),
	FOREIGN KEY(player_id) REFERENCES players(id)
);


INSERT INTO players (fname,lname,gender,wins)VALUES 
   ('Harry','Potter','Male',0),
   ('Hermione','Granger','Female',0),
   ('Ronald','Weasley','Male',0),
   ('Luna','Lovegood','Female',0),
   ('Neville','Longbottom','Male',0);


INSERT INTO games (name, type, max_players) VALUES 
	('Connect Four','Other',2),
	('Checkers','Board game',2),
	('Monopoly Deal','Card game',4),
	('Nerts','Card Game',4),
	('Settlers of Catan','Board Game',4),
	('Spot It','Card game',4),
	('Scrabble','Board Game',4);


INSERT INTO sessions (game_id,winner_id,number_of_players) VALUES
		 (1,1,2),
		 (5,1,3),
		 (5,3,2),
		 (6,2,4),
		 (4,2,4);

INSERT INTO players_sessions (player_id,session_id) VALUES
		(1,1),
		(3,1),
		(1,2),
		(4,2),
		(5,2),
		(3,3),
		(1,3),
		(2,4),
		(3,4),
		(1,4),
		(5,4),
		(2,5),
		(4,5),
		(1,5),
		(5,5);


/* Output every game, with eveyr player, every game name and every winner */
SELECT p.fname AS name,s.id AS session, g.name, pl.fname AS winner
FROM players p
JOIN players_sessions ps 
ON p.id = ps.player_id
JOIN sessions s
ON ps.session_id = s.id
JOIN players pl
ON s.winner_id = pl.id
JOIN games g
ON s.game_id = g.id;

/*Find the count of games each player has won */
SELECT p.fname, COUNT(s.winner_id) FROM players p 
JOIN players_sessions ps
ON p.id = ps.player_id 
JOIN sessions s
ON ps.session_id = s.id
WHERE p.id = s.winner_id
GROUP BY p.fname;
/* Doesn't show players who have zero wins */



SELECT * FROM games;
SELECT * FROM players;
SELECT * FROM sessions;
SELECT * FROM players_sessions;

DROP TABLE sessions CASCADE;
DROP TABLE players_sessions CASCADE;


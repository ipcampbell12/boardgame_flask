from flask import Flask
#from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

#initialize the flask app
app = Flask(__name__)
app.secret_key="Ian"

#define databse location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boardgames.db'
#engine = create_engine('sqlite:///boardgames.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

#register views at the url
from views import views
app.register_blueprint(views,url_prefix='/')

#only run files on run, not on import
if __name__ == 'main':
    db.init_app(app)
    app.run(debug=True)



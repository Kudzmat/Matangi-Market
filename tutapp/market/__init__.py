"""every python package is going to include a special python file called "__init__"
The init file will be the first to be run so we can import everything from a different file
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)  # flask app
"""
use app object & add extra configuration so flask app 
can recognize its database. We do this by adding key values which are considered conventions so
the flask app can understand where database is located.
We create a key called "SQLALCHEMY_DATABASE_URI." Uniform Resource Identifier (uri) is not like url which is a link to a website,
it is an identifier - a file that will be identified as a database. "sqlite:///market.db" allows us to find that database,
"market.db" is the name of the file.
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '169d3c991557feaa996ccbbf'
db = SQLAlchemy(app)  # database
bcrypt = Bcrypt(app)  # for storing the passwords as # instead of plain text
#login_manager = LoginManager(app)

from market import routes
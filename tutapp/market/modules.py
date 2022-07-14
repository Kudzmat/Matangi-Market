from market import db
from market import bcrypt


# creating models for databases
# nullable refers to whether a field can remain empty

# registering new users
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)  # password needs to be encrypted for security
    # purposes
    budget = db.Column(db.Integer(), nullable=False, default=1000)  # each user will have a budget / wallet system for
    # spending on the website, they get 1000 for being a new user
    items = db.relationship('Item', backref='owned_user',
                            lazy=True)  # this will show which items the user currently has ownership over

    # additional attribute which will be available at each instance
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_passowrd):
        self.password_hash = bcrypt.generate_password_hash(plain_text_passowrd).decode('utf-8')

    # magic method to display string
    def __repr__(self):
        return f'User - {self.username}'


# creating new items on the store
class Item(db.Model):
    # creating fields
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))  # foreign key will be related to another models

    # primary key

    # magic method to display string
    def __repr__(self):
        return f'Item - {self.name}'

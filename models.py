from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

class Good(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float(), nullable=False)
    max_quantity = db.Column(db.Integer(), nullable=False)

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.max_quantity = quantity

    @property
    def json(self):
        dictionary = self.__dict__
        dictionary.pop('_sa_instance_state')
        return dictionary

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(20), unique=True)
    mail = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(50))
    cart_id = db.Column(db.Integer())
    is_admin = db.Column(db.Boolean())


    def __init__(self,username, email, password ):
        self.login = username
        self.mail = email
        self.password = password



class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer(), primary_key=True)
    good_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer())

    def __init__(self,good_id,user_id,quantity):
        self.good_id = good_id
        self.user_id = user_id
        self.quantity = quantity
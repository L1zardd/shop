from flask import Flask, request, jsonify
from flask_login import current_user
from flask_cors import CORS, cross_origin
from models import db, Good, User, Cart

app = Flask(__name__)

app.config['SECRET_KEY'] = "this_badass_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

cors = CORS(app)


with app.app_context():
    db.drop_all()
    db.create_all()
    good1=Good("Губозакаточная машинка",20000,10)
    good2 = Good("Карточки с видом на закат губы", 200, 3)
    good3 = Good("Игральные контурные карты", 500, 40)
    good1.description = "Особо мощная машина, закатывает даже широко раскатанные губы"

    user_testa = User("UserTA", "userTA@mail.ru", "UserTA123")
    user_testa.is_admin = True

    db.session.add(user_testa)
    db.session.add(good1)
    db.session.add(good2)
    db.session.add(good3)
    db.session.commit()



@app.route("/api/good", methods=["post",'get'])
def good_page():
    if request.method == "GET":
        goods = Good.query.all()
        listgoods=[]
        for good in goods:
            listgoods.append(good.json)
        return jsonify(listgoods)
    if request.method == "POST":
        if current_user.is_admin == 1:


@app.route("/api/good/<g_id>", methods = ["get","put","delete"])
def good_instance_page(g_id):
    if request.method == "GET":
        good = Good.query.filter_by(id=g_id).first()
        return good.json
    if request.method == "PUT":
        pass
    if request.method == "DELETE":
        good = Good.query.filter_by(id=p_id).first_or_404()
        session.delete(good)
        session.commit()

@app.route("/api/user", methods=["post",'get'])
def user_page():
    if request.method=="GET":
        pass

app.run(debug=True)

from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
import mongoengine as me

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host':'mongodb://localhost:27017/shop'}
db = MongoEngine(app)


class Parameters(me.EmbeddedDocument):
    manufacturer = me.StringField()
    country = me.StringField()
    color = me.StringField()
    screen = me.DecimalField()
    storage = me.IntField()
    mpix = me.IntField()
    battery_life = me.StringField()


class Products(me.Document):
    name = me.StringField()
    description = me.StringField()
    parameters = me.EmbeddedDocumentField(Parameters)


@app.route('/add/', methods=['GET', 'POST'])
def add_product():
    body = request.get_json()
    product = Products(**body).save()
    return jsonify(product)


@app.route('/search_name/', methods=['GET', 'POST'])
def search_name():
    products = Products.objects.order_by('name')
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        search_filter = request.get_json()
        products = Products.objects(name=search_filter['name']).only('name')
    return jsonify(products)


@app.route('/search_parametr/', methods=['GET', 'POST'])
def search_parametr():
    products = Products.objects.only('name').order_by('name')
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
    	search_filter = request.get_json()
    	products = Products.objects(parameters__match=search_filter['parameters']).only('name')
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)

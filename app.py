"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/api/cupcakes')
def list_all_cupcakes():
    """return all cupcakes in jason format"""
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def list_cupcake(id):
    """return info on one cupcake"""
    cake = Cupcake.query.get_or_404(id)
    return jsonify(cake=cake.to_dict())
    
@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    
    data = request.json

    new_cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None
    )
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.to_dict())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cake(id):

    data=request.json

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = data["flavor"]
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()
    
    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")


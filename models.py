from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


"""Models for Cupcake app."""
class Cupcake(db.Model):
    __tablename__="cakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating= db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default='https://tinyurl.com/demo-cupcake')

def connect_db(app):
    db.app = app
    db.init_app(app)
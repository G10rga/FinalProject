from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import  DataRequired, Length, NumberRange
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView



from extensions import db, login_manager
from flask_login import UserMixin , current_user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(60), default = 'Guest')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Item('{self.category}', '{self.name}', '{self.price}', '{self.img}')"






@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    db.create_all()

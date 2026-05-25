from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Float, nullable=False)

    quantity = db.Column(db.Integer, nullable=False)

    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }

from ..app import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "pizza_id": self.pizza_id,
            "restaurant_id": self.restaurant_id,
            "pizza": self.pizza.to_dict() if self.pizza else None,
            "restaurant": self.restaurant.to_dict() if self.restaurant else None
        }

    def validate(self):
        errors = []
        if not (1 <= self.price <= 30):
            errors.append("Price must be between 1 and 30")
        return errors

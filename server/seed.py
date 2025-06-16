from .app import app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

# Seed data
def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()
        restaurants = [
            Restaurant(name="Mario's Pizza", address="123 Main St"),
            Restaurant(name="Luigi's Pizza", address="456 Side St"),
            Restaurant(name="Kiki's Pizza", address="789 Broadway")
        ]
        pizzas = [
            Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Peppers, Onions, Olives")
        ]
        db.session.add_all(restaurants)
        db.session.add_all(pizzas)
        db.session.commit()
        restaurant_pizzas = [
            RestaurantPizza(price=5, restaurant_id=restaurants[0].id, pizza_id=pizzas[0].id),
            RestaurantPizza(price=7, restaurant_id=restaurants[0].id, pizza_id=pizzas[1].id),
            RestaurantPizza(price=6, restaurant_id=restaurants[1].id, pizza_id=pizzas[2].id),
            RestaurantPizza(price=8, restaurant_id=restaurants[2].id, pizza_id=pizzas[0].id),
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        print("Database seeded!")

if __name__ == "__main__":
    seed()

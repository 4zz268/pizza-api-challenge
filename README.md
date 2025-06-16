# Pizza Restaurant API Challenge

## Setup Instructions

1. **Clone the repository**
2. **Create a virtual environment and install dependencies:**

```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

3. **Set up the database:**

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

4. **Seed the database:**

```bash
python server/seed.py
```

## Project Structure

```
server/
  app.py
  config.py
  models/
    __init__.py
    restaurant.py
    pizza.py
    restaurant_pizza.py
  controllers/
    __init__.py
    restaurant_controller.py
    pizza_controller.py
    restaurant_pizza_controller.py
  seed.py
migrations/
README.md
```

## Routes

### Restaurants
- `GET /restaurants` — List all restaurants
- `GET /restaurants/<id>` — Get a restaurant and its pizzas
- `DELETE /restaurants/<id>` — Delete a restaurant (cascades to RestaurantPizzas)

### Pizzas
- `GET /pizzas` — List all pizzas

### RestaurantPizzas
- `POST /restaurant_pizzas` — Create a new RestaurantPizza

#### Example POST
```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

#### Success Response
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" },
  "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "789 Broadway" }
}
```

#### Error Response
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## Validation Rules
- `RestaurantPizza.price` must be between 1 and 30 (inclusive)

## Postman Testing
- Import `challenge-1-pizzas.postman_collection.json` into Postman
- Test all endpoints

---

**Enjoy your pizza API!**

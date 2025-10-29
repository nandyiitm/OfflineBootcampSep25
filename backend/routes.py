from flask_restful import Api, Resource
from flask import request

from models import db, Pizza

api = Api()

# This is what we NEED to do in mad2 (i.e, returning data instead of HTML)
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    
api.add_resource(HelloWorld, '/')

class PizzaAPI(Resource):
    def get(self, pizza_id=None):
        if pizza_id:
            pizza = Pizza.query.get(pizza_id)
            if not pizza:
                return {'message': 'Pizza not found!'}, 404
            return {'id': pizza.id, 'name': pizza.name, 'toppings': pizza.toppings}, 200
        pizzas = Pizza.query.all()
        pizzas = [{'id': p.id, 'name': p.name, 'toppings': p.toppings} for p in pizzas]
        return {'message': 'Pizzas fetched successfully!', "pizzas": pizzas}, 200
    
    def post(self):
        data = request.get_json()

        if not data or 'name' not in data and not data['name']:
            return {'message': 'Name is required!'}, 400
        
        pizza = Pizza(name=data['name'], toppings=data.get('toppings', False))
        db.session.add(pizza); db.session.commit()
        
        return {'message': 'Pizza created!'}, 201
    
    def put(self, pizza_id=None):
        if pizza_id is None:
            return {'message': 'Pizza ID is required for update!'}, 400
        
        # check pizza exists or not
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return {'message': 'Pizza not found!'}, 404
        
        # get data and validate
        data = request.get_json()
        if not data:
            return {'message': 'Date is required!'}, 400
        
        pizza.name = data.get('name', pizza.name)
        pizza.toppings = data.get('toppings', pizza.toppings)
        db.session.commit()
        
        return {'message': 'Pizza updated!'}, 200
    
    def delete(self, pizza_id=None):
        if pizza_id is None:
            return {'message': 'Pizza ID is required for deletion!'}, 400
        
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return {'message': 'Pizza not found!'}, 404
        
        db.session.delete(pizza); db.session.commit()

        return {'message': 'Pizza deleted!'}, 200
    
api.add_resource(PizzaAPI, '/pizza', '/pizza/<int:pizza_id>')

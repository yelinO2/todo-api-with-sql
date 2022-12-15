from models.todo_model import TodoModel
from flask import jsonify, request
from flask_restful import Resource

class Todo(Resource):
    def post(self):
        name = request.json['name']
        is_excecuted = request.json['is_executed']

        new_todo_item = TodoModel(name, is_excecuted)
        new_todo_item.save_to_db()
        
        return new_todo_item.json(), 201

    def get(self):
        todo_items = TodoModel.query.all()
        return {"todo_items" : [todo_item.json() for todo_item in todo_items]},201
        
class Delete_Todo(Resource):
    def delete(self, id):
        item = TodoModel.find_by_id(id)
        if item:
            item.delete_from_db()
        return {"Message" : "Item deleted successfully"}
        
        
            
             
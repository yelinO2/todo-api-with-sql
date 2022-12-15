from flask import Flask
from flask_restful import Api
from db import db
from resources.todo import Todo, Delete_Todo


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
app.secret_key = "todoapi"


api.add_resource(Todo, '/todo')
api.add_resource(Delete_Todo, '/todo/<int:id>')


@app.before_first_request
def create_table():
    db.create_all()

if __name__ == "__main__":
    from db import db
    db.init_app(app)

    app.run(debug=True)

from db import db

class TodoModel(db.Model):
    __tablename__ = 'db'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    is_executed = db.Column(db.Boolean)

    def __init__(self, name, is_executed):
        self.name = name
        self.is_executed = is_executed

    def json(self):
        return {'id' : self.id, 'name' : self.name, 'is_executed' : self.is_executed}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
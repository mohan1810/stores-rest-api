from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel',lazy='dynamic')

    def __init__(self,name):
        self.name = name

    def json(self):
        return {"name":self.name, "items":[item.json() for item in self.items.all()]}#self.items now is a query builder

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()# first return only one row
        # this above functions return an ItemModel object with name and price
        # In place of cls u can also use ItemModel

    def save_to_db (self):
        db.session.add(self) #this saves  the ItemModel object we dont have to separately give the value of name and price
        db.session.commit()  #we can directly pass the ItemModel object

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

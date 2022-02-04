from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2 ))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name":self.name, "price":self.price}

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

from app import db


class Survivors(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   gender = db.Column(db.String(50))
   flags = db.Column(db.String(128))
   lat = db.Column(db.Float)
   lon = db.Column(db.Float)
   infected = db.Column(db.Boolean)

   def to_json(self):
      return {"name": self.name,
                "id": self.id,
                "gender":self.gender,
                "flags":self.flags,
                "infected":self.infected,
                "lat":self.lat,
                "lon":self.lon}

class Inventory(db.Model):
   #survivor = db.Column(db.String(100), db.ForeignKey("Survivors.id"), primary_key = True)
   survivor = db.Column(db.String(100), primary_key = True)
   name = db.Column(db.String(100), primary_key = True)

db.drop_all()
db.create_all()
db.session.commit()

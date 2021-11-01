from app import db

class Survivors(db.Model):
   __tablename__ = "survivors"
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   gender = db.Column(db.String(50))
   lat = db.Column(db.Float)
   lon = db.Column(db.Float)
   infected = db.Column(db.Boolean)

   def to_json(self):
      return {"name": self.name,
                "id": self.id,
                "gender":self.gender,
                "infected":self.infected,
                "lat":self.lat,
                "lon":self.lon}

class Inventory(db.Model):
   __tablename__ = "inventory"
   survivor = db.Column(db.String(100), db.ForeignKey("survivors.id"), primary_key = True)
   name = db.Column(db.String(100), primary_key = True)


class Infected(db.Model):
   __tablename__ = "infected"
   survivor = db.Column(db.String(100), db.ForeignKey("survivors.id"), primary_key = True)
   reporter = db.Column(db.String(100), db.ForeignKey("survivors.id"), primary_key = True)


db.drop_all()
db.create_all()
db.session.commit()

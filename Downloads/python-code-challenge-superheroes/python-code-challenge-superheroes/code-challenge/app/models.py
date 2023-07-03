from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    super_name= db.Column(db.String)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    hero_powers = db.relationship("Hero_power", backref="hero")
    serialize_rules = ("-hero_powers.hero",)

    def __repr__(self):
        return f"Hero {self.name} has {self.super_name}."
    
class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    description= db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    hero_powers= db.relationship("Hero_power", backref="power")
    serialize_rules = ("-hero_powers.power",)

    def __repr__(self):
        return f"Power {self.name} was created at {self.created_at}."
    
    @validates("description")
    def validate_description(self, key , description):
        if description and len(description) < 20:
            raise ValueError("Description must be atleast 20 characters long.")
        return description
    
class Hero_power(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    serialize_rules = ("-hero.hero_powers", "-power.hero_powers",)

    def __repr__(self):
        return f"Hero_power with {self.strength} belongs to hero {self.hero_id}"
    
    @validates("strength")
    def validate_strength(self, key, strength):
        if strength and strength not in ["Strong", "Weak", "Average"]:
            raise ValueError("Invalid strength.")
        return strength




# add any models you may need. 
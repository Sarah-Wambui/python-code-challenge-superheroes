#!usr/bin/env python3
from random import randint, choice as rc
from faker import Faker
from models import db, Hero, Power, Hero_power
from app import app

fake = Faker()
strengths = ["Strong", "Weak", "Average"]

with app.app_context():
    Hero.query.delete()
    Power.query.delete()
    Hero_power.query.delete()

    heroes = []
    for i in range(50):
        hero = Hero(
          name= fake.name(),
          super_name = fake.first_name(),  
        )
        heroes.append(hero)
    db.session.add_all(heroes)

    powers = []
    for i in range(50):
        power = Power(
            name = fake.name(),
            description = fake.paragraph()
        )
        powers.append(power)
    db.session.add_all(powers)

    hero_powers = []
    for i in range(50):
        hero_power = Hero_power(
            strength=rc(strengths),
            hero_id= randint(1, 50),
            power_id = randint(1, 50)
        )
        hero_powers.append(hero_power)
    db.session.add_all(hero_powers)
    db.session.commit()
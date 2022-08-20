from turtle import position
from . import database
from sqlalchemy.sql import func

#User
class Guest_user(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    creation_date = database.Column(database.DateTime(timezone=True), default = func.now())
    ship = database.Column(database.String(768))

class User(database.Model):
    id = database.Column(database.Integer, primary_keys=True)
    email = database.Column(database.String(250), unique = True)
    hash_password = database.Column(database.String(260))
    position = database.Column(database.String(16))
    ship = database.relationship('Ships')

#Ships
class ShipOverview(database.Model):
    id = database.Column(database.Integer, primary_keys = True)
    owner = database.Column(database.Integer, database.ForeignKey('user.id'))
    name = database.Column(database.String(200))
    dimensions = database.Column(database.String(10))
    schematics_S = database.relationship('SmallShip')
    schematics_M = database.relationship('MediumShip')
    schematics_B = database.relationship('BigShip')


class SmallShip(database.Model):
    id = database.Column(database.Integer, database.ForeignKey('shipoverview.id'))
    plans = database.Column(database.String(768))

class MediumShip(database.Model):
    id = database.Column(database.Integer, database.ForeignKey('shipoverview.id'))
    plans = database.Column(database.String(3072))

class BigShip(database.Model):
    id = database.Column(database.Integer, database.ForeignKey('shipoverview.id'))
    plans = database.Column(database.String(12288))

#Map
class Map(database.Model):
    id = database.Column(database.String(6), primary_key = True)
    special = database.Column(database.Boolean)
    tile_id = database.Column(database.Integer)
    
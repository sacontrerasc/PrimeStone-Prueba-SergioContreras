import db
from sqlalchemy import Column, Integer, String, Float, Date
class Persona(db.Base):
    __tablename__ = 'persona'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fechaNacimiento = Column(Date)
    def __init__(self, nombre, fechaNacimiento):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
    def __repr__(self):
        return f'Producto({self.nombre}, {self.fechaNacimiento})'
    def __str__(self):
        return self.nombre
from datetime import datetime
from sqlalchemy import (
    Column, 
    Integer,
    String,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#Creacion de modelo de tabla para cargar datos extraidos de Discord
class DatosDiscord(Base):
    __tablename__ = 'datosDiscord'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(), default=datetime.now())
    autor = Column(String, nullable=False)
    title = Column(String, nullable=False)
    data = Column(String, nullable=False)


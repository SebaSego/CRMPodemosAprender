from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from db.models import DatosDiscord, Base

conn_string = 'sqlite:///test.sqlite3'
engine = create_engine(conn_string)
Base.metadata.create_all(engine) # here we create all tables
Session = sessionmaker(bind=engine)
session = Session()

# Now we are ready to use the model

#new_data = DatosDiscord(autor='test3', title='title3', data='datos de prueba3')
#session.add(new_data)
#session.commit()

def altaDatosDiscord(dautor, dtitle, ddata):
    
    new_data = DatosDiscord(autor=f'{dautor}', title=f'{dtitle}', data=f'{ddata}')
    session.add(new_data)
    session.commit()




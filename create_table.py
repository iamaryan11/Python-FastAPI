from database import engine,Base

# just : import model, sqlalchemy will automatically stored the data to metadata
import model


# the line means that : I am asking sqlalchemy to create all the tables that are mentioned in the model.py, Class is the table as per sqlalchemy
Base.metadata.create_all(bind=engine)


# run the file as: python create_table.py
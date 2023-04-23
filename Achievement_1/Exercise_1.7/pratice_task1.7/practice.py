from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://cf-python:password@localhost/my_database")

Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"


tea = Recipe(
    name="Tea",
    cooking_time=5,
    ingredients="Tea Leaves, Water, Sugar, Cardamom"
)

coffee = Recipe(
    name="Coffee",
    cooking_time=5,
    ingredients="Coffee Powder, Water"
)

cake = Recipe(
    name="Pork Tenderloins",
    cooking_time=45,
    ingredients="Pork Tenderloin, Spices"
)

banana_smoothie = Recipe(
    name="Spaghetti",
    cooking_time=25,
    ingredients="Noodles, Tomato Sauce, Meatballs, Parmesean Cheese"
)

buttered_toast = Recipe(
    name="Egg Sandwich",
    ingredients="Bread, Butter, Eggs, Cheese, Salt, Pepper",
    cooking_time=4
)

recipe_to_be_deleted = session.query(Recipe).filter(
    Recipe.name == 'Egg Sandwich').one()

session.delete(recipe_to_be_deleted)

recipes_list = session.query(Recipe).all()
session.commit()

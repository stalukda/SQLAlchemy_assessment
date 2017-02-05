"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

#flask_sqlalchemy.BaseQuery, meaning its a query.

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

#An association table binds two tables together although that table doesn't have any meaningful fields beyond 
#the ones glueing the other two tables. It manages many to many relationships. 




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').one()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter_by(name="Corvette", brand_id="che").all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter_by(founded = 1903, discontinued = None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950) ).all()

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = Model.query.options(db.joinedload('brand')).all()

    for car in models:
        if car.year == year:
            print car.name, car.brand.name, car.brand.headquarters

# get_model_info(1958)

def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    cars = Brand.query.options(db.joinedload('models')).all()

    for car in cars:
        print car.name,
        for car.model in car.models:
            print '\n', '\t', car.model.year, car.model.name

# get_brands_summary()

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_obj = Brand.query.filter(Brand.name.like('%{}%'.format(mystr))).all()

    return brand_obj

# search_brands_by_name("Ford")

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year <= end_year).all()

get_models_between(1960, 1980)

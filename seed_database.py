"""Script to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie.get('title')
    overview = movie.get('overview')
    poster_path = movie.get('poster_path')
    datetime_str = movie.get('release_date')
    format = "%Y-%m-%d"
    datetime = datetime.strptime(datetime_str, format)

    new_movie = crud.create_movie(title, overview, datetime, poster_path)

    movies_in_db.append(new_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    user = crud.create_user(email, password)

    for n in range(10):
        random_movie = choice(movies_in_db)
        rating = randint(1, 5)
        new_rating = crud.create_rating(user, random_movie, rating)
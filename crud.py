"""CRUD operations"""

from model import db, User, Rating, Movie, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date,
                    poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie


def show_all_movies():
    """Returns a list of all movies"""
    
    return db.session.query(Movie).all() 


def create_rating(user, movie, score):
    """create and return a new rating"""

    rating = Rating(user=user, movie=movie, score=score)
    
    # user_id = Rating.user.user_id

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movie_by_id(movie_id):
    """Returns a movie by id"""

    movie = Movie.query.filter(Movie.movie_id == movie_id).one()

    return movie


def show_all_users():
    """Returns a list of all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns a user by id."""

    user = User.query.filter(User.user_id == user_id).one()

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
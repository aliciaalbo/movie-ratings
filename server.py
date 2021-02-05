"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "GFRWYU83752ounfatgr25DCFgw8795trhegsfjdvn"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """Displays homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def show_movies():
    """View all the movies"""

    all_movies = crud.show_all_movies()

    return render_template('all_movies.html', movies=all_movies)

@app.route('/movies/<movie_id>')
def show_movie_info(movie_id):
    """Show movie info page"""
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html',
                            movie=movie)


@app.route('/users')
def show_all_users():
    """Shows all users."""

    all_users = crud.show_all_users()

    return render_template('all_users.html', users=all_users)


@app.route('/users/<user_id>')
def show_user_info(user_id):
    """Show user info page."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
 
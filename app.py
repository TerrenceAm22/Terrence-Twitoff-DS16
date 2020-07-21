#!/usr/bin/env python
"""Main app/routing file for TwitOff."""
from flask import Flask, render_template
from .models import DB, User
from .twitter import add_users
import tweepy

from flask import Flask, render_template
from .models import DB, User, add_test_users


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')
<<<<<<< HEAD
   
    
    
=======

>>>>>>> 3bd40e539524d24ad997b539f8dafb95ae5b113a
    @app.route('/add_test_users')
    def add_users():
        DB.drop_all()  # Reset the DB
        DB.create_all()
        add_test_users()
        return 'Users added!'

    @app.route('/view_test_users')
    def view_users():
        users = User.query.all()
<<<<<<< HEAD
        return '\n'.join([str(user) for users in users])
    return app
=======
        return '\n'.join([str(user) for user in users])
>>>>>>> 3bd40e539524d24ad997b539f8dafb95ae5b113a

    return app
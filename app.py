#!/usr/bin/env python
"""Main app/routing file for TwitOff."""
from flask import Flask, render_template
from .models import DB, User

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
    DB.init_app(app)
    app.run(debug=True)
    @app.route('/add_test_users')
    def add_users():
        DB.drop_all()
        DB.create_app()
        add_test_users()
        return 'Users Added!'
    
    @app.route('/view_test_users')
    def view_users():
        users = User.query.all()
        return '\n'.join([str(user) for users in users])
    @app.route('/')
    def root():
        return render_template('base.html')
    return app


import pytest
from app import app, db, Class, Origin, Type, RailwayLine, StationStop  # Adjust imports as per your file structure
from flask import jsonify
from unittest.mock import patch, MagicMock
import sqlite3

@pytest.fixture(scope='module')
def test_client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.test_client() as client:
        # Create the tables for testing
        with app.app_context():
            db.create_all()
        yield client
        # Clean up after tests
        with app.app_context():
            db.drop_all()






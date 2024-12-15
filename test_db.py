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

@pytest.fixture(scope='function')
def add_class(test_client):
    # Adding a class to test against
    class_data = {'class_code': 'C001', 'class_description': 'Test Class'}
    test_client.post('/classes', json=class_data)
    yield class_data
    # Clean up if needed (can delete specific records after test)

@pytest.fixture(scope='function')
def add_origin(test_client):
    # Adding an origin to test against
    origin_data = {'origin_code': 'O001', 'origin_description': 'Test Origin'}
    test_client.post('/origins', json=origin_data)
    yield origin_data
    # Clean up if needed

@pytest.fixture(scope='function')
def add_type(test_client):
    # Adding a type to test against
    type_data = {'type_code': 'T001', 'type_description': 'Test Type'}
    test_client.post('/types', json=type_data)
    yield type_data
    # Clean up if needed

@pytest.fixture(scope='function')
def add_station_stop(test_client):
    # Adding a station stop to test against
    stop_data = {'line_id': 1, 'station_name': 'Test Station', 'first_stop_yn': True, 'last_stop_yn': False}
    test_client.post('/station_stops', json=stop_data)
    yield stop_data
    # Clean up if needed

@pytest.fixture(scope='function')
def add_railway_line(test_client, add_class, add_origin, add_type):
    # Adding a railway line to test against
    line_data = {
        'line_number': 1,
        'class_code': 'C001',
        'origin_code': 'O001',
        'type_code': 'T001',
        'steam_or_diesel': 'Steam',
        'line_name': 'Test Railway Line',
        'address': '123 Test Street',
        'phone_number': '1234567890',
        'nearest_mainline_station': 'Test Station',
        'total_miles': 10.5,
        'year_opened': 1950
    }
    test_client.post('/railway_lines', json=line_data)
    yield line_data

    




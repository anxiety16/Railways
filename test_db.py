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

# Test for POST /classes
def test_create_class(test_client):
    class_data = {'class_code': 'C002', 'class_description': 'New Test Class'}
    response = test_client.post('/classes', json=class_data)
    assert response.status_code == 201
    assert response.json['message'] == 'created successfully'

# Test for PUT /classes/<class_code>
def test_update_class(test_client, add_class):
    updated_data = {'class_description': 'Updated Test Class'}
    response = test_client.put('/classes/C001', json=updated_data)
    assert response.status_code == 200
    assert response.json['message'] == 'update successfully'

# Test for DELETE /classes/<class_code>
def test_delete_class(test_client, add_class):
    response = test_client.delete('/classes/C001')
    assert response.status_code == 200
    assert 'Class C001 has been deleted' in response.json['message']

# Test for GET /origins
def test_get_origins(test_client, add_origin):
    response = test_client.get('/origins')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert data[0]['origin_code'] == 'O001'

# Test for POST /origins
def test_create_origin(test_client):
    origin_data = {'origin_code': 'O002', 'origin_description': 'New Origin'}
    response = test_client.post('/origins', json=origin_data)
    assert response.status_code == 201
    assert response.json['message'] == 'Created successfully'

# Test for PUT /origins/<origin_code>
def test_update_origin(test_client, add_origin):
    updated_data = {'origin_description': 'Updated Test Origin'}
    response = test_client.put('/origins/O001', json=updated_data)
    assert response.status_code == 200
    assert response.json['message'] == 'update successfully'

# Test for DELETE /origins/<origin_code>
def test_delete_origin(test_client, add_origin):
    response = test_client.delete('/origins/O001')
    assert response.status_code == 200
    assert 'Origin O001 has been deleted' in response.json['message']

# Test for GET /types
def test_get_types(test_client, add_type):
    response = test_client.get('/types')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert data[0]['type_code'] == 'T001'

# Test for POST /types
def test_create_type(test_client):
    type_data = {'type_code': 'T002', 'type_description': 'New Type'}
    response = test_client.post('/types', json=type_data)
    assert response.status_code == 201
    assert response.json['message'] == 'created successfully'


# Test for PUT /types/<type_code>
def test_update_type(test_client, add_type):
    updated_data = {'type_description': 'Updated Test Type'}
    response = test_client.put('/types/T001', json=updated_data)
    assert response.status_code == 200
    assert response.json['message'] == 'update successfully'

# Test for DELETE /types/<type_code>
def test_delete_type(test_client, add_type):
    response = test_client.delete('/types/T001')
    assert response.status_code == 200
    assert 'Type T001 has been deleted' in response.json['message']


# Test for GET /railway_lines/<line_number>
def test_get_railway_line(test_client, add_railway_line):
    response = test_client.get('/railway_lines/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['line_number'] == 1
    assert data['line_name'] == 'Test Railway Line'



# Test for PUT /railway_lines/<line_number>
def test_update_railway_line(test_client, add_railway_line):
    updated_data = {
        'line_name': 'Updated Railway Line',
        'total_miles': 12.5
    }
    response = test_client.put('/railway_lines/1', json=updated_data)
    assert response.status_code == 200
    assert response.json['message'] == 'update successfully'

# Test for DELETE /railway_lines/<line_number>
def test_delete_railway_line(test_client, add_railway_line):
    response = test_client.delete('/railway_lines/1')
    assert response.status_code == 200
    assert 'Railway Line 1 has been deleted' in response.json['message']



   # Test for GET /classes with pagination
def test_get_classes_pagination(test_client):
    # Add multiple classes
    class_data = [
        {'class_code': f'C00{i}', 'class_description': f'Test Class {i}'} 
        for i in range(1, 15)  # Create 14 classes
    ]
    
    for data in class_data:
        test_client.post('/classes', json=data)
    
    # Test default pagination (page 1, limit 10)
    response = test_client.get('/classes') 



@patch('app.db.session.commit')
def test_database_error_handling(mock_commit, test_client):
    """Test database error handling"""
    mock_commit.side_effect = sqlite3.Error('Database error')
    
    class_data = {'class_code': 'C003', 'class_description': 'Test Class'}
    response = test_client.post('/classes', json=class_data)
    assert response.status_code == 500
    assert 'error' in response.json

@patch('app.db.session.add')
def test_database_add_error(mock_add, test_client):
    """Test database add operation failure"""
    mock_add.side_effect = Exception('Database add error')
    
    class_data = {'class_code': 'C004', 'class_description': 'Test Class'}
    response = test_client.post('/classes', json=class_data)
    assert response.status_code == 500
    assert 'error' in response.json


# Test for GET /railway_lines
def test_get_railway_lines(test_client, add_railway_line):
    response = test_client.get('/railway_lines')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert data[0]['line_number'] == 1
    assert data[0]['line_name'] == 'Test Railway Line'


# Test for GET /station_stops
def test_get_station_stops(test_client, add_station_stop):
    response = test_client.get('/station_stops')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert data[0]['station_name'] == 'Test Station'
    assert data[0]['first_stop_yn'] is True
    assert data[0]['last_stop_yn'] is False


# Test JWT protected routes
def test_protected_route(test_client):
    # Test accessing protected route without JWT
    response = test_client.get('/classes')
    assert response.status_code == 401  # Unauthorized
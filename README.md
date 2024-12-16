# Railway Management System API

## Description

A Flask-based REST API for managing railway lines, stations, and related information. The system provides endpoints for managing railway classes, origins, types, railway lines, and station stops with JWT authentication.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Railways
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Set the following environment variables:
```bash
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:root@localhost/preserved
SECRET_KEY=your_secret_key
```

## Database Setup

1. Create the database:
```sql
CREATE DATABASE preserved;
```

2. Initialize the database:
```python
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

## API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/register` | POST | Register new user | No |
| `/login` | POST | User login | No |
| `/classes` | GET | Get all classes | Yes |
| `/classes` | POST | Create new class | Yes |
| `/classes/<class_code>` | GET | Get specific class | Yes |
| `/classes/<class_code>` | PUT | Update class | Yes |
| `/classes/<class_code>` | DELETE | Delete class | Yes |
| `/origins` | GET | Get all origins | No |
| `/origins` | POST | Create new origin | No |
| `/origins/<origin_code>` | GET | Get specific origin | No |
| `/origins/<origin_code>` | PUT | Update origin | No |
| `/origins/<origin_code>` | DELETE | Delete origin | No |
| `/types` | GET | Get all types | No |
| `/types` | POST | Create new type | No |
| `/types/<type_code>` | GET | Get specific type | No |
| `/types/<type_code>` | PUT | Update type | No |
| `/types/<type_code>` | DELETE | Delete type | No |
| `/railway_lines` | GET | Get all railway lines | No |
| `/railway_lines` | POST | Create new railway line | No |
| `/railway_lines/<line_number>` | GET | Get specific railway line | No |
| `/railway_lines/<line_number>` | PUT | Update railway line | No |
| `/railway_lines/<line_number>` | DELETE | Delete railway line | No |
| `/station_stops` | GET | Get all station stops | No |
| `/station_stops` | POST | Create new station stop | No |
| `/station_stops/<station_id>` | GET | Get specific station stop | No |
| `/station_stops/<station_id>` | PUT | Update station stop | No |
| `/station_stops/<station_id>` | DELETE | Delete station stop | No |

## Testing

Run the tests using pytest:

```bash
pytest test_db.py -v
```

The test suite includes:
- Authentication tests
- CRUD operations for all entities
- Error handling
- Database operations
- JWT protection tests

## Models

### User
- username (string)
- password (string)
- role (string)

### Class
- class_code (string)
- class_description (string)

### Origin
- origin_code (string)
- origin_description (string)

### Type
- type_code (string)
- type_description (string)

### RailwayLine
- line_number (integer)
- class_code (string)
- origin_code (string)
- type_code (string)
- line_name (string)
- address (text)
- phone_number (string)
- fax_number (string)
- nearest_mainline_station (string)
- resident_locos_url (text)
- route_map_url (text)
- website_url (text)
- total_miles (decimal)
- year_opened (integer)
- membership_prices (decimal)
- year_built (integer)
- other_details (text)

### StationStop
- station_id (integer)
- line_id (integer)
- next_station_id (integer)
- station_name (string)
- first_stop_yn (boolean)
- last_stop_yn (boolean)
- other_details (text)

## Git Commit Guidelines

Follow conventional commits format:

```
feat: add user authentication
fix: resolve database connection issue
docs: update API documentation
test: add user registration tests
refactor: improve error handling
style: format code according to PEP 8
chore: update dependencies
```

## Error Handling

The API includes comprehensive error handling for:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
```

This README.md provides comprehensive documentation for your Railway Management System API, including:
- Installation instructions
- Configuration details
- API endpoint documentation
- Testing procedures
- Model descriptions
- Git commit guidelines
- Error handling information
- Contributing guidelines
- License information

You can now save this content to your `Railways/README.md` file.
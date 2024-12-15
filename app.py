from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/preserved'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'admin', 'user', etc.


# Model for 'classes' table
class Class(db.Model):
    __tablename__ = 'classes'
    class_code = db.Column(db.String(10), primary_key=True)
    class_description = db.Column(db.String(255), nullable=False)

# Model for 'origins' table
class Origin(db.Model):
    __tablename__ = 'origins'
    origin_code = db.Column(db.String(10), primary_key=True)
    origin_description = db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #6200ea;
                color: white;
                padding: 20px 0;
                text-align: center;
            }
            h1 {
                margin: 0;
                font-size: 2.5em;
            }
            .content {
                text-align: center;
                padding: 50px 20px;
            }
            .content p {
                font-size: 1.2em;
                margin: 20px 0;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 1em;
                color: white;
                background-color: #6200ea;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            .button:hover {
                background-color: #3700b3;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to the Home Page</h1>
        </header>
        <div class="content">
            <p>This is a simple Flask application with a styled home page.</p>
        </div>
    </body>
    </html>
    """
# Initialize the database (only run this once)
# db.create_all()

@app.route('/classes', methods=['GET'])
@jwt_required()
def get_classes():
    try:
        classes = Class.query.all()
        return jsonify([{'class_code': c.class_code, 'class_description': c.class_description} for c in classes])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/classes', methods=['POST'])
def create_class():
    if not request.json or 'class_code' not in request.json or 'class_description' not in request.json:
        abort(400, description="Missing required fields: class_code or class_description")
    
    class_code = request.json['class_code']
    class_description = request.json['class_description']
    
    # Check if the class already exists
    existing_class = Class.query.filter_by(class_code=class_code).first()
    if existing_class:
        abort(400, description="Class with this class_code already exists")
    
    new_class = Class(class_code=class_code, class_description=class_description)
    db.session.add(new_class)
    db.session.commit()

    return jsonify({'message': 'created successfully'}), 201

@app.route('/classes/<class_code>', methods=['PUT'])
def update_class(class_code):
    class_info = Class.query.filter_by(class_code=class_code).first()
    if class_info is None:
        abort(404, description="Class not found")

    if not request.json:
        abort(400, description="Request must be JSON")

    class_info.class_description = request.json.get('class_description', class_info.class_description)
    db.session.commit()

    return jsonify({'message': 'update successfully'})



@app.route('/classes/<class_code>', methods=['DELETE'])
def delete_class(class_code):
    class_info = Class.query.filter_by(class_code=class_code).first()
    if class_info is None:
        abort(404, description="Class not found")

    db.session.delete(class_info)
    db.session.commit()

    return jsonify({'message': f'Class {class_code} has been deleted'}), 200

@app.route('/origins', methods=['GET'])
def get_origins():
    origins = Origin.query.all()
    return jsonify([{'origin_code': o.origin_code, 'origin_description': o.origin_description} for o in origins])

@app.route('/origins', methods=['POST'])
def create_origin():
    if not request.json or 'origin_code' not in request.json or 'origin_description' not in request.json:
        abort(400, description="Missing required fields: origin_code or origin_description")
    
    origin_code = request.json['origin_code']
    origin_description = request.json['origin_description']
    
    # Check if the origin already exists
    existing_origin = Origin.query.filter_by(origin_code=origin_code).first()
    if existing_origin:
        abort(400, description="Origin with this origin_code already exists")
    
    new_origin = Origin(origin_code=origin_code, origin_description=origin_description)
    db.session.add(new_origin)
    db.session.commit()

    return jsonify({'message': 'Created successfully'}), 201

@app.route('/origins/<origin_code>', methods=['GET'])
def get_origin(origin_code):
    origin_info = Origin.query.filter_by(origin_code=origin_code).first()
    if origin_info is None:
        abort(404, description="Origin not found")
    return jsonify({'origin_code': origin_info.origin_code, 'origin_description': origin_info.origin_description})

@app.route('/origins/<origin_code>', methods=['PUT'])
def update_origin(origin_code):
    origin_info = Origin.query.filter_by(origin_code=origin_code).first()
    if origin_info is None:
        abort(404, description="Origin not found")

    if not request.json:
        abort(400, description="Request must be JSON")

    origin_info.origin_description = request.json.get('origin_description', origin_info.origin_description)
    db.session.commit()

    return jsonify({'message': 'update successfully'})

@app.route('/origins/<origin_code>', methods=['DELETE'])
def delete_origin(origin_code):
    origin_info = Origin.query.filter_by(origin_code=origin_code).first()
    if origin_info is None:
        abort(404, description="Origin not found")

    db.session.delete(origin_info)
    db.session.commit()

    return jsonify({'message': f'Origin {origin_code} has been deleted'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
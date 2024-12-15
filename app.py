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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
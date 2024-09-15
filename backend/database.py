from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

db = SQLAlchemy()  # Define db instance

def init_db(app):
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)  # Initialize db with app
        print("Database connection successful.")
    except KeyError as e:
        print(f"Environment variable not set: {e}")
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def test_db():
    try:
        with db.session.begin(subtransactions=True):
            db.session.execute('SELECT 1')  # Test query to check database connection
        return True, None
    except SQLAlchemyError as e:
        return False, str(e)

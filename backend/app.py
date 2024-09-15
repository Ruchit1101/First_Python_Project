from flask import Flask, jsonify

from database import init_db, test_db


app = Flask(__name__)
init_db(app)
@app.route('/test_db')
def test_db_route():
    success, error = test_db()
    if success:
        return jsonify({"message": "Database connection is working!"})
    else:
        return jsonify({"error": "Database connection failed.", "details": error}), 500
@app.route('/')   #Entry Point API
def home():
       return "Hello, Flask"

if __name__ == '__main__':
       print("Server running")
       app.run(debug=True, port =5000)  #PORT NUMBER
       



from flask import Blueprint, request, jsonify
from backend.controller.createrecord import create_student_record
from backend.controller.readingrecord import  female_student_name, get_lowest_maths, get_sciencesocial

main = Blueprint('main', __name__)

# ROUTES FOR TASK 1:
@main.route('/create_record', methods=['POST'])
def create_record():
       data = request.get_json()
       id =data.get('id')
       name=data.get('name')
       gender=data.get('gender')
       maths_marks=data.get('maths_marks')
       science_marks=data.get('science_marks')
       social_marks=data.get('social_marks')
       

       # VALIDATE INPUT(IF ANY ERRORS IN THE FORM(NOT NULL))
       if not name or not gender:
              return jsonify({"message":"Missing required fields"}),400
       return jsonify(*create_student_record(id, name, gender, maths_marks, science_marks, social_marks))  


@main.route('/specific_record', methods=['GET'])
def specific_record():
       query_type = request.args.get('query_type')
       if query_type == 'get_lowest_maths':
        return jsonify(*get_lowest_maths())  # Unpack tuple response
       elif query_type == 'get_sciencesocial':
        return jsonify(*get_sciencesocial())  # Unpack tuple response
       elif query_type == 'female_student_name':
        return jsonify(*female_student_name())  # Unpack tuple response
       else:
        return jsonify({
            "message": "Invalid query_type provided!!!"
        }), 400
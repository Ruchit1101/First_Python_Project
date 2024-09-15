from ..model import Students, GenderEnum
from ..database import db

# TASK 1:- INSERTING DATA INTO  DATABASE......
def create_student_record(id, name, gender, maths_marks, science_marks, social_marks):
       try:
              gender_enum = GenderEnum[gender]

              new_student = Students(
                     id=id,
                     name=name,
                     gender=gender_enum,
                     maths_marks=maths_marks,
                     science_marks=science_marks,
                     social_marks=social_marks
              )
              db.session.add(new_student)
              db.session.commit()
              return{
                     "message": "Record Successfully Inserted"
              },201
       except Exception as e:
              db.session.rollback()
              return{
                     "message":f"An error encountered while inserting into database: {str(e)}"
              },500




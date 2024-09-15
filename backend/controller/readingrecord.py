from ..model import Students
from . import db

# 2.1: Take five students' information who received the lowest math grades from the students table.
def get_lowest_maths():
       try:
              obj = Students.query.order_by(Students.maths_marks.asc().limit(5)).all()
              return [{
                     "id":s.id,
                     "name":s.name,
                     "maths_marks":str(s.maths_marks)
              } for s in obj],200
       except Exception as e:
              return {"message":"An error occured while fetching Maths marks: {str(e)}"},500

# 2.2  Take information on students from the students table who excel in science but struggle in social studies.
def get_sciencesocial():
       try:
              obj = Students.query.filter(Students.science_marks > 75, Students.social_marks < 30).all()
              return [{
                     "id":s.id,
                     "name":s.name,
                     "science_marks":str(s.science_marks),
                     "socail_marks":str(s.social_marks)
              } for s in obj],200
       except Exception as e:
              return {"message":"An error occured while fetching Science And Social Marks: {str(e)}"},500

#  2.3: Get information about female students whose names begin with "a" from the  students table
def female_student_name():
       try:
              obj = Students.query.filter(Students.gender=="Female", Students.name.ilike("a%")).all()
              return [{
                     "id":s.id,
                     "name":s.name,
                     "gender":s.gender,
                     "maths_marks":str(s.maths_marks),
                     "science_marks":str(s.science_marks),
                     "socail_marks":str(s.social_marks)
              } for s in obj],200
       except Exception as e:
              return {"message":"An error occured while fetching female students records: {str(e)}"},500
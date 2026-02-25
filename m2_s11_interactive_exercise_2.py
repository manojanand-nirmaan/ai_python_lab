 #Initialize database

students_db = []


def add_student(db, roll_id, name, branch):

# Create student dictionary

    student = {

    'roll': roll_id,

    'name': name,

    'branch': branch

    }

    db.append(student)

 

def find_student(db, roll_id):

# TODO: Implement search logic

    for s in db:

        if s['roll'] == roll_id:

            return s

    return None

    

    # Usage

add_student(students_db, 101, "Anu", "CSE")


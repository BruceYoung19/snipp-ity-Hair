from datetime import date 

class User:
    def __init__(self, id, fname,lname,email,age,status):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
        self.status=status

def calculate_age():
    today = date.today()
    return age


import unittest
from user import User

class TestUserConstructor(unittest.TestCase):
    def test_new_user(self):
        """GIVEN a user """
        """WHEN a user is created """
        person = User(1,"John","Pope", "John.fresh@gmail.com", 40,"Active")
        """THEN check id,first name, last name, email, age , status is defined """
        self.assertEqual(person.id,1)
        self.assertEqual(person.fname,"John")
        self.assertEqual(person.lname, "Pope")
        self.assertEqual(person.email,"John.fresh@gmail.com")
        self.assertEqual(person.age, 40)
        self.assertEqual(person.status, "Active")
    
    def test_user_age(self):
        """GIVEN a name and age are positive """
        """WHEN a person is created """
        person = User(1,"John","Pope", "John.fresh@gmail.com", 40,"Active")
        """ THEN the age should be greater than 0 """
        self.assertGreater(person.age,0)

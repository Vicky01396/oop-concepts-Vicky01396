import unittest
from exercise.solution import Person, User, Employee

class TestPersonUserEmployee(unittest.TestCase):
    def test_person(self):
        person = Person("John", "Doe", "2000-01-01")
        self.assertEqual(person.display_info(), "This is John Doe, born on 2000-01-01")
        self.assertEqual(person.get_full_name(), "John Doe")

    def test_user(self):
        user = User("Alice", "Smith", "1995-05-05", "alice123")
        user.password = "new_password" 
        self.assertEqual(user.display_info(), "This is Alice Smith, born on 1995-05-05 with username: alice123")
        self.assertEqual(user.to_dictionary(), {'first_name': 'Alice', 'last_name': 'Smith', 'birthdate': '1995-05-05', 'username': 'alice123', 'password': 'new_password'})

    def test_employee(self):
        employee = Employee("Bob", "Johnson", "1990-02-15", "E12345")
        employee.employee_id = "E54321" 
        self.assertEqual(employee.display_info(), "This is Bob Johnson, born on 1990-02-15 with employee ID: E54321")
        self.assertEqual(employee.to_dictionary(), {'first_name': 'Bob', 'last_name': 'Johnson', 'birthdate': '1990-02-15', 'employee_id': 'E54321'})

    def test_to_json_string(self):
        user1 = User("Alice", "Smith", "1995-05-05", "alice123")
        user1.password = "new_password"
        employee1 = Employee("Bob", "Johnson", "1990-02-15", "E54321")
        employee1.employee_id = "E54321"
        objects = [user1, employee1]
        json_string = Person.to_json_string([obj.to_dictionary() for obj in objects])
        expected_json = '[{"first_name": "Alice", "last_name": "Smith", "birthdate": "1995-05-05", ' \
                        '"username": "alice123", "password": "new_password"}, ' \
                        '{"first_name": "Bob", "last_name": "Johnson", "birthdate": "1990-02-15", ' \
                        '"employee_id": "E54321"}]'
        self.assertEqual(json_string, expected_json)


    def test_save_to_file(self):
        user1 = User("Alice", "Smith", "1995-05-05", "alice123")
        user1.password = "new_password"
        employee1 = Employee("Bob", "Johnson", "1990-02-15", "E54321")
        employee1.employee_id = "E54321"

        objects = [user1, employee1]

        Person.save_to_file(objects)

        with open('Person.json', 'r') as file:
            saved_json = file.read()

        expected_json = '[{"first_name": "Alice", "last_name": "Smith", "birthdate": "1995-05-05", ' \
                        '"username": "alice123", "password": "new_password"}, ' \
                        '{"first_name": "Bob", "last_name": "Johnson", "birthdate": "1990-02-15", ' \
                        '"employee_id": "E54321"}]'

        self.assertEqual(saved_json, expected_json)


    def test_password_validation(self):
        user = User("Alice", "Smith", "1995-05-05", "alice123")
        
        with self.assertRaises(ValueError):
            user.password = "pass"

        try:
            user.password = "password"
        except ValueError:
            self.fail("Password with 8 characters should not raise an error")
    
    def test_employee_id_validation(self):
        employee = Employee("Bob", "Johnson", "1990-02-15", "E12345")
    
        try:
            employee.employee_id = "E54321"
        except ValueError:
            self.fail("Employee ID starting with 'E' should not raise an error")
        
        with self.assertRaises(ValueError):
            employee.employee_id = "X54321"
    
    def test_user_to_dictionary(self):
        user = User("Alice", "Smith", "1995-05-05", "alice123")
        user.password = "new_password"
        
        user_dict = user.to_dictionary()
        expected_dict = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'birthdate': '1995-05-05',
            'username': 'alice123',
            'password': 'new_password'
        }
        self.assertEqual(user_dict, expected_dict)
    
    def test_employee_to_dictionary(self):
        employee = Employee("Bob", "Johnson", "1990-02-15", "E12345")
        employee.employee_id = "E54321"
        
        employee_dict = employee.to_dictionary()
        expected_dict = {
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'birthdate': '1990-02-15',
            'employee_id': 'E54321'
        }
        self.assertEqual(employee_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

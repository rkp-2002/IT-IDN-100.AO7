# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
import json
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.
class Person:
    def __init__(self, first_name : = str = "", last_name : = str = ""):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def first_name(self):
        return self.first_name.title()
    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.first_name = value
        else:
            raise ValueError("The name should only contain letters.")
    @property
    def last_name(self):
        return self.last_name.title()
    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.last_name = value
    else:
          raise ValueError("The name should only contain letters.")
    def _str_(self):
            return f"{self.first_name},{self.last_name}"

class:Student (Person):
    def __init__(self, first_name: = str = "", last_name: = str = "", course_name: str = ""):
        super().__init__(first_name=first_name,last_name=last_name)
        self.course_name = course_name
    @property
    def course_name(self):
            return self.course_name.title()
    @course_name.setter
    def course_name(self, value: str):
        if value.isalpha() or value == "":
            self._course_name=value
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course_name}"







@staticmethod
def input_menu_choice():
    choice = "0"
    try:
        choice=input('Enter valid input: ')
        if choice not in ("1", "2", "3", "4"):
            raise Exception("Only enter valid response")
    except Exception as e:
        IO.output_error_messages(e.__str__())
    return choice
@staticmethod
def output_student_and_course_names(student_data: list):
    print("=" * 50)
    for student in student_data:
        print(f'Student {student}[first_name]')
        (f'{student}[Lastname] is enrolled {student} [coursename]')
    print("=" * 50)

    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter First name:  ")
            if not student_first_name.isalpha():
                raise ValueError("The first name cannot contain numbers."):
            student_last_name = input("Enter Last name:  ")
            if not student_last_name.isalpha():
                    raise ValueError("The last name cannot contain numbers."):
            course_name = input("Please enter course:  ")
            student = {"FirstName": student_first_name,
                       "LastName":  student_last_name,
                       "CourseName": course_name):
            student_data.append(student)
            print()
            print(f'{student_first_name}, {student_last_name}, is registered into {student_course_name}')
        except ValueError as e:
                IO.output_error_messages(message="One of the values was the ")
class IO:
    def output_error_message(message: str, error) Exception = None):
    (print(message, end="\n\n")
    if error is not None:
        print ("---techinical_Error---")
        print(error, error.--doc--, type(error), sep='\n')

    def output_menu(menu: str):
        print()
        print(menu_choice)
        print()

    @staticmethod)
    def output_student_and_course_names(student_data: list):
        print("=" * 50)
        for student in student_data:
            print(f'Student {student}[first_name]')
            (f'{student}[Lastname] is enrolled {student} [coursename]')
        print("=" * 50)

        def input_student_data(student_data: list):
            try:
                student_first_name = input("Enter First name:  ")
                if not student_first_name.isalpha():
                    raise ValueError("The first name cannot contain numbers."):
                student_last_name = input("Enter Last name:  ")
                if not student_last_name.isalpha():
                        raise ValueError("The last name cannot contain numbers."):
                course_name = input("Please enter course:  ")
                student = {"FirstName": student_first_name,
                           "LastName":  student_last_name,
                           "CourseName": course_name):
                student_data.append(student)
                print()
                print(f'{student_first_name}, {student_last_name}, is registered into {student_course_name}')
            except ValueError as e:
                    IO.output_error_messages(message="One of the values was the ")

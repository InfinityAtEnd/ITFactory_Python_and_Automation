"""
Strategy Design Patterns - Behavioral Design
USAGE:
	- best used when user intent result in calling a method that is implemented in multiple interfaces.

PROS:
	- provides the user a simple way of choosing what he wishes to do (ex: pay with visa sau PayPal, etc..)
CONS:
	-

Rules of the Strategy Pattern:
	-
"""
import random



def alphabeticaly(the_student_list):
	return the_student_list.sort()


def inverse_alphabeticaly(the_student_list):
	the_list = the_student_list.sort(reverse=True)
	return the_list


def random_order(the_student_list):
	random.shuffle(the_student_list)
	return the_student_list


class ClassRoom:
	def __init__(self):
		self.students = []

	def add_student(self, student):
		self.students.append(student)
		print(f'{student} is present')
		print(f'present student so far: {self.students}')

	def students_survey(self, strategy):
		survey_order = strategy(self.students)
		print(f'the survey_order: {survey_order}')
		for student in survey_order:
			print(f'current student: {student}')
			self.the_survey(student)

	@staticmethod
	def the_survey(student):
		print(f'{student} what have you learned for today? ')


# creating the class room
my_class_room = ClassRoom()

# checking who is present
my_class_room.add_student('Marian')
my_class_room.add_student('Daniel')
my_class_room.add_student('Stelian')
my_class_room.add_student('Eli')
my_class_room.add_student('Tabeea')

# calling the survey with the desired strategy
print('Alphabeticaly Strategy:')
my_class_room.students_survey(alphabeticaly)
print('Inverse Alphabeticaly Strategy:')
my_class_room.students_survey(inverse_alphabeticaly)
print('Random Strategy:')
my_class_room.students_survey(random_order)

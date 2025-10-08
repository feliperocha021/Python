class Student:
  class_year = 2025
  num_students = 0

  def __init__(self, name, age):
    self.anme = name
    self.age = age
    Student.num_students += 1

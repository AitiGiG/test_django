from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=40)
    experience = models.IntegerField()
    students = models.ManyToManyField(Student, related_name='teachers', related_query_name='teacher')



# student1 = Student.objects.create(name='student1',age=15)
# student2 = Student.objects.create(name='student2',age=16)
# student3 = Student.objects.create(name='student3',age=17)
# teacher1 = Teacher.objects.create(name='teacher1', subject='Math', experience= 10)
# teacher1.students.set([student1 , student2])
# teacher1.students.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>

# teacher2 = Teacher.objects.create(name='teacher2', subject='Geograph', experience= 5)
# student1.teachers.set([teacher1 ,teacher2])
# student1.teachers.all()
# <QuerySet [<Teacher: Teacher object (1)>, <Teacher: Teacher object (2)>]>

# realeted_name | realeted_query_name
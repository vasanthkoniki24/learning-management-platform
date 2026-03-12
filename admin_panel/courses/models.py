from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor_id = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    



class Lesson(models.Model):
    course_id = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField()





class Enrollment(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()
    enrolled_on = models.DateTimeField(auto_now_add=True)





class Progress(models.Model):
    enrollment_id = models.IntegerField()
    completed_lessons = models.IntegerField()
    progress_percent = models.FloatField()



# Create your models here.

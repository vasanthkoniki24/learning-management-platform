from django.db import models


class User(models.Model):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor')
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    status = models.CharField(max_length=20, default="active")
    is_premium = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title


class Lesson(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    enrolled_on = models.DateTimeField(auto_now_add=True)


class Progress(models.Model):

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )

    completed_lessons = models.IntegerField(default=0)
    progress_percent = models.FloatField(default=0)


class Plan(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name
    

class Subscription(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    status = models.CharField(max_length=20,default="active")



class Payment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)

    amount = models.FloatField()

    payment_date = models.DateTimeField(auto_now_add=True)

# Create your models here.

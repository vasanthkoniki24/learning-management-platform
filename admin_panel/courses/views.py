# from django.shortcuts import render
# from .models import User, Course, Enrollment 
# from django.db.models import Count


# def dashboard(request):

#     total_users = User.objects.count()
#     total_courses = Course.objects.count()
#     total_enrollments = Enrollment.objects.count()

#     courses = Course.objects.all()

#     labels = []
#     data = []

#     for course in courses:
#         count = Enrollment.objects.filter(course_id = course.id).count()
#         labels.append(course.title)
#         data.append(count)

#     # # Top enrolled courses
#     # course_stats = (
#     #     Course.objects
#     #     .annotate(enroll_count=Count('enrollment'))
#     #     .values('title', 'enroll_count')
#     # )

#     # labels = [c['title'] for c in course_stats]
#     # data = [c['enroll_count'] for c in course_stats]



#     context = {
#         "total_users": total_users,
#         "total_courses": total_courses,
#         "total_enrollments": total_enrollments,
#         "labels": labels,
#         "data": data
#     }


#     return render(request, "dashboard.html",context)
# # Create your views here.


from django.shortcuts import render
from .models import User, Course, Enrollment
import json


def dashboard(request):

    users = User.objects.all()
    courses = Course.objects.all()
    enrollments = Enrollment.objects.all()

    total_users = users.count()
    total_courses = courses.count()
    total_enrollments = enrollments.count()

    user_names = [u.name for u in users]
    course_names = [c.title for c in courses]

    enrollment_users = []

    for e in enrollments:
        user = User.objects.filter(id=e.user_id).first()
        if user:
            enrollment_users.append(user.name)

    labels = []
    data = []

    for course in courses:
        count = Enrollment.objects.filter(course_id=course.id).count()
        labels.append(course.title)
        data.append(count)

        if count > 0:

            labels.append(course.title)
            data.append(count)


    context = {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments,
        "user_names": user_names,
        "course_names": course_names,
        "enrollment_users": enrollment_users,
        "labels": labels,
        "data": data,
    }

    return render(request, "dashboard.html", context)
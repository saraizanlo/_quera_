from django.urls import path
from user.views import teacher_list, student_list, teacher_detail, student_detail, add_teacher_to_class, add_teacher_to_bootcamp, add_student_answer, add_student_to_bootcamp,add_student_to_class, register_new_student, register_new_teacher

urlpatterns = [
    path('teacher/', teacher_list),
    path('student/', student_list),
    path('teacher/<str:input_email>/', teacher_detail),
    path('student/<str:input_email>/', student_detail),
    path('add_teacher_to_class/', add_teacher_to_class),
    path('add_teacher_to_bootcamp/', add_teacher_to_bootcamp),
    path('add_student_answer/', add_student_answer),
    path('add_student_to_bootcamp/', add_student_to_bootcamp),
    path('add_student_to_class/', add_student_to_class),
    path('register_new_student/',register_new_student),
    path('register_new_teacher/',register_new_teacher)
]
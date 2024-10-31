from django.urls import path
from learning.views import add_assignmet_to_class, add_bootcamp, add_lesson_to_class, bootcamp_list, classes_list, creat_class, get_bootcamp, get_class 

urlpatterns = [
    path('add_assignmet_to_class', add_assignmet_to_class),
    path('add_bootcamp', add_bootcamp),
    path('add_lesson_to_class', add_lesson_to_class),
    path('bootcamp_list', bootcamp_list),
    path('classes_list', classes_list),
    path('creat_class', creat_class),
    path('get_bootcamp/<str:bootcamp_id>', get_bootcamp),
    path('get_class/<str:class_id>', get_class)
]
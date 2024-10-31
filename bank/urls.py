from django.urls import path
from bank.views import questions_list , lessons_list , add_question, add_lesson, get_lesson, get_question

urlpatterns = [
    path('questions/', questions_list),
    path('lessons/', lessons_list),
    path('add-question/', add_question),
    path('add-lesson/', add_lesson),
    path('get-lesson/<str:lesson_id>', get_lesson),
    path('get-question/<str:question_id>', get_question)
]
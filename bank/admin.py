from django.contrib.admin import register, ModelAdmin
from bank.models import Question , Lesson



@register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = [
        "name",
        "form",
        "answer",
        "publish_date",
        "level",
    ]
    search_fields = [
        'name'
    ]

@register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = [
        "subject",
        "text"
    ] 
    search_fields = [
        'subject'
    ]
    



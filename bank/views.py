from django.shortcuts import render
from bank.models import Question , Lesson
from learning.models import Class , Bootcamp
from user.models import Teacher, Student, Student_answer
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


def questions_list(request):
    questions = Question.objects.all()
    questions_list_ = []
    for question in questions:
        questions_list_.append({
            "name": question.name,
            "form": question.form,
            "answer": question.answer,
            "publish_date": question.publish_date,
            "level": question.level,
        })
    return JsonResponse(questions_list_, safe=False)

def lessons_list(request):
    lessons = Lesson.objects.all()
    lessons_list_ = []
    for lesson in lessons:
        lessons_list_.append({
            'subject': lesson.subject,
            'text': lesson.text,
        }
        )
    return JsonResponse(lessons_list_, safe=False)

@csrf_exempt
def add_question(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question_name = data['name']
            if Question.objects.filter(name=question_name).exists():
                return JsonResponse({'message': 'Question already exists'}, safe=False)
            question_form = data['form']
            question_answer = data['answer']
            question_publish_date = data['publish_date']
            question_level = data['level']
            question = Question.objects.create(name = question_name, form = question_form, answer = question_answer, publish_date = question_publish_date, level = question_level)
            question.save()

            return JsonResponse({'message': 'Question added successfully'}, safe=False)
        except IntegrityError:
            return JsonResponse({'message': 'Question already exists'}, safe=False)
        
        except KeyError:
            return JsonResponse({'message': 'Invalid request data'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, safe=False)
        
        except Exception as e:
            return JsonResponse({'message': 'An error occurred'}, safe=False)
        
    
    return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def add_lesson(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lesson_subject = data['subject']
            lesson_text = data['text']
            lesson = Lesson.objects.create(subject = lesson_subject, text = lesson_text)
            lesson.save()
            return JsonResponse({'message': 'Lesson added successfully'}, safe=False)
        except KeyError:
            return JsonResponse({'message': 'Invalid request data'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, safe=False)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred'}, safe=False)
    else:    
        return JsonResponse({'message': 'Invalid request method'})

def get_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        question_data = {
            'name': question.name,
            'form': question.form,
            'answer': question.answer,
            'publish_date': question.publish_date,
            'level': question.level,
        }
        return JsonResponse(question_data, safe=False)
    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question not found'}, safe=False)
    except Exception as e:
        return JsonResponse({'message': 'An error occurred'}, safe=False)

def get_lesson(request, lesson_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        lesson_data = {
            'subject': lesson.subject,
            'text': lesson.text,
        }
        return JsonResponse(lesson_data, safe=False)
    except Lesson.DoesNotExist:
        return JsonResponse({'message': 'Lesson not found'}, safe=False)
    except Exception as e:
        return JsonResponse({'message': 'An error occurred'}, safe=False)
            
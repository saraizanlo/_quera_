from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher, Student, Student_answer
from django.shortcuts import render
import json
from django.db import IntegrityError
from .models import Question, Class, Bootcamp
from django.contrib.auth.hashers import make_password
def teacher_list(request):
    teachers = Teacher.objects.all()
    data = []
    for teacher in teachers:
        data.append({
            'name' : teacher.name, 
            'last_name' : teacher.last_name,
            'email' : teacher.email,
            'classes' : list(teacher.classes.values('name')),
            'bootcamps' : list(teacher.bootcamps.values('name'))
        })
    return JsonResponse(data, safe=False)

def student_list(request):
    students = Student.objects.all()
    data = []
    for student in students:
        data.append({
            'name' : student.name,
            'last_name' : student.last_name,
            'email' : student.email,
            'classes' : list(student.classes.values('name')),
            'bootcamps' : list(student.bootcamps.values('name'))
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def teacher_detail(request, input_email):
    if request.method == 'GET':
        try:
            teacher = Teacher.objects.get(email=input_email)
            data = {
                'name' : teacher.name,
                'last_name' : teacher.last_name,
                'email' : teacher.email,
                'classes' : [cls.name for cls in teacher.classes.all()],
                'bootcamps' : [bootcamp.name for bootcamp in teacher.bootcamps.all()]
            }
            return JsonResponse(data, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Ger request required'}, status=405)


@csrf_exempt
def student_detail(request, input_email):
    if request.method == 'GET':
        try:
            student = Student.objects.get(email=input_email)
            data = {
                'name' : student.name,
                'last_name' : student.last_name,
                'email' : student.email,
                'classes' : [cls.name for cls in student.classes.all()],
                'bootcamps' : [bootcamp.name for bootcamp in student.bootcamps.all()]
            }
            return JsonResponse(data, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'student does not exist'}, safe=False)
    else:
        return JsonResponse({'error': 'Ger request required'}, status=405)

@csrf_exempt
def add_student_answer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(email=data['student_email'])
            question = Question.objects.get(id=data['question_id'])
            answer = data['answer']
            true_percentange = data['true_percentange']
            student_answer = Student_answer.objects.create(student=student, question=question, answer=answer, true_percentange=true_percentange)
            student_answer.save()
            return JsonResponse({'message': 'student answer added successfully'}, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'student does not exist'}, safe=False)
        except Question.DoesNotExist:
            return JsonResponse({'error': 'question does not exist'},safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_student_to_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(email=data['student_email'])
            class_id = data['class_id']
            class_to_add = Class.objects.get(id=class_id)
            student.classes.add(class_to_add)
            student.save()
            return JsonResponse({'message': 'student added to class successfully'}, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'student does not exist'}, safe=False)
        except Class.DoesNotExist:
            return JsonResponse({'error': 'class does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_student_to_bootcamp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(email=data['student_email'])
            bootcamp_id = data['bootcamp_id']
            bootcamp_to_add = Bootcamp.objects.get(id=bootcamp_id)
            student.bootcamps.add(bootcamp_to_add)
            student.save()
            return JsonResponse({'message': 'student added to bootcamp successfully'}, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'student does not exist'}, safe=False)
        except Bootcamp.DoesNotExist:
            return JsonResponse({'error': 'bootcamp does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_teacher_to_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            teacher = Teacher.objects.get(email=data['teacher_email'])
            class_id = data['class_id']
            class_to_add = Class.objects.get(id=class_id)
            teacher.classes.add(class_to_add)
            teacher.save()
            return JsonResponse({'message': 'teacher added to class successfully'}, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except Class.DoesNotExist:
            return JsonResponse({'error': 'class does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_teacher_to_bootcamp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            teacher = Teacher.objects.get(email=data['teacher_email'])
            bootcamp_id = data['bootcamp_id']
            bootcamp_to_add = Bootcamp.objects.get(id=bootcamp_id)
            teacher.bootcamps.add(bootcamp_to_add)
            teacher.save()
            return JsonResponse({'message': 'teacher added to bootcamp successfully'}, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except Bootcamp.DoesNotExist:
            return JsonResponse({'error': 'bootcamp does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
@csrf_exempt
def register_new_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            last_name = data['last_name']
            email = data['email']
            password = make_password(data['password'])
            if Student.objects.filter(email=email).exists():
                return JsonResponse({'error': 'student with this email already exists'}, safe= False)
            
            student = Student.objects.create(name=name, last_name=last_name, email=email, password=password)
            
            student.save()
            return JsonResponse({'message': 'student registered successfully'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        except IntegrityError as e:
            return JsonResponse({'error': str(e)}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def register_new_teacher(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            last_name = data['last_name']
            email = data['email']
            password = make_password(data['password'])
            if Teacher.objects.filter(email=email).exists():
                return JsonResponse({'error': 'teacher with this email already exists'}, safe= False)

            teacher = Teacher.objects.create(name=name, last_name=last_name, email=email, password=password)

            teacher.save()
            return JsonResponse({'message': 'teacher registered successfully'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except IntegrityError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
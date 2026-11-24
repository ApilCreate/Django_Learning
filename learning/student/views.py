from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Students

@api_view(['GET','POST','PATCH','DELETE'])
def View_Students(request):
    if request.method == "POST":
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        age = request.data.get('age')
        grade = request.data.get('grade')
        address = request.data.get('address')
        contact = request.data.get('contact')
        students = Students.objects.create(first_name= first_name, last_name=last_name, age = age, grade = grade, address = address, contact = contact)
        return JsonResponse(
            {
                "message": "New Student Record Created Successfully",
                "student_id": students.id,
            },
            status=201,
        )
    elif request.method == "GET":
        students = Students.objects.all()
        data = [
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "grade": student.grade,
                "address": student.address,
                "contact": student.contact,
            }
            for student in students
        ]
        return JsonResponse(data, safe=False)
    elif request.method == "PATCH":
        student_id = request.data.get('id')
        student = get_object_or_404(Students, id=student_id)
        if 'first_name' in request.data:
            student.first_name = request.data['first_name']
        if 'last_name' in request.data:
            student.last_name = request.data['last_name']
        if 'age' in request.data:
            student.age = request.data['age']
        if 'grade' in request.data:
            student.grade = request.data['grade']
        if 'address' in request.data:
            student.address = request.data['address']
        if 'contact' in request.data:
            student.contact = request.data['contact']
        student.save()
        return JsonResponse({"message": "Student ID updated successfully"})
    elif request.method == "DELETE":
        student_id = request.data.get('id')
        student = get_object_or_404(Students, id=student_id)
        student.delete()
        return JsonResponse({"message": "Student ID Delete Successfully"})


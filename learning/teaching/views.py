from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Teaching

def create_teacher(request):

        Teaching.objects.create(
            name="Ram",
            faculty="Science",
            shift="Day"
        )

        return HttpResponse("Teacher successfully created!!")

def retrive_teacher(request):
    
    teachers = Teaching.objects.all()
    result = ""

    for teacher in teachers:
        result += f"""
            Name: {teacher.name}<br>
            Faculty: {teacher.faculty}<br>
            Shift: {teacher.shift}<br>
            <hr>
        """
    return HttpResponse(result if result else "No teachers found.")


def update_teacher(request, pk):
    teacher = get_object_or_404(Teaching, pk=pk)

    teacher.name = request.GET.get("name", teacher.name)
    teacher.faculty = request.GET.get("faculty", teacher.faculty)
    teacher.shift = request.GET.get("shift", teacher.shift)
    teacher.save()

    return HttpResponse("Teacher successfully updated!!")


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teaching, pk=pk)
    teacher.delete()

    return HttpResponse("Teacher successfully deleted!!")
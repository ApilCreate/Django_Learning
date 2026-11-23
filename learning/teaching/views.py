from django.http import HttpResponse
from .models import Teaching

def create_teacher(request):

        Teaching.objects.create(
            name="Ram",
            faculty="Science",
            shift="Day"
        )

        return HttpResponse("Teacher successfully created!!")
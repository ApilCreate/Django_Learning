from django.http import JsonResponse
from .models import Organization
from rest_framework.decorators import api_view

@api_view(['POST','GET'])
def organization_view(request):
    if request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        organization = Organization.objects.create(name=name, description=description)
        return JsonResponse({'message':'Organization created successfully', 'organization_id': organization.id})
    elif request.method == 'GET':
        organizations = Organization.objects.all()
        data = [{'id': org.id, 'name': org.name, 'description': org.description} for org in organizations]
        return JsonResponse(data, safe=False)

# @api_view(['GET'])
# def organization_description(request):
#     if request.method == 'GET':
#         organizations = Organization.objects.all()
#         data = [{'id': org.id, 'description': org.description} for org in organizations]
#         return JsonResponse(data, safe=False)

# @api_view(['GET'])
# def organization_name(request):
#     if request.method == 'GET':
#         organizations =  Organization.objects.all()
#         data = [{'id': org.id, 'name': org.name} for org in organizations]
#         return JsonResponse(data, safe=False)

# @api_view(['POST'])
# def add_org_name(request):
#     if request.method == 'POST':
#         name = request.data.get('name')
#         organization = Organization.objects.create(name= name)
#         return JsonResponse({'message':'Organization created successfully', 'organization_id': organization.id, 'organization_name': organization.name})
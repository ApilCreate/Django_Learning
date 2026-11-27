from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Parent
from .serializers import ParentSerializer
from rest_framework import status

@api_view(['GET'])
def view_parent(request):
    parent = Parent.objects.all()
    data = list(parent.values())
    return Response(data)

@api_view(['GET'])
def get_parent(request, pk):
    parent = Parent.objects.get(id = pk)
    serializer = ParentSerializer(parent)
    return Response(serializer.data)

@api_view(['POST'])
def create_parent_entry(request):
    # first_name = request.data.get('first_name')
    # last_name = request.data.get('last_name')
    # address = request.data.get('address')
    # student_name = request.data.get('student_name')

    # parent = Parent.objects.create(
    #     first_name = first_name,
    #     last_name = last_name,
    #     address = address,
    #     student_name = student_name
    # )
    serializer = ParentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Parent Id Created Successfully!!", "Parent_Id" : serializer.data.get("id")}, status=status.HTTP_201_CREATED)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['PATCH'])
def update_parent(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    serializer = ParentSerializer(parent, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_parent(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    parent.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

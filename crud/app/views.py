from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers


class StudentAPIView(APIView):

    # CREATE
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # READ (ALL or SINGLE)
    def get(self, request, id=None):
        if id:
            student = get_object_or_404(Student, id=id)
            serializer = StudentSerializers(student)
            return Response(serializer.data, status=status.HTTP_200_OK)

        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # UPDATE
    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

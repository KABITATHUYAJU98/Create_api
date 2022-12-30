from django.shortcuts import render

#package for api
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializers import StudentSerializer
from rest_framework.request import Request 
from .models import Student

#API views with class based views
class StudentApiView(APIView):
    def get(self,request):
        student_list=Student.objects.all() 
        serializer=StudentSerializer(student_list,many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self,request):
        data={
            'name':request.data.get('name'),
            'roll':request.data.get('roll'),
            'city':request.data.get('city'),
        }

        serializer=StudentSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentIdApiView(APIView):

    def get_object(self,id):
        try: 
            data=Student.objects.get(id=id)
            return data
        except Student.DoesNotExist:
            return None

    def get(self,request,id):
        std_instance=self.get_object(id) 
        if not std_instance: 
            return Response({"error":"Data not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializer(std_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        std_instance=self.get_object(id)

        if not std_instance:
            return Response({"error":"Data not found"},status=status.HTTP_404_NOT_FOUND)
        data={
            'name':request.data.get('name'),
            'roll':request.data.get('roll'),
            'city':request.data.get('city'),
        }

        serializer=StudentSerializer(instance=std_instance,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        std_instance=self.get_object(id)

        if not std_instance:
            return Response({"error":"Data not found"},status=status.HTTP_400_BAD_REQUEST)

        std_instance.delete()
        return Response({"msg":"Data Deleted"},status=status.HTTP_200_OK)

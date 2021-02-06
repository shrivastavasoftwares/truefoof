from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from stu.models import school,teacher,student,subject,class_t
from stu.serializers import schoolSerializer,subjectSerializer,class_tSerializer


# Create your views here.

class schoolViewsset(viewsets.ViewSet):

    def create(self,request):      # craete Api
        serializers=schoolSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status":200})
        else:
            return Response(serializers.errors)


    def list(self,request): # Get Api #fetch all data of teacher Api from database
        queryset=school.objects.all()
        print(queryset)
        serializers=schoolSerializer(queryset,many=True)
        print(serializers.data)
        return Response(serializers.data)



class subjectViewsset(viewsets.ViewSet):


  """  def destroy(self,request,pk=None): # delete Api
        queryset=subject.objects.get(id=pk).delete()

        return Response({"status":"ok"})"""
  def list(self,request):
      queryset=subject.objects.all()
      print(queryset)
      serializers=subjectSerializer(queryset,many=True)
      print(serializers.data)
      return Response(serializers.data)



class class_tViewsset(viewsets.ViewSet):
    pass
from django.shortcuts import render
from .serializers import *
from rest_framework import views,status
from .models import Resume
from rest_framework.response import Response
from .admin import ResumeResource
# Create your views here.


class ResumeView(views.APIView):
    def get(self,request,*args,**kwargs):
        cv = Resume.objects.get(user=request.user)
        serializer = ResumeSerializer(cv)
        dataset = ResumeResource().export()
        with open('resume.csv','wt',encoding='utf-8')as inresume:
            inresume.writelines(str(dataset.csv))
        return Response (serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ExperienceView(views.APIView):

    def get(self,request,*args,**kwargs):
        experience = Experience.objects.get(id=kwargs['resume_id'],user=request.user)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EducationView(views.APIView):

    def get(self,request,*args,**kwargs):
        education = Education.objects.get(id=kwargs['resume_id'],user=request.user)
        serializer = EducationSerializer(education)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class LanguagesView(views.APIView):

    def get(self,request,*args,**kwargs):
        languages = Languages.objects.get(id=kwargs['resume_id'],user=request.user)
        serializer = LanguagesSerializer(languages)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = LanguagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class SkillsView(views.APIView):

    def get(self,request,*args,**kwargs):
        skills = Skills.objects.get(id=kwargs['resume_id'],user=request.user)
        serializer = SkillsSerializer(skills)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = SkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class CertificationsView(views.APIView):

    def get(self,request,*args,**kwargs):
        certification = Certifications.objects.get(id=kwargs['resume_id'],user=request.user)
        serializer = CertificationsSerializer(certification)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = CertificationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
from django.urls import path
from .views import *

urlpatterns =[
    path('resume/',ResumeView.as_view(),name='create'),
    path('experience/<int:resume_id>/',ExperienceView.as_view()),
    path('education/<int:resume_id>/',EducationView.as_view()),
    path('languages/<int:resume_id>/',LanguagesView.as_view()),
    path('skills/<int:resume_id>/',SkillsView.as_view()),
    path('certifications/<int:resume_id>/',CertificationsView.as_view()),







]
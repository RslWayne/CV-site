from rest_framework import serializers
from .models import *


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Languages
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = '__all__'


class CertificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    expi = ExperienceSerializer(many=True,required=False)
    edu = EducationSerializer(many=True,required=False)
    language = LanguagesSerializer(many=True,required=False)
    skill = SkillsSerializer(many=True,required=False)
    certification = CertificationsSerializer(many=True,required=False)

    class Meta:
        model = Resume
        fields = '__all__'




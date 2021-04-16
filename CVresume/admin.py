from django.contrib import admin
from  import_export import resources
from import_export.fields import Field
from .models import Resume
# Register your models here.
from .models import *


class ResumeResource(resources.ModelResource):
    full_title = Field()

    class Meta:
        model = Resume
        # fields = ('id__full_name')


    def dehydrate_full_tittle(self,resume):
        return '%s by %s' % (resume.name,resume.author.name)







admin.site.register([Resume,Experience,Education,Languages,Skills,Certifications])
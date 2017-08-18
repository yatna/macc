from django.db import models

from profiles.models import Pcuser
from django.core.validators import RegexValidator

from django.core.files.storage import FileSystemStorage


class Contact(models.Model):
    office_name = models.CharField(max_length=200)
    contact_number = models.BigIntegerField()

    def __str__(self):
        return self.office_name
        
    class Meta:
    	verbose_name = 'Contact'
    	verbose_name_plural = 'Contacts'


class ghnPost(models.Model):
    owner = models.ForeignKey(Pcuser, null=False, related_name='xowner')
    title = models.CharField(max_length=1000, validators=[
                                        RegexValidator(
                                            r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                        )])
    description = models.TextField(max_length=3000)
    created_date = models.DateTimeField(auto_now=True)

    # link to important documents
    link = models.CharField(max_length=200, null = True)

    fs = FileSystemStorage(location='static/')

    photo = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)

    def __str__(self):
        return self.title

    #to get the url of the model in templates
    def get_absolute_url(self):
        return '/gethelpnow/view_post/%i' % self.id
    
    #to access the model name in templates
    def model_name(self):
        return 'PCSA Get Help Now'
        
    class Meta:
    	verbose_name = 'Get Help Now Post'
    	verbose_name_plural = 'Get Help Now Posts'

from django.db import models

<<<<<<< HEAD
from profiles.models import Pcuser
=======
from signup.models import Pcuser
from django.core.files.storage import FileSystemStorage
>>>>>>> Extended Info Hub posts to support Images and External Links


# Create your models here.
class Contact(models.Model):
    office_name = models.CharField(max_length=190)
    contact_number = models.BigIntegerField()

    def __str__(self):
        return self.office_name
        
    class Meta:
    	verbose_name = 'Contact'
    	verbose_name_plural = 'Contacts'


class ghnPost(models.Model):
    owner = models.ForeignKey(Pcuser, null=False, related_name='xowner')
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=3000)
    created_date = models.DateTimeField(auto_now=True)

# <<<<<<< HEAD
#     def __str__(self):
# =======
    # link to important documents
    link = models.CharField(max_length=200, null = True)

    fs = FileSystemStorage(location='infohub/static/')

    photo = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)

    def __unicode__(self):
# >>>>>>> Extended Info Hub posts to support Images and External Links
        return self.title
        
    class Meta:
    	verbose_name = 'Get Help Now Post'
    	verbose_name_plural = 'Get Help Now Posts'

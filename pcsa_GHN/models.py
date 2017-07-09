from django.db import models

from profiles.models import Pcuser


# Create your models here.
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
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=30000)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    class Meta:
    	verbose_name = 'Get Help Now Post'
    	verbose_name_plural = 'Get Help Now Posts'

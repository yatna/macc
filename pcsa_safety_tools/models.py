from django.db import models
from django.core.validators import RegexValidator


class SafetyToolsCategory(models.Model):
    category_id = models.IntegerField()
    category_name = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name
        
    class Meta:
    	verbose_name = 'Safety Tools Category'
    	verbose_name_plural = 'Safety Tools Categories'


class SafetyToolsPost(models.Model):
    category_id = models.ForeignKey(SafetyToolsCategory)
    title = models.CharField(max_length=500, validators=[
                                            RegexValidator(
                                                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                            )])
    description = models.TextField(max_length=30000)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    class Meta:
    	verbose_name = 'Safety Tools Post'
    	verbose_name_plural = 'Safety Tools Posts'

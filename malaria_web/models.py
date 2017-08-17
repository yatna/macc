from django.core.validators import RegexValidator
from django.db import models
from django.core.files.storage import FileSystemStorage

from profiles.models import Pcuser

# Model corresponding to malaria posts
class Post(models.Model):
    # The owner of the post
    owner = models.ForeignKey(Pcuser, null=False, related_name='owner')
    title_post = models.CharField(max_length=1000,
                                  validators=[
                                      RegexValidator(
                                          r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                      )]
                                  )
    description_post = models.TextField(max_length=20000)
    # link to important documents
    link_post = models.CharField(max_length=200)

    #define where the images in posts will get stored
    fs = FileSystemStorage(location='static/')
    # uploadable image in posts
    photo = models.ImageField( storage =fs ,upload_to = 'images/', default = 'images/sample.jpg',null=True)

    # field to note the timestamp when the post was created
    created = models.DateTimeField(auto_now_add=True)
    # field to note the timestamp when the post was last updated
    updated = models.DateTimeField(auto_now=True)

    # Name to be shown for a particular instance of this type of model
    def __str__(self):
        return self.owner.user.username

    def get_absolute_url(self):
        return '/malaria/view_post/%i' % self.id

    def model_name(self):
        return 'Malaria'
    
    # Name to be shown on the home page of the admin view for the collective set 
    # of model instances    
    class Meta:
    	verbose_name = 'Post'
    	verbose_name_plural = 'Posts'

# Model corresponding to Revision of Malaria Posts
class RevPost(models.Model):
    # The post which is being edited
    owner_rev_post = models.ForeignKey(Post,
                                       null=False,
                                       related_name='owner_rev_post')
    # The user who is editing the post
    owner_rev = models.ForeignKey(Pcuser, null=False, related_name='owner_rev')
    # revised title
    title_post_rev = models.CharField(max_length=1000)
    # revised description
    description_post_rev = models.TextField(max_length=20000,
                                            validators=[
                                                RegexValidator(
                                                    r'^[(A-Z)|(a-z)|(0-9)|(\n)|(\s)|(\.)|(,)|(\-)|(_)|(!)|(:)|(%)]+$'
                                                )]
                                            )


    # field to note the timestamp when the revised version was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner_rev.user.username
        
    class Meta:
    	verbose_name = 'Reviewed Post'
    	verbose_name_plural = 'Reviewed Posts'

# Model corresponding to Malaria App (Mobile) User
class MalariaUsers(models.Model):
    # Name of the user
    name = models.CharField(max_length=200)
    # email of the user
    email = models.EmailField(max_length=254)
    # age of the user
    age = models.IntegerField()
    # gender of the user
    gender = models.CharField(max_length=20, default='Not Specified')
    #The meicine he/she is taking eg Mefloquine, Malarone etc
    medicineType = models.CharField(max_length=100)

    # Name to be shown for a particular instance of this type of model
    def __str__(self):
        return self.name

    # Name to be shown on the home page of the admin view for the collective set 
    # of model instances
    class Meta:
        verbose_name = 'Malaria App Users'

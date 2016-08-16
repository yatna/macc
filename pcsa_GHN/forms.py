from django.forms import ModelForm
from pcsa_GHN.models import Post, Contact


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['office_name', 'contact_number']

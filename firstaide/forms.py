from django.forms import ModelForm
from firstaide.models import *

class FirstAideAPIForm(ModelForm):
	class Meta:
		model = FirstAideAPI
		fields = ['post_id','page_type','title','content']


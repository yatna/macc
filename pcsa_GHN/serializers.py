from .models import *
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'created_date')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('office_name', 'contact_number')

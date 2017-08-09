from rest_framework import serializers

from .models import *


class firstAideAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAideAPI
        fields = ('card_content',)

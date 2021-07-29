from django.db import models
from rest_framework import serializers

class Image(models.Model):
    img = models.ImageField(upload_to='images')
    
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
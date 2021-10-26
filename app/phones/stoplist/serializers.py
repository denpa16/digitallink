from rest_framework import serializers
from .models import Phone, File

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone_number',)

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = '__all__'
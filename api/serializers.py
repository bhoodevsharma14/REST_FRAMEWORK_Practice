from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student     #name of our model
        fields = ['name','roll','city']   #List of fields we want to see in the response
        # fields = '__all__'
        
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student     #name of our model
        fields = ['name','roll','city']   #List of fields we want to see in the response
        read_only_fields = ['name','roll']
        # fields = '__all__'
        
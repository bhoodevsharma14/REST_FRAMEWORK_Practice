from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create (self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    #Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('SEAT FULL !!')
        return value

    #Object Level Validation used when More thant one field have to be Validated
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'balram' and ct.lower() != 'barujna':
            raise serializers.ValidationError('City must be Barujna')
        return data
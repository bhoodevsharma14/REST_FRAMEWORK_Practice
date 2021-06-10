from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#Model Object - Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)         #Calling Data from Student Model
    serializer = StudentSerializer(stu)     #Converting to Serialied data
    # these two lines to single line
    # json_data = JSONRenderer().render(serializer.data)  #Converting serialized data into JSON data
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)


#All Student Data    
def student_list(request):
    stu = Student.objects.all()         #Calling Data from Student Model
    serializer = StudentSerializer(stu,many=True)     #Converting to Serialied data
    # These two lines to single line
    # json_data = JSONRenderer().render(serializer.data)  #Converting serialized data into JSON data
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False) #for multiple data safe= False defaut safe=True

#To Create Student
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer =StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application//json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from api.models import Student

def grade_average(grades):
    result=[]
    result1=[]
    for item1 in grades:
        count=0
        for item2 in result:
            if item1["code"]==item2["code"]:
                count+=1                
                item2["value"]+=item1["value"]
                item2["count"]+=1
        if count==0:                    
            result.append({"code":item1["code"],"value":item1["value"],"count":1})           
    for item in result:
        result1.append({"code":item["code"],"value":item["value"]/item["count"]})       
    return result1
 
def api_home(request: HttpRequest, *args, **kwargs):
    pk=0
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            nGrades=grade_average(body["grades"])
            student=Student(name=body["name"],surname=body["surname"],stdNumber=body["stdNumber"],grades=nGrades)
            student.save()
            pk=student.pk

        
        # print(Student.objects.filter(pk=pk).values())
        # print(model_to_dict(Student.objects.filter(pk=pk)))

        return JsonResponse({'message':list(Student.objects.filter(pk=pk).values())})
    except:
        return HttpResponse(content="""Here is a sample request: {
            "name": "Ali",
            "surname": "Yilmaz",
            "stdNumber": "B012X00012",
            "grades": [
                            
            {
            "code": "MT101",
            "value": 90
            }, {
            "code": "PH101",
            "value": 75
            }, {
            "code": "CH101",
            "value": 60
            }, {
            "code": "MT101",
            "value": 70
            }, {
            "code": "HS101",
            "value": 65
            }
            ]}""",status=409)
    
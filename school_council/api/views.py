import json
from django.http import JsonResponse
from api.models import Student
from django.views import View
from cerberus import Validator

class StudentView(View):
    sample_post_request = {
        "name": "John",
        "surname": "Doe",
        "stdNumber": "B012X00012",
        "grades": [
            {
                "code": "MT101",
                "value": 90
            },
            {
                "code": "MT101",
                "value": 75
            },
            {
                "code": "CH101",
                "value": 60
            },
            {
                "code": "MT101",
                "value": 70
            },
            {
                "code": "HS101",
                "value": 65
            }
        ]
    }
    
    post_schema = {
        "name": {
            "required": True,
            "type": "string"
        },
        "surname": {
            "required": True,
            "type": "string"
        },
        "stdNumber": {
            "required": True,
            "type": "string"
        },
        "grades": {
            "required": True,
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "code": {"type": "string"},
                    "value": {"type": "integer"}
                }
            }
        }
    }

    def options(self, request, *args, **kwargs):
        return JsonResponse(self.post_schema)

    def post(self, request, *args, **kwargs):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            v = Validator(schema=self.post_schema)
            if not v.validate(body):
                return JsonResponse(v.errors, safe=False, status=400)
            student = Student(**body)
            student.grades = student.calculate_grades()
            student.save()
            data = list(Student.objects.filter(pk=student.pk).values())[0]
            return JsonResponse({'data': data})
        except Exception as e:
            print(e)
            return JsonResponse({
                "error": str(e),
                "sample_request": self.sample_post_request
            }, status=400)

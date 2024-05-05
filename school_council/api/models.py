from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    surname=models.CharField(max_length=100,null=False,blank=False)
    stdNumber=models.CharField(max_length=20,null=False,blank=False,unique=True)
    grades=models.JSONField()

    class Meta:
        db_table = "students"
 
    def calculate_grades(self):
        total_grades = {}
        for grade in self.grades:
            if grade["code"] not in total_grades:
                total_grades[grade["code"]] = {"total": 0, "count": 0}
            total_grades[grade["code"]]["total"] += grade["value"]
            total_grades[grade["code"]]["count"] += 1
        return list(map(lambda item: {
                "code": item,
                "value": total_grades[item]["total"] / total_grades[item]["count"]
            },
            total_grades.keys()
        ))
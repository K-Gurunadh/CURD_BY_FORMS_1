from django.db import models
class EmpployeeData(models.Model):
        emp_id = models.IntegerField(unique=True)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        mobile = models.BigIntegerField()
        salary = models.IntegerField()
        location = models.CharField(max_length=100)
        company = models.CharField(max_length=100)

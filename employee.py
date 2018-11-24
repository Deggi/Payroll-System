from peewee import *

try:
    db = PostgresqlDatabase ('payrollSystem', user='postgres', host='localhost',password='chiyo')
    print("successful")
except:
    print("error")

class Employee(Model):
    full_name=CharField("100")
    kra_pin_number=CharField()
    department=CharField()
    position=CharField()
    basic_salary=FloatField()
    house_allowance=FloatField()

# class Payroll(Model):
#     id=IntegerField()
#     payroll_date=DateField()
#     overtime=FloatField()
#     other_benefits=FloatField()
#     nhif=FloatField()
#     nssf=FloatField()
#     payee=FloatField()
#     employee_id=ForeignKeyField()

    class Meta:
        database = db
        table_name="employees2"

Employee.create_table(fail_silently=True)

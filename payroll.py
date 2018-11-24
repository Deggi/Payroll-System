from peewee import *
from employee import Employee,db

class Payroll(Model):
    payroll_date=DateField()
    overtime=FloatField()
    other_benefits=FloatField()
    nhif=FloatField()
    nssf=FloatField()
    payee=FloatField()
    employee_id=ForeignKeyField(Employee,backref='id',on_update="cascade")

    class Meta:
        database = db
        table_name="payroll"

Payroll.create_table(fail_silently=True)

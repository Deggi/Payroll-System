from employee import Employee
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    Employee.create(full_name="Edwin Goldwin",kra_pin_number="100001",department="Marketing",position="Analyst",basic_salary=100000,house_allowance=2000)
    allEmployees= Employee.select()
    return render_template("index.html",displayEmployees=allEmployees)

if __name__=="__main__":
    app.run(debug=True,port=5005)
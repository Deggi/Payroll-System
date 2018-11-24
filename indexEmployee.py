from employee import Employee
from user import User
from flask import Flask,render_template,request,redirect,url_for,flash,session
from cryptography.fernet import Fernet

app=Flask(__name__)
app.secret_key="78hhmahu"
key=b'6IvzllrLA1gHEBvfAmRllLf9eViK88YU_G2LuyAzWaE='
cipher_suite = Fernet(key)

def logged_in():
    if session:
        return True
    return False

@app.route("/auth")
def authentification():
    if logged_in():
        return redirect(url_for("home"))
    return render_template("register_login.html")

@app.route("/register",methods=["post"])
def register():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    confirm=request.form["confirm-password"]
    if password!=confirm:
        flash("Passwords Do Not Match")
        return redirect(url_for("authentification"))

    check=User.select().where(User.email==email).count()
    if check!=0:
        flash("Email already exists")
        return redirect(url_for("authentification"))

    encpass=cipher_suite.encrypt(bytes(password,"utf-8"))

    User.create(name=name,email=email,password=encpass)
    session["email"]=email

    return redirect(url_for("home"))

@app.route("/login",methods=["POST"])
def login():
    email=request.form["email"]
    password=request.form["password"]
    encpass = cipher_suite.encrypt(bytes(password, "utf-8"))

    #check if email and password match
    check = User.select().where(User.email == email).count()
    if check==0:
        flash("Wrong Credentials")
        return redirect(url_for("authentification"))
    else:
        user=User.select().where(User.email==email).get()
        passwordFromDb=cipher_suite.decrypt(bytes(user.password, "utf-8")).decode("utf-8")
        if password==passwordFromDb:
            session["email"]=email
            flash("Successully Logged in")
            return redirect(url_for("home"))
        else:
            flash("Wrong Credentials")
            return redirect(url_for("authentification"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("authentification"))

@app.route("/")
def home():
    if logged_in():
        allEmployees = Employee.select()
        return render_template("index.html",displayEmployees=allEmployees)
    return redirect(url_for("authentification"))

@app.route("/employee")
def employee():
    return render_template("add_employee.html")

@app.route("/saveEmployee",methods=["POST"])
def employee_save():
    name=request.form["form_full_name"]
    kra_pin=request.form["form_kra_pin_number"]
    department=request.form["form_department"]
    position=request.form["form_position"]
    basic=request.form["form_basic_salary"]
    house=request.form["form_house_allowance"]

    Employee.create(full_name=name,
                    kra_pin_number=kra_pin,
                    department=department,
                    position=position,
                    basic_salary=basic,
                    house_allowance=house)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True,port=5001)
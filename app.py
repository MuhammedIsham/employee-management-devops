from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy 
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://employee_user:password123@localhost/employee_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/add', methods=['POST'])
def add_employee_ui():
    name = request.form['name']
    new_employee = Employee(name=name)
    db.session.add(new_employee)
    db.session.commit()
    return redirect('/')


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([
    {
         "id": emp.id,
         "name": emp.name
   	 }
    for emp in employees
    ])


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):

    employee = Employee.query.get(id)
    if employee:
          return jsonify({
            "id": employee.id,
            "name": employee.name
        })

    return jsonify({"error": "Employee not found"}), 404


@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json

    new_employee = Employee(name=data["name"])

    db.session.add(new_employee)
    db.session.commit()

    return jsonify({
    "id": new_employee.id,
    "name": new_employee.name
    }), 201


@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):

    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": "Employee deleted"})

    return jsonify({"error": "Employee not found"}), 404



@app.route('/search', methods=['POST'])
def search_employee():
    emp_id = int(request.form['id'])
    employees = Employee.query.all()
    employee = Employee.query.get(emp_id)
    if employee:
        return render_template(
            'index.html',
             employees=employees,
             result=employee
            )

    return render_template(
        'index.html',
        employees=employees,
        error="Employee not found"
    )


@app.route('/delete', methods=['POST'])
def delete_employee_ui():
    global employees

    emp_id = int(request.form['id'])

    employee = Employee.query.get(emp_id)

    if employee:
        db.session.delete(employee)
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,
debug=False)

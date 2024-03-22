from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('database.json', 'r') as file:
    employee_data = json.load(file)

@app.get('/birthdays')
def birthdays():
    month = request.args.get('month')
    department = request.args.get('department')

    filtered_employees = [emp for emp in employee_data if emp['Department'] == department and emp['Birthday'][5:7] == month]

    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }

    return jsonify(response)

@app.get('/anniversaries')
def anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')

    filtered_employees = [emp for emp in employee_data if emp['Department'] == department and emp['Hiring Date'][5:7] == month]

    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
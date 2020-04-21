from gift_planner import app, db, model
import json
import os

with open('employees.json', 'r') as f:
    employees = json.load(f)

with open('gifts.json', 'r') as f:
    gifts = json.load(f)


def init_db():
    """
    Populate database with given json files
    :return:
    """

    # Loop over gifts json and create an entry in Gift table for each gift name
    # and an entry in Category table with category name and link it to Gift
    for gift in gifts:
        for category in gift['categories']:
            db.session.add(model.Category(name=category, gift_name=gift['name']))

        if not model.Gift.query.filter_by(name=gift['name']).first():
            db.session.add(model.Gift(name=gift['name']))

    # Loop over employees json and create an entry in Category table if interest
    # match category with employee name. Also, create an entry for all employees.
    for employee in employees:
        for interest in employee['interests']:
            categories = model.Category.query.filter_by(name=interest).all()
            for category in categories:
                if category:
                    if not category.employee_name:
                        category.employee_name = employee['name']
                    else:
                        db.session.add(model.Category(name=category.name, gift_name=category.gift_name, employee_name=employee['name']))

        if not model.Employee.query.filter_by(name=employee['name']).first():
            db.session.add(model.Employee(name=employee['name']))

    db.session.commit()


@app.route('/gifts/<name>', methods=['POST'])
def assign_gift(name):
    """
    Assigns gift to employee with given name
    :param name: Employee name
    :return: name of gift
    """

    # Check if employee with that name exists before proceeding
    employee = model.Employee.query.filter_by(name=name).first()
    if not employee:
        return 'Employee name does not exist', 404

    # Check if gift was not previously assigned to that employee
    if model.Gift.query.filter_by(employee_name=employee.name).first():
        return 'Employee has already received a gift', 403

    # Loop over interests of employee and return gift matching the same category
    for interest in employee.interests:
        gift = model.Gift.query.filter_by(name=interest.gift_name).first()

        # Only assign that gift to that employee name if not assigned before
        if not gift.employee_name:
            gift.employee_name = name
            db.session.commit()
            return gift.name, 200

    return "Sorry, all gifts with your interests have been assigned", 404

from gift_planner import db


class Category(db.Model):
    """
    Table representing categories of gifts and interests of employees
    """
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gift_name = db.Column(db.String(50), db.ForeignKey('gift.name'))
    employee_name = db.Column(db.String(20), db.ForeignKey('employee.name'))


class Gift(db.Model):
    """
    Table representing assigned gifts with relationship to Category table
    """
    __tablename__ = 'gift'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    employee_name = db.Column(db.String(20), db.ForeignKey('employee.name'))

    categories = db.relationship('Category', backref=db.backref('gift', lazy=True))


class Employee(db.Model):
    """
    Table that hold information with regard to employees with relationship to Category and Gift tables
    """
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    interests = db.relationship('Category', backref=db.backref('employee'), lazy=True)
    gifts = db.relationship('Gift', backref=db.backref('employee', lazy=True))


db.create_all()

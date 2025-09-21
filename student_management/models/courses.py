from odoo import api, fields, models
class Courses(models.Model):
    _name = 'student.management.courses' 
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Course Code")
    credit = fields.Integer(string="Credit")
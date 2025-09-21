from odoo import api, fields, models
class Studnents(models.Model):
    _name = 'student.management.students'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    roll_no = fields.Char(string="Roll Number", required=True)
    department = fields.Char(string="Department", required=True)
    course_ids = fields.Many2many('student.management.courses', string="Courses")


    def action_show_enrolled_courses(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Enrolled Courses',
            'res_model': 'student.management.courses',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.course_ids.ids)],
            'target': 'current',
        }

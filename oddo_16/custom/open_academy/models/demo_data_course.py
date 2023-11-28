from odoo import models, fields

class DemoDataCourse(models.Model):
    _name = 'demo.data.course'
    _description = 'Demo Data Academy Course'
    _rec_name = 'academy_course'

    academy_course = fields.Char(string='Academy Course',help='This is only demo data')
    course_description = fields.Text(string='Course Description',help='description of course')
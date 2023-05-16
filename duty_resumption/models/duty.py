from  datetime import date
from odoo import api, fields, models


class EmployeeDetails(models.Model):
    _name = "employee.details" 
    _description = "Employee Details"


    name_id = fields.Many2one('hr.employee',string='Name of Employee')
    date=fields.Date(string='Reporting Date')
    reason=fields.Char(string='Reason for early/late')

    state = fields.Selection([
        ('submit','Submit'),
        ('verify','Verify'),
        ('cancel','Cancel')
        ], default='submit',string='Status', required=True)

    
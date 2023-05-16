from  datetime import date
from odoo import api, fields, models


class ClinicPatient(models.Model):
    _name = "clinic.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Clinic patient"

    patient_id = fields.Many2one('clinic.patient', string='Patient')
    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')

    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age',compute='_compute_age',tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender',tracking=True)
    image = fields.Image(string='Image')
    

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=1    



    patient_count = fields.Integer(string='Appointment', compute='_compute_visitor_count')
  

    # @api.depends('internal_group')
    def _compute_visitor_count(self): 
        # for rec in self:
            patient_count = self.env['clinic.appointment'].search_count([('patient_id','=', self.id)])
            self.patient_count = patient_count
            print('self')


    def action_clinic_appointment(self):
        return {
            'name': 'History',
            'type': 'ir.actions.act_window',
            'res_model': 'clinic.appointment',
            'domain' : [('patient_id','=',self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }



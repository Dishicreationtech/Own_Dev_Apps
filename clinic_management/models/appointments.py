
from odoo import api, fields, models
from  datetime import date

class ClinicAppointment(models.Model):
    _name = "clinic.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Clinic appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('clinic.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time',default=fields.Datetime.now,tracking=True)
    booking_date = fields.Date(string='Booking Date',default=fields.Date.context_today,tracking=True)
    
    ref = fields.Char(string='Reference', help= "Reference from patient record")
    prescription = fields.Html(string='Prescription')
    
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancelled','Cancelled')], default='draft',string='Status', required=True)
    
    doctor_id = fields.Many2one('res.users', string='Doctor',tracking=True)
    age = fields.Integer(string='Age',tracking=True)
    pharmacy_line_ids = fields.One2many('appointments.pharmacy.lines','view_appointment_id',string='Pharmacy Lines')
   
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        appointment = self

        appointment.ref = appointment.patient_id.ref
        # print("---------ref--",ref)
        date_of_birth = appointment.patient_id.date_of_birth
        today = date.today()
        if date_of_birth:
            appointment.age = today.year - date_of_birth.year
        else:
            appointment.age = 1
    

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancelled(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'    


class AppointmentsPharmacyLines(models.Model):
    _name = "appointments.pharmacy.lines"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Appointments Pharmacy Lines"

    medicine_id = fields.Many2one('product.product',required=True)
    price_unit = fields.Float(related='medicine_id.lst_price')
    qty = fields.Integer(string='Quantity',default=1)
    view_appointment_id = fields.Many2one('clinic.appointment','ClinicAppointment')

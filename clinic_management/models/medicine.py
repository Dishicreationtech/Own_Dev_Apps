from  datetime import date
from odoo import api, fields, models


class PatientMedicine(models.Model):
    _name = "patient.medicine"
    _description = "Patient Medicine"


    patient_name_id = fields.Many2one('clinic.patient', string='Patient')
    medicine = fields.Char(string='Medicine Name')
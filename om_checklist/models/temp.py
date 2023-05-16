from  datetime import date
from odoo import api, fields, models


class ChecklistTemplate(models.Model):
    _name = "checklist.template" 
    _description = "Checklist Template"


    name=fields.Char(string='Name')
    req= fields.Html(string='Requirement')    
    risk=fields.Html(string='Risk')
    remark=fields.Html(string='Remark')
    

    requirement_line_ids = fields.One2many('requirement.template','remark_id',string='Pharmacy Lines')

class RequirementTemplate(models.Model):
    _name = "requirement.template" 
    _description = "Requirement Template"

    req_id = fields.Many2one('checklist.template', string='Requirement')
    risk_id = fields.Many2one('checklist.template', string='Risk')
    remark_id = fields.Many2one('checklist.template', string='Remark')



class ChecklistConfiguration(models.Model):
    _name = "checklist.configuration" 
    _description = "Checklist Configuration"
    
    date=fields.Date(string='Date')
    created_id= fields.Many2one('res.users', string='Created By')
    approved_id= fields.Many2one('res.users',string='ApprovedBy')
    attachment=fields.Binary(string='Attachment')
    # select_template_id = fields.Many2one('requirement.template',string='Select Template')

    requirement_line_ids = fields.One2many('requirement.template','remark_id',string='Pharmacy Lines')
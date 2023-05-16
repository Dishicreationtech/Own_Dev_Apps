from  datetime import date
from odoo import api, fields, models


class CustomerDetails(models.Model):
    _name = "customer.details"
    _description = "Customer Details"
    _rec_name ="name_id"  

    name_id = fields.Many2one('res.partner',string='Name')
    date = fields.Date(string='Date of Visit')
    image = fields.Image(string='Image')
    meet = fields.Char(string='Whom to meet')
    purpose = fields.Char(string='Purpose To visit')
    email = fields.Char(string='Email')
    phone_no = fields.Integer(string='Mobile No')
    address = fields.Char(string='Company Name And Address')
   
    state = fields.Selection([
            ('draft','Draft'),
            ('verify','Verify'),
            ('cancel','Cancel')
            ], default='draft',string='Status', required=True)

    def action_allow(self):
        for rec in self:
            rec.state = 'verify'

    def action_notallow(self):
        for rec in self:
            rec.state = 'cancel'

class CustomerDetailsNew(models.Model):
    
    _inherit = "res.partner"
    
   
    name_ids = fields.One2many('customer.details','name_id',string='Name')   


    visitors_count = fields.Integer(string='No of visits',compute='_compute_visitor_count')
  

    # @api.depends('internal_group')
    def _compute_visitor_count(self): 
        # for rec in self:
            visitors_count = self.env['customer.details'].search_count([('name_id','=', self.id)])
            self.visitors_count = visitors_count



    # def action_open_visitor(self):
    #     return {
    #         'name':'Visit',
    #         'type':'ir.actions.act_window',
    #         'res_model':'customer.details',
    #         'domain' : [('name_id','=',self.name_ids.ids)],
    #         'view_mode': 'form,tree',
    #         'target': 'current',
    #     }



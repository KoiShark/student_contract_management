from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    power_bi_url = fields.Char(string="Power BI URL")

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    power_bi_url = fields.Char(related="company_id.power_bi_url", readonly=False)

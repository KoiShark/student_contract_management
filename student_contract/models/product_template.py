from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_subject = fields.Boolean(
        string="subject",
        default=False,
    )

    @api.onchange("is_subject")
    def _onchange_is_subject(self):
        for product in self:
            product.type = "service" if product.is_subject else product.type

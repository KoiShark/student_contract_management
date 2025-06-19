from odoo import fields, models


class TermSubject(models.Model):
    _name = "term.subject"
    _description = "Allows to manage subjects"

    name = fields.Char(
        string="Subject",
        related="product_id.name",
    )

    product_id = fields.Many2one(
        "product.product",
        string="Product",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

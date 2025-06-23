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
    subject_amount = fields.Float(related="product_id.list_price", readonly=False)
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
        string="Company",
    )
    company_currency_id = fields.Many2one(
        string="Company Currency",
        related="company_id.currency_id",
        readonly=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

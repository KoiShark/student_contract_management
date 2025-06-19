from odoo import _, fields, models


class StudentContract(models.Model):
    _name = "student.contract"
    _description = "Manage student contracts and relation with student subjects"

    name = fields.Char(string="Contract")
    active = fields.Boolean(
        string="Active",
        default=True,
    )

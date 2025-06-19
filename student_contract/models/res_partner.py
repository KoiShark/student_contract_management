from odoo import _, fields, models


CONTACT_SELECTION = [("student", "Student"), ("teacher", "Teacher")]


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_institute_contact = fields.Boolean(
        string="Institute Contact",
        default=False,
    )

    contact_type = fields.Selection(
        CONTACT_SELECTION,
        string="Contact Type",
        default="student",
    )

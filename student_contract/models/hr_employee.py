from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_teacher = fields.Boolean(
        string="Is teacher?",
        default=False,
    )

    course_line_ids = fields.One2many(
        "course.line",
        "teacher_id",
        string="Course Lines",
    )

    # subject_ids = fields.Many2many(
    #     "term.subject",
    #     "hr_employee_term_subject_rel",
    #     string="Subjects",
    # )

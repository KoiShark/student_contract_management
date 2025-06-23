from odoo import api, fields, models


class StudentSubjectLine(models.Model):
    _name = "student.subject.line"
    _description = "Lines representing student's subject history"

    name = fields.Char(related="subject_id.name")
    student_id = fields.Many2one("res.partner", string="Student")
    domain_subject_ids = fields.Many2many(
        "term.subject",
        compute="_compute_domain_subject_ids",
        string="Subjects domain",
    )
    subject_id = fields.Many2one("term.subject", string="Subject")
    course_id = fields.Many2one("course.table", string="Course")
    status = fields.Selection(
        [
            ("on_hold", "On hold"),
            ("coursing", "Coursing"),
            ("approved", "Approved"),
            ("failed", "Failed"),
            ("rejected", "Rejected"),
        ],
        string="Status",
        default="on_hold",
    )

    @api.depends("course_id")
    def _compute_domain_subject_ids(self):
        """
        Method to get subjects per course
        """
        for rec in self:
            rec.domain_subject_ids = rec.course_id and rec.course_id.subject_ids or []

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
    contract_id = fields.Many2one("student.contract", string="Contract")
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
            if not rec.course_id:
                rec.domain_subject_ids = []
                continue

            # Get subjects linked to the course
            course_subjects = rec.course_id.subject_ids
            if not course_subjects:
                rec.domain_subject_ids = []
                continue

            # Find teachers assigned to ANY course (not necessarily this one)
            assigned_teachers = rec.env["hr.employee"].search([
                ("is_teacher", "=", True),
                ("course_line_ids.course_id", "=", rec.course_id.id),
            ]).course_line_ids

            # Get subjects taught by these teachers AND available in the course
            rec.domain_subject_ids = course_subjects & assigned_teachers.mapped("subject_ids")

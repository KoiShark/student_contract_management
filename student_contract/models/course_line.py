from odoo import api, fields, models


class CourseLine(models.Model):
    _name = "course.line"
    _description = "Course Lines"

    name = fields.Char(related="course_id.name")
    course_id = fields.Many2one(
        "course.table",
        string="Course",
    )
    domain_subject_ids = fields.Many2many(
        "term.subject",
        compute="_compute_domain_subject_ids",
        string="Subject Domain",
    )
    subject_ids = fields.Many2many(
        "term.subject",
        "course_line_term_subject_rel",
        string="Subjects",
    )
    teacher_id = fields.Many2one(
        "hr.employee",
        string="Teacher",
    )

    @api.depends("course_id")
    def _compute_domain_subject_ids(self):
        for rec in self:
            rec.domain_subject_ids = rec.course_id and rec.course_id.subject_ids or []

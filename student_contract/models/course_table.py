from odoo import fields, models


class CourseTable(models.Model):
    _name = "course.table"
    _description = "Course table: semester, trimester, etc"

    name = fields.Char(string="Course")
    subject_ids = fields.Many2many(
        "term.subject",
        "course_table_term_subject_rel",
        string="Subjects"
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

from odoo import api, Command, fields, models


class ContractLine(models.Model):
    _name = "contract.line"
    _description = "Contract lines"

    name = fields.Char(related="student_subject_line_id.name")
    student_subject_line_id = fields.Many2one(
        "student.subject.line",
        string="Subject",
        # domain="[('student_id', '=', contract_id.student_id.id)]",
    )
    domain_teacher_ids = fields.Many2many(
        "hr.employee",
        compute="_compute_domain_teacher_ids",
        string="Teacher domain",
    )
    company_currency_id = fields.Many2one(
        string="Company Currency",
        related="contract_id.company_currency_id",
        readonly=True,
        store=True,
        precompute=True,
    )
    amount = fields.Monetary(
        string="Amount",
        compute="_compute_amount",
        precompute=True,
        readonly=False,
        currency_field="company_currency_id",
        store=True,
    )
    contract_id = fields.Many2one(
        "student.contract",
        string="Contract",
    )
    student_id = fields.Many2one(related="contract_id.student_id")
    teacher_id = fields.Many2one(
        "hr.employee",
        string="Teacher",
    )

    @api.depends("student_subject_line_id")
    def _compute_domain_teacher_ids(self):
        """
        Method to get teachers per subject
        """
        for rec in self:
            if not rec.student_subject_line_id:
                rec.domain_teacher_ids = False
                continue

            subject_id = rec.student_subject_line_id.subject_id
            course_id = rec.student_subject_line_id.course_id

            teacher_ids = rec.env["hr.employee"].search(
                [
                    ("is_teacher", "=", True),
                    ("course_line_ids.course_id", "=", course_id.id),
                    ("course_line_ids.subject_ids", "=", subject_id.id),
                ]
            )

            rec.domain_teacher_ids = [Command.set(teacher_ids.ids)]

    @api.depends("student_subject_line_id")
    def _compute_amount(self):
        """
        Method to handle amount assignment or computation if needed
        """
        for rec in self:
            if not rec.student_subject_line_id:
                rec.amount = False
                continue

            rec.amount = rec.student_subject_line_id.subject_id.product_id.list_price

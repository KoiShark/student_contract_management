from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StudentContract(models.Model):
    _name = "student.contract"
    _description = "Manage student contracts and relation with student subjects"

    name = fields.Char(
        string="Contract",
        compute="_compute_name",
        store=True,
        default="New",
    )
    student_id = fields.Many2one(
        "res.partner",
        string="Student",
    )
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("paid", "Paid"),
            ("cancelled", "Cancelled"),
        ],
        copy=False,
        default="draft",
        string="Status",
    )
    payment_status = fields.Selection(
        [
            ("not_paid", "Not Paid"),
            ("in_payment", "In Payment"),
            ("paid", "Paid"),
        ],
        string="Payment Status",
        compute="_compute_payment_status",
        store=True,
        readonly=True,
        copy=False,
    )
    date = fields.Date(string="Date")
    date_due = fields.Date(string="Due Date")
    contract_line_ids = fields.One2many(
        "contract.line",
        "contract_id",
        string="Contract lines",
    )
    total_amount = fields.Float(
        string="Total",
        compute="_compute_total_amount",
        store=True,
    )
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

    # Taking into account just one invoice per contract
    move_id = fields.Many2one(
        "account.move",
        string="Invoice",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    @api.depends("status")
    def _compute_name(self):
        """
        Method to assign sequence to student contract
        """
        Sequence = self.env["ir.sequence"]
        for rec in self:
            if rec.status == "confirmed" and rec.name == "New":
                rec.name = Sequence.next_by_code("student_contract")

    @api.depends("contract_line_ids")
    def _compute_total_amount(self):
        """
        Method to compute total amount
        """
        for rec in self:
            rec.total_amount = sum(
                rec.contract_line_ids and rec.contract_line_ids.mapped("amount") or []
            )

    @api.depends("move_id", "move_id.payment_state")
    def _compute_payment_status(self):
        """
        Method to automate contract payment status
        """
        for rec in self:
            if not rec.move_id:
                rec.payment_status = "not_paid"
                continue
            payment_status = (
                "not_paid"
                if rec.move_id.payment_state not in ["paid", "in_payment"]
                else rec.move_id.payment_state
            )

            # Update status for subjects assigned to the student
            if payment_status != "not_paid":
                rec.contract_line_ids.update({"status": "coursing"})

            rec.payment_status = payment_status

    @api.constrains("date_due", "date")
    def _check_dates(self):
        """
        Validate that dates are in a proper range
        """
        for rec in self:
            if rec.date_due < rec.date:
                raise ValidationError(_("Due date value can't be lower than Date"))

    def _prepare_invoice(self):
        """
        Prepare the dict of values to create a new invoice.
        """
        partner_id = self.student_id

        values = {
            "move_type": "out_invoice",
            "invoice_date": fields.Date.today(),
            "currency_id": self.company_id.currency_id.id,
            "partner_id": partner_id.id,
            "company_id": self.company_id.id,
            "invoice_line_ids": [],
        }
        return values

    def _prepare_invoice_line_ids(self, contract_lines):
        """
        Prepare the dict of values to create a new invoice.
        """
        subject_ids = [
            (line.student_subject_line_id.subject_id.product_id, line.amount)
            for line in contract_lines
        ]

        invoice_line_vals = [
            (
                0,
                0,
                {
                    "product_id": subject.id,
                    "name": subject.name,
                    "price_unit": amount,
                    # "account_id": subject.property_account_income_id.id
                    # or subject.categ_id.property_account_income_categ_id.id,
                },
            )
            for subject, amount in subject_ids
        ]
        return invoice_line_vals

    def action_validate_contract(self):
        """
        Action that confirms the contract and creates an invoice
        """
        self.ensure_one()
        if self.status != "draft":
            return

        invoice_vals = self._prepare_invoice()
        invoice_line_vals = self._prepare_invoice_line_ids(self.contract_line_ids)

        invoice_vals.update(
            {
                "invoice_line_ids": invoice_line_vals,
            }
        )
        move_id = self.env["account.move"].create(invoice_vals)
        self.status = "confirmed"
        self.move_id = move_id

        # Asociate a contract to the student's subject
        subject_line_ids = self.contract_line_ids.mapped("student_subject_line_id")
        subject_line_ids.write({"contract_id", "=", self.id})
        return move_id

    def action_cancel_contract(self):
        """
        Method to cancel contracts
        """
        self.ensure_one()
        self.status = "cancelled"

    def open_invoices(self):
        """
        Open invoice related to the contract
        """
        self.ensure_one()
        return self.move_id.with_context(create=False)._get_records_action(
            name=_("Invoice"),
        )

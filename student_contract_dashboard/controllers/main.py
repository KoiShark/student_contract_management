from odoo import http
from odoo.http import request
import werkzeug


class DashboardController(http.Controller):

    @http.route("/student_contract_dashboard", type="http", auth="user")
    def show_dashboard(self, **kwargs):
        dashboard_url = request.env.company.power_bi_url

        if not dashboard_url:
            raise werkzeug.exceptions.NotFound()

        # Check for right access
        user_groups = request.env.user.groups_id
        dashboard_group = request.env.ref(
            "student_contract_dashboard.group_student_contract_dashboard"
        )
        if not (user_groups & dashboard_group):
            raise werkzeug.exceptions.Forbidden()

        # Render template with iframe
        return request.render(
            "student_contract_dashboard.dashboard_bi_template", {"dashboard_url": dashboard_url}
        )

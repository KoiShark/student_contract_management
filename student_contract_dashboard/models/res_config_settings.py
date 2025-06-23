from odoo import fields, models

DEFAULT_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2UyZDUzZTUtMTZmMi00YjMwLWFlZTEtZTk2NzQ1NjJhZ[%E2%80%A6]6IjBiMTgwYjAyLTIzMTUtNDBjMS05ZWIxLTY0MDk4N2FmNDRkYyIsImMiOjl9"


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    power_bi_url = fields.Char(related="company_id.power_bi_url", readonly=False, default=DEFAULT_URL)

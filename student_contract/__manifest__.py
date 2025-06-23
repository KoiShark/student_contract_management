{
    "name": "Student Contract",
    "version": "18.0.0.0.1",
    "summary": "Student Contract Management",
    "category": "Human Resources/Contracts",
    "author": "Joel Rivas <joelrivas39@gmail.com>",
    "contributors": [
        "Joel Rivas <joelrivas39@gmail.com>",
    ],
    "maintainer": [
        "Joel Rivas <joelrivas39@gmail.com>",
    ],
    "website": "",
    "depends": [
        "hr",
        "account",
        "product",
    ],
    "data": [
        "security/student_contract_security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/student_contract_menu_views.xml",
        "views/course_table_views.xml",
        "views/term_subject_views.xml",
        "views/course_line_views.xml",
        "views/contract_line_views.xml",
        "views/student_subject_line_views.xml",
        "views/res_partner_views.xml",
        "views/hr_employee_views.xml",
        "views/product_template_views.xml",
        "views/student_contract_views.xml",
    ],
    # "assets": {
    #     "web.assets_frontend": [
    #         "l10n_ve_dpt_website_sale/static/src/**/*",
    #     ],
    # },
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}

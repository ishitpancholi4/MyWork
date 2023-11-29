# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Open Academy',
    'category': '',
    'version': '16.0',
    'summary': """ Managments are made up here Open Academy""",
    'description': """ Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
            """,
    'depends': ['base','board'],

    'data': [
        'security/ir.model.access.csv',
        'data/demo_data_course.xml',
        'views/academy_course_view.xml',
        'views/res_partner_view.xml',
        'views/session_board.xml',
        'reports/openacademy_report.xml',

    ],
    'images': ['static/description/open_academy.png'],

    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
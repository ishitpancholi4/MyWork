# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Open Academy',
    'category': '',
    'version': '16.0',
    'summary': """ Managments are made up here""",
    'description': """ Open Academy Management""",
    'depends': ['base','board'],

    'data': [
        'security/ir.model.access.csv',
        'views/academy_course_view.xml',
        'views/demo_data_course_view.xml',
        'views/res_partner_view.xml',
        'views/opneacademy_session_report.xml',
        'data/demo_data_course.xml',

    ],
    'images': ['static/description/icon.png'],
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
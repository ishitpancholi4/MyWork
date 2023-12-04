# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Real Estate',
    'category': 'Real Estate/ Brokerage',
    'version': '16.0',
    'summary': """ Managments are made up here Real Estate""",
    'description': """ 
            - Real Estate,
            - Brokrage,
            - Selling Property
            """,
    # 'depends': ['base','web'],

    'data': [
        'security/ir.model.access.csv',
        'views/real_estate_property_view.xml',
    ],
    'images' : ['static/description/icon.png'],

    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

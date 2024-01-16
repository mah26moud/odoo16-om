# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management ',
    'version': '1.0.0',
    'category': 'hospital',
    'author': 'mahmoud shady',
    'website': 'mah26moud12@gmail.com',
    'summary': 'Hospital Management System',
    'description': """hospital for more help """,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',

    ],
    'demo': [],
    #'installable': False,
    #'auto_install': False,
    'license': 'LGPL-3'


}

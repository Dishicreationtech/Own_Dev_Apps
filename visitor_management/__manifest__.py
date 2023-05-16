{
    'name': "Visitor Management",
    'version': '1.0.01',
    'category':'visitor',
    'website': 'https://www.dishicreation.com',
    'summary': 'Visitor Details Applicatipn',
    'description': """Visitor Management Applicatipn System""",
    'depends': ['base'],
    'data': [ 
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/visitor_detail_view.xml',
        

        ],
    'demo': [],
    'installable': True,
    'auto install':'False',
    'application': True,
    'license': 'LGPL-3',
    'sequence': 3,
}

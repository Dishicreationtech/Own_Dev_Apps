{
    'name': "Duty Resumption",
    'version': '1.0.01',
    'category':'Employee',
    'website': 'https://www.dishicreation.com',
    'summary': 'Duty Resumption application',
    'description': """Duty Resumption appication system""",
    'depends': ['base','hr'],
    'data': [ 
        'security/ir.model.access.csv',
        'views/menu.xml',
        ],
    'demo': [],
    'installable': True,
    'auto install':'False',
    'application': True,
    'license': 'LGPL-3',
    'sequence': 3,
}
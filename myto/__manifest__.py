{
    'name': 'My test module',
    'summary': 'UA TEST GUN MY AR',

    'author': 'xtos tam ua',
    'website': 'https://des-tam.ua',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.0.0.1',

    'depends': [
        'base',
        ],

    'external_dependencies': {'python': [], },
    'data': [
        'security/ir.model.access.csv',
        'views/my_to_views.xml',
    ],
    'demo': [
        'demo/my_demo.xml'
    ],

    'installable': True,
    'auto_install': False,
    'aplication': False,
    'images': [
       'static/description/cover.png',
       'static/description/icon.png',
    ],
    'price': 0,
    'curency': 'EUR',
}

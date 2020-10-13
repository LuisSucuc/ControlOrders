# -*- coding: utf-8 -*-

response.menu = [
    (T('Comprar'),     'flaticon-cart',         URL('default', 'index' ), []),
    (T('Administración'), 	'flaticon-time',     None, 
        [
            (T('Clasificaciones'),      False,        URL( 'products', 'product_types' ),     []),
            (T('Products'),             False,        URL( 'products', 'products' ), []),
            (T('Reporte'),              False,        URL( 'products', 'report' ), []),
            (T('Comprados'),            False,        URL( 'products', 'my_products' ), []),
        ]
    ),
]

if auth.has_membership(group_id='Administrator'):
    response.menu += [ (T('Manage'),     'flaticon-interface-1',        None, 
                        [
                            (T('Users'),       False,      URL( 'manage', 'users' ), []),
                        ]),
                    ]
# -*- coding: utf-8 -*-

response.menu = [
    (T('Comprar'),     'flaticon-map',         URL('default', 'index' ), []),
    (T('Menu'), 	'flaticon-time',     None, 
        [
            (T('Clasificaciones'),      False,        URL( 'default', 'index' ),     []),
            (T('Products'),             False,        URL( 'products', 'products' ), []),
            (T('Report'),               False,        URL( 'products', 'report' ), []),
        ]
    ),
]

if auth.has_membership(group_id='Administrator'):
    response.menu += [ (T('Manage'),     'flaticon-interface-1',        None, 
                        [
                            (T('Users'),       False,      URL( 'manage', 'users' ), []),
                        ]),
                    ]
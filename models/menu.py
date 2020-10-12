# -*- coding: utf-8 -*-

response.menu = [
    (T('Home'),     'flaticon-map',         URL('default', 'index' ), []),
    (T('Menu'), 	'flaticon-time',     None, 
        [
            (T('Test'),       False,        URL( 'default', 'index' ), []),
            (T('Controller'),   False,      URL( 'default', 'index' ), []),
        ]
    ),
]

if auth.has_membership(group_id='Administrator'):
    response.menu += [ (T('Manage'),     'flaticon-interface-1',        None, 
                        [
                            (T('Users'),       False,      URL( 'manage', 'users' ), []),
                        ]),
                    ]
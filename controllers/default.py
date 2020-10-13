# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
@auth.requires_login()
def index():
    return dict()

@auth.requires_login()
def buy():
    products = db(db.product.owner!=auth.user_id).select()
    return dict(products = products)


@auth.requires_login()
def buy_product():
    print(request.vars.product_id)
    return db.purchased_product.validate_and_insert( product = request.vars.product_id,
                                                    price = request.vars.price)



# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if request.args(0)=='login':
        redirect(URL('default','login'))
    return dict(form=auth())

def login():
    """
    exposes:
    http://..../[app]/default/user/login
    """
    form=auth.login()
    return dict(form = form)

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

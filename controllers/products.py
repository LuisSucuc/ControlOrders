
# -*- coding: utf-8 -*-

@auth.requires_login()
def products():
    products = db(db.product.owner == auth.user_id).select()
    return dict(products = products)


@auth.requires_login()
def report():
    products = db(db.product.owner == auth.user_id).select()
    def get_total_sales(product_id):
        return 100
    return dict(products = products,
                get_total_sales = get_total_sales)


@auth.requires_login()
def edit_product():
    product_id = request.vars.product_id

    form = SQLFORM(db.product,
                   record = product_id,
                   _class = 'form-horizontal',
                   showid =False)

    if form.process().accepted:
        session.flash = T('Saved')
        redirect(URL('products'))
    elif form.errors:
        response.flash = T('Check your data')
    return dict(form = form,
    			      product_id = product_id)

@auth.requires_login()
def delete_product():
	#db(db.product.id == request.vars.product_id).delete()
	session.flash = T('Deleted')
	redirect(URL('products'))
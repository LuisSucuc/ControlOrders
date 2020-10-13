
# -*- coding: utf-8 -*-

@auth.requires_login()
def products():
    products = db(db.product.owner == auth.user_id).select()
    return dict(products = products)


@auth.requires_login()
def report():
    sum = db.purchased_product.price.sum()
    products = db(db.product.owner == auth.user_id).select()
    number_products = db(db.product.owner == auth.user_id).count()
    avg = db.purchased_product.price.avg() or 0
    products_avg = db(db.product.owner == auth.user_id).select(avg).first()[avg] or 0
    global_total_sales = db((db.product.owner == auth.user_id)&
                     (db.purchased_product.product == db.product.id)).select(sum).first()[sum] or 0
    def get_total_sales(product_id):
        return db(db.purchased_product.product == product_id).select(sum).first()[sum] or 0
    def get_number_sales(product_id):
        return db(db.purchased_product.product == product_id).count()
    return dict(products = products,
                products_avg = products_avg,
                get_total_sales = get_total_sales,
                get_number_sales = get_number_sales,
                global_total_sales = global_total_sales,
                number_products    = number_products)

@auth.requires_login()
def my_products():
    __products = db(db.purchased_product.buyer == auth.user_id)._select(db.purchased_product.product)
    products = db(db.product.id.belongs(__products)).select(db.product.ALL)
    def get_total(product_id):
        return db((db.purchased_product.product == product_id)&
                  (db.purchased_product.buyer == auth.user_id)).count()
    return dict(products    = products,
                get_total = get_total)

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
from flask import Flask, render_template, request, jsonify, redirect, url_for

import database as dbbase

from product import Product
from customers import Customer
from supplier import Supplier

db = dbbase.dbConnection()

app= Flask(__name__)

@app.route('/')
def home():
    index = db['index']
    indexReceived = index.find()
    return render_template('index.html', index=indexReceived)

####################### CRUD PRODUCTOS #####################################
@app.route('/products')
def home_products():
    products = db['products']
    productsReceived = products.find()
    return render_template('products.html', products=productsReceived)

#metodo post
@app.route('/products', methods=['POST'])
def addProducts():
    products = db['products']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        product = Product(nombre, precio, cantidad)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'nombre' : nombre,
            'precio' : precio,
            'cantidad' : cantidad,
        })
        return redirect(url_for('home_products'))
    else:
        return notFound()
    
#method delete 
@app.route('/delete_products/<string:product_name>')
def delete_products(product_name):
    products =db['products']
    products.delete_one({'nombre' : product_name})
    return redirect(url_for('home_products'))

#method Put
@app.route('/edit_product/<string:product_name>', methods=['POST'])
def edit_product(product_name):
    products = db['products']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        products.update_one({'name':product_name}, {'$set':{'nombre' : nombre, 'precio' : precio, 'cantidad' : cantidad}})
        response = jsonify({'mensaje' : 'Producto' + product_name + 'Actualizado correctamente'})
        return redirect(url_for('home_products'))
    else:
        return notFound()

########################## CRUD CLIENTES ################################
@app.route('/customers')
def home_customers():
    customers = db['customers']
    customersReceived = list(customers.find())
    return render_template('customers.html', customers=customersReceived)

    #metodo post
@app.route('/customers', methods=['POST'])
def addcustomers():
    customers = db['customers']
    nombre = request.form['nombre']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    direccion = request.form['direccion']
    celular = request.form['celular']
    nota = request.form['nota']

    if nombre and apellidoP and apellidoM and direccion and celular and nota:
        customer = Customer(nombre, apellidoP, apellidoM, direccion, celular, nota)
        customers.insert_one(customer.toDBCollection())
        response = jsonify({
            'nombre' : nombre,
            'apellidoP' : apellidoP,
            'apellidoM' : apellidoM,
            'direccion': direccion,
            'celular' : celular,
            'nota' : nota,
        })
        return redirect(url_for('home_customers'))
    else:
        return notFound()

 #method delete 
@app.route('/delete_customer/<string:customer_name>')
def delete_customer(customer_name):
    customers =db['customers']
    customers.delete_one({'nombre' : customer_name})
    return redirect(url_for('home_customers'))

#method Put
@app.route('/edit_customer/<string:customer_name>', methods=['POST'])
def edit_customer(customer_name):
    customers = db['customers']
    nombre = request.form['nombre']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    direccion = request.form['direccion']
    celular = request.form['celular']
    nota = request.form['nota']

    if nombre and apellidoP and apellidoM and direccion and celular and nota:
        customers.update_one({'nombre':customer_name}, {'$set':{'nombre' : nombre, 'apellidoP' : apellidoP, 'apellidoM' : apellidoM,'direccion' : direccion, 'celular' : celular, 'nota' : nota, }})
        response = jsonify({'mensaje' : 'Cliente' + customer_name + 'Actualizado correctamente'})
        return redirect(url_for('home_customers'))
    else:
        return notFound() 

    ###############################  CRUD PROVEEDORES  ##########################3

################## CRUD Proveedores
@app.route('/suppliers')
def home_suppliers():
    suppliers = db['suppliers']
    suppliersReceived = list(suppliers.find())
    return render_template('suppliers.html', suppliers=suppliersReceived)

#metodo post
@app.route('/suppliers', methods=['POST'])
def addsuppliers():
    suppliers = db['suppliers']
    nombre = request.form['nombre']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    direccion = request.form['direccion']
    celular = request.form['celular']
    nota = request.form['nota']

    if nombre and apellidoP and apellidoM and direccion and celular and nota:
        supplier = Supplier(nombre, apellidoP, apellidoM, direccion, celular, nota)
        suppliers.insert_one(supplier.toDBCollection())
        response = jsonify({
            'nombre' : nombre,
            'apellidoP' : apellidoP,
            'apellidoM' : apellidoM,
            'direccion': direccion,
            'celular' : celular,
            'nota' : nota,
        })
        return redirect(url_for('home_suppliers'))
    else:
        return notFound()


 #method delete 
@app.route('/delete_supplier/<string:supplier_name>')
def delete_supplier(supplier_name):
    suppliers = db['suppliers']
    suppliers.delete_one({'nombre' : supplier_name})
    return redirect(url_for('home_suppliers'))

#method Put
@app.route('/edit_supplier/<string:supplier_name>', methods=['POST'])
def edit_supplier(supplier_name):
    suppliers = db['suppliers']
    nombre = request.form['nombre']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    direccion = request.form['direccion']
    celular = request.form['celular']
    nota = request.form['nota']

    if nombre and apellidoP and apellidoM and direccion and celular and nota:
        suppliers.update_one({'name':supplier_name}, {'$set':{'nombre' : nombre, 'apellidoP' : apellidoP, 'apellidoM' : apellidoM,'direccion' : direccion, 'celular' : celular, 'nota' : nota, }})
        response = jsonify({'mensaje' : 'Proveedor' + supplier_name + 'Actualizado correctamente'})

        return redirect(url_for('home_suppliers'))
    else:
        return notFound()

    ####################################################  Pagina no encontrada
    
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message' : 'No encontrado: ' + request.url,
        'status' : 404
    }

    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000) 

""" if __name__ == '__main__':
    app.run(debug=False, use_reloader=False) """

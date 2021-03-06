from flask import render_template
from app import app
from models.order_details import orders

@app.route('/orders')
def index():
    return render_template('index.html' , title='Our Shop', orders=orders)

@app.route('/orders/<order_id>')
def get_order(order_id):
    index = None
    for order in orders:
        if order.order_id == int(order_id):
            index = orders.index(order)

    return render_template('order.html' , title='Orders Page', product=orders[index])


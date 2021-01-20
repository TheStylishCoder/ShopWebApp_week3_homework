from flask import render_template
from app import app
from app.models.orders_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Dried Flower Company', orders=orders)

@app.route('/orders/<index>')
def single_order(index):
    chosen_order = orders[int(index)] #chosen order is the order from the orders list at the chosen index
   
    return render_template('order.html', order=chosen_order)
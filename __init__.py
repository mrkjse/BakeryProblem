from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField, RadioField, DateField
import json
from forms.reusableform import ReusableForm
from sqlalchemy import create_engine, text
import datetime
from coinchange import pack_product, order_product, generate_data

# App config.
#DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'this is my secret key'



 ### ERROR HANDLERS ###
def handle_error(e):
    """

    Displays a default Error view if the app encounters an error.

    """

    try:
        if e.description is not None:
            error = {}
            error["message"] = e.description
    except:
        error = e
    return render_template('error.html', error=error)

app.register_error_handler(404, handle_error)
app.register_error_handler(500, handle_error)


### VIEWS ###
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def hello():
    """
    
    Initializes the FLASK app.

    """

    # Generate the table menu 
    bakery_goods = generate_data('')
    bakery_goods.drop(columns=['Quantity'], inplace=True)
    bakery_data = bakery_goods.to_dict(orient='records')

    # Display the web form view
    if request.method == 'GET':  
        # Load the form
        form = ReusableForm(request.form) 

        # Load the view  
        return render_template('index.html', form=form, data=bakery_data)
    elif request.method == 'POST':

        # Retrieve the string input
        bakery_orders = request.form['bakeryOrder']

        # Try to process the string input (order) per line
        orders = bakery_orders.split('\n')
        orders = [s.strip('\r') for s in orders]
        results = [order_product(s) for s in orders]

        # Format output
        form = ReusableForm(request.form)
        form.bakeryOrder.data = bakery_orders
        form.bakeryOutput.data = '\n'.join(results)

        # Load the view
        return render_template('index.html', form=form, data=bakery_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

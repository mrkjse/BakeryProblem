from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField, RadioField, DateField



class ReusableForm(Form):
    bakeryOrder = TextAreaField('Order Form (Input)', render_kw={"placeholder": 'Sample Input:\r\n10 VS5\r\n14 MB11\r\n13 CF'})
    bakeryOutput = TextAreaField('Package Allocation (Output)')

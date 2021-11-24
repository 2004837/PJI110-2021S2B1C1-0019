from flask import Blueprint, render_template, request
from datetime import datetime
from .models import Customer
from . import db
import json

views= Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])

def home():
    customer_name=""
    if request.method =='POST':
        celular = request.form.get('celular')
        customer = Customer.query.filter_by(celular=celular).first()
        if customer:
            customer_name=customer.name
        else:
            customer_name="Cliente não cadastrado"
   

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return render_template("home.html",customer_name=customer_name,dt_string=dt_string)


@views.route('/cadastrar',methods=['GET','POST'])

def cadastrar():
    if request.method == 'POST':
        celular = request.form.get('celular')
        name=request.form.get('name')
        new_customer=Customer(celular=celular,name=name)
        db.session.add(new_customer)
        db.session.commit()
    return render_template("cadastrar.html")

@views.route('/cadastro')
def cadastro(): 
    table_data = Customer.query.all()
    return render_template('cadastro.html', table_data=table_data)
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.cookie_model import Cookie

@app.route('/')
def index():
    return redirect ('/cookies')

@app.route('/cookies')
def dashboard():
    cookies = Cookie.get_all()
    return render_template ('dash.html', all_orders = cookies)

@app.route('/new')
def show_create_page():
    return render_template('create.html')

@app.route('/go_home')
def go_home():
    return redirect('/cookies')

@app.route('/create_order', methods = ['post'])
def create_order():
    print(request.form)
    if not Cookie.cookie_validator(request.form):
        return redirect('/new')
    order = Cookie.save(request.form)
    return redirect('/cookies')

@app.route('/edit_order/<int:id>')
def edit_order(id):
    data = {
        'id': id
    }
    return render_template('edit_order.html', one_order = Cookie.get_one_order(data))

@app.route('/update_order/<int:id>', methods = ['post'])
def update_order(id):  
    if not Cookie.cookie_validator(request.form):
        return redirect(f'/edit_order/{id}')
    Cookie.update_order(request.form,id)
    return redirect('/cookies')
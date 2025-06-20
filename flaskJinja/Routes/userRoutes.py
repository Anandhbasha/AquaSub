from flask import Blueprint, render_template, request, redirect, url_for, flash
from Controller.userController import *

userRoutes = Blueprint('userRoutes', __name__)

@userRoutes.route('/')
def home():
    data = get_all_users()
    return render_template('index.html', users=data)

@userRoutes.route('/add', methods=['POST'])
def add_user():
    new_id = len(get_all_users()) + 1
    name = request.form['name']
    email = request.form['email']
    create_user({'id': new_id, 'name': name, 'email': email})
    flash('User Added Successfully!')
    return redirect(url_for('userRoutes.home'))

@userRoutes.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    name = request.form['name']
    email = request.form['email']
    update_user(user_id, {'name': name, 'email': email})
    flash('User Updated Successfully!')
    return redirect(url_for('userRoutes.home'))

@userRoutes.route('/delete/<int:user_id>')
def delete(user_id):
    delete_user(user_id)
    flash('User Deleted Successfully!')
    return redirect(url_for('userRoutes.home'))

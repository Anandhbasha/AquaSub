users = [
    {'id': 1, 'name': 'Raj', 'email': 'raj@gmail.com'},
    {'id': 2, 'name': 'Kumar', 'email': 'kumar@gmail.com'}
]

def get_all_users():
    return users

def get_user_by_id(user_id):
    return next((user for user in users if user['id'] == user_id), None)

def create_user(new_user):
    users.append(new_user)

def update_user(user_id, updated_data):
    user = get_user_by_id(user_id)
    if user:
        user.update(updated_data)
    return user

def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]

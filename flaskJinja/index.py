from flask import Flask
from Routes.userRoutes import userRoutes

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flashing messages

app.register_blueprint(userRoutes)

if __name__ == '__main__':
    app.run(debug=True)

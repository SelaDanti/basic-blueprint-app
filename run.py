from flask import Flask
from app.setup import app_v1


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(app_v1)
    app.run(debug=True)
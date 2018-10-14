from flask import Flask
from app.api.v1 import app_v1


app = Flask(__name__)
app.register_blueprint(app_v1)
app.run(debug=True)
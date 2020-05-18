from flask import Flask
from .api import main


app = Flask(__name__)
app.register_blueprint(main)

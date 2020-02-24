from flask import Blueprint, request, render_template

# initilialize main
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('about.html')

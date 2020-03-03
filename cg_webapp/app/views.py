from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/help')
def help():
    return render_template('help.html')

from flask import Blueprint, render_template, request
import torch


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        latent_vector = torch.randn(1, 100, 1, 1)
        print(latent_vector)

        return render_template('index.html', latent_vector=latent_vector)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/help')
def help():
    return render_template('help.html')

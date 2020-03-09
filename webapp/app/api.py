from flask import Blueprint, render_template, request
import torch
from .model import generator
import matplotlib.pyplot as plt
import numpy as np


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        latent_vector = torch.randn(1, 100, 1, 1)
        image = generator.generator(latent_vector).numpy()[0].transpose(1, 2, 0)
        # image values between [-1..1], converting to [0..1]/[0..255] 
        image = ((image + 1)*255 / (2)).astype(np.uint8)
        plt.imsave('app/static/generated/gen.png', image)

        return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/help')
def help():
    return render_template('help.html')

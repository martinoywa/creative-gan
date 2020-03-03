from flask import Blueprint, render_template, request
import torch
from .model.generator import generator
#import matplotlib.pyplot as plt


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        latent_vector = torch.randn(1, 100, 1, 1)
        image = generator(latent_vector).numpy()[0].transpose(1, 2, 0)
        #plt.savefig()
        #img = cv2.imwrite('../generated/gen.png', image)

        return render_template('index.html', image_name=image)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/help')
def help():
    return render_template('help.html')

import os

from flask import Flask
from flask import render_template, redirect, request
import torch
from models.generator import generate
import matplotlib.pyplot as plt
import numpy as np

from random import randint


app = Flask(__name__)

# configuration
app.config["GENERATED_FOLDER"] = "static/generated/"

if 'generated' not in os.listdir('static'):
    os.mkdir(app.config["GENERATED_FOLDER"])


def generate_image(latent_vector):
    if latent_vector != None:
        image = generate(latent_vector).numpy()[0].transpose(1, 2, 0)
        return image
    else:
        return False


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        latent_vector = torch.randn(1, 100, 1, 1)

        fake = generate_image(latent_vector)
        if fake.any():
            filename = "generated_image"+str(randint(1, 1000000000))+".png"
            plt.imsave(os.path.join(app.config["GENERATED_FOLDER"], filename),
                        ((fake + 1)*255 / (2)).astype(np.uint8))
        else:
            return redirect(request.url)

    return render_template("results.html", filename=filename)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True)

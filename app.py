import os

from flask import Flask
from flask import render_template, redirect, request
import torch
from models.generator import generate
from random import randint

from torchvision import utils, transforms


app = Flask(__name__)

# configuration
app.config["GENERATED_FOLDER"] = "static/generated/"

if 'generated' not in os.listdir('static'):
    os.mkdir(app.config["GENERATED_FOLDER"])


def generate_image(latent_vector):
    if latent_vector != None:
        image = generate(latent_vector)
        return image
    else:
        return False


def unnormalize_image(fake_image):
    fake_image = fake_image / 2 + 0.5
    return fake_image


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        latent_vector = torch.randn(64, 100, 1, 1)

        fake = generate_image(latent_vector)

        if fake.numpy().any():
            filename = "generated_image"+str(randint(1, 1000000000))+".png"
            utils.save_image(utils.make_grid(unnormalize_image(fake), padding=2).cpu(),
                             os.path.join(app.config["GENERATED_FOLDER"], filename))
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
    app.run(debug=False)

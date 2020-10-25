import unittest
import os.path
from pathlib import Path
import torch
from models.generator import generate

class TestGenerator(unittest.TestCase):
    def test_checkpoints_loader(self):
        """
        Assert that checkpoint file exists
        :return: True if exists else False
        """
        weights = Path('models/checkpoints/cars-0.0.6-Monday.pt')
        self.assertTrue(os.path.isfile(weights), True)

    def test_image_generation(self):
        """
        Assert that images are being generated
        is of correct shape
        :return: True if generation works
        """
        latent_vector = torch.randn(1, 100, 1, 1)
        image = generate(latent_vector)
        self.assertEqual([1, 3, 64, 64], list(image.shape))

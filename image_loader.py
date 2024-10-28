# pylint: disable=trailing-whitespace
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=missing-final-newline
# pylint: disable=attribute-defined-outside-init
# pylint: disable=consider-using-enumerate
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=import-error
# pylint: disable=no-name-in-module

import os

import pygame as pg

class ImageLoader:
    """ Loads images from a given directory and returns """
    @staticmethod
    def load(path: str) -> dict:
        """ Loads images from a given directory and returns a dictionary of the images

        Args:
            path (str): The directory to load the images from

        Returns:
            dict: A dictionary where the key is the image name and the value is a pygame Surface
        """
        images = {}
        for file_name in os.listdir(path):
            if file_name.endswith(".png"):
                image_surface = pg.image.load(os.path.join(path, file_name))
                images[file_name.split(".")[0]] = image_surface
        return images
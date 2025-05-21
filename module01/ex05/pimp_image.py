import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    
    print("inverting")

    array = 255 - array

    print(array)
    img = Image.fromarray(array)
    plt.imsave("invert.png", array)


def ft_red(array) -> np.ndarray:
    """Applies red filter to the image received."""

    img = Image.fromarray(array)
    plt.savefig("red.png")


def ft_green(array):
    """Applies green filter to the image received."""

    img = Image.fromarray(array)
    plt.savefig("green.png")


def ft_blue(array):
    """Applies blue filter to the image received."""

    img = Image.fromarray(array)
    plt.savefig("blue.png")


def ft_grey(array):
    """Applies grey filter to the image received."""

    img = Image.fromarray(array)
    plt.savefig("grey.png")

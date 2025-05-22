import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""

    cpy = array.copy()
    cpy = 255 - cpy
    plt.imsave("invert.png", cpy)
    return (cpy)


def ft_red(array) -> np.ndarray:
    """Applies red filter to the image received."""

    cpy = array.copy()
    cpy[:, :, 1] = 0      # set G to 0
    cpy[:, :, 2] = 0      # set B to 0
    plt.imsave("red.png", cpy)
    return (cpy)


def ft_green(array) -> np.ndarray:
    """Applies green filter to the image received."""

    cpy = array.copy()
    cpy[:, :, 0] = 0      # set R to 0
    cpy[:, :, 2] = 0      # set B to 0
    plt.imsave("green.png", cpy)
    return (cpy)


def ft_blue(array) -> np.ndarray:
    """Applies blue filter to the image received."""

    cpy = array.copy()
    cpy[:, :, 0] = 0      # set R to 0
    cpy[:, :, 1] = 0      # set G to 0
    plt.imsave("blue.png", cpy)
    return (cpy)


def ft_grey(array):
    """Applies grey filter to the image received."""

    cpy = array.copy()
    # grey = (0.2989 * cpy[:, :, 0] +
    #         0.5870 * cpy[:, :, 1] +
    #         0.1140 * cpy[:, :, 2]).astype(np.uint8)
    # cpy[:, :, 0] = grey
    # cpy[:, :, 1] = grey
    # cpy[:, :, 2] = grey

    # can only use = and / operators???

    grey = cpy[:, :, 0] / 3     # set everything to 1/3 of R
    cpy[:, :, 0] = grey
    cpy[:, :, 1] = grey
    cpy[:, :, 2] = grey

    plt.imsave("grey.png", cpy)
    return (cpy)

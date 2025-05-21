from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """loads an image, prints its format, and its pixels
content in RGB format."""

    try:
        img = Image.open(path)
        rgb_array = np.array(img)
        # print(f"The shape of image is: {rgb_array.shape}")
    except Exception as e:
        print(f"{e}")
        return []

    return rgb_array

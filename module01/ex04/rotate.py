from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def main():
    np_array = ft_load("animal.jpeg")
    # print(np_array)		# Values: (X_pixels, Y_pixels, channels)

    img = Image.fromarray(np_array)

    # Convert image to greyscale
    img = img.convert("L")

    # Crop image
    left = 450
    upper = 100
    img = img.crop((left, upper, left + 400, upper + 400))

    new_array = np.array(img)
    new_array1 = new_array.reshape((400, 400, 1))	    # add extra dimension
    print(f"The shape of image is: {new_array1.shape} or {new_array.shape}")
    print(new_array1)

    # Flip anti-clockwise
    img = img.transpose(Image.TRANSPOSE)
    new_array = np.array(img)
    print(f"New shape after Transpose: {new_array.shape}")
    print(new_array)

    # Save output image
    plt.imshow(img, cmap='grey')
    plt.axis("on")
    plt.savefig("output.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

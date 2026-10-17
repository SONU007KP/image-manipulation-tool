import numpy as np

def crop(image_array, top, bottom, left, right):
    height, width = image_array.shape[:2]

    top_pixels = int(height * top / 100)
    bottom_pixels = int(height * bottom / 100)
    left_pixels = int(width * left / 100)
    right_pixels = int(width * right / 100)

    cropped_array = image_array[
        top_pixels:height - bottom_pixels,
        left_pixels:width - right_pixels
    ]

    return cropped_array

def flip_horizontal(image_array):
    return image_array[:, ::-1]

def flip_vertical(image_array):
    return image_array[::-1, :]

def rotate(image_array, k):
    rotated_array = np.rot90(image_array, k = k)
    return rotated_array

def grayscale(image_array):
    if image_array.ndim == 2:
        return image_array

    gray = (
        0.299 * image_array[:, :, 0] +
        0.587 * image_array[:, :, 1] +
        0.114 * image_array[:, :, 2]
    )

    return gray.astype(np.uint8)

def brightness(image_array, value):
    brightened_array = np.clip(
        image_array.astype(np.int16) + value,
        0,
        255
    ).astype(np.uint8)

    return brightened_array
#!/usr/bin/env python3

import logging
import os
from PIL import Image, ExifTags

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"]

def print_exif_data(image):
    """Prints the EXIF data of a PIL Image object."""
    exif_data = image._getexif()
    if exif_data is not None:
        logging.info("------ EXIF Data ------")
        for tag, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            logging.info(f"{tag_name}: {value}")
    else:
        logging.info("The image does not have any EXIF data.")

def remove_exif(image):
    """Removes the EXIF data from a PIL Image object and returns the modified image."""
    if "exif" in image.info:
        image_without_exif = image._copy()
        return image_without_exif
    else:
        logging.info("The image does not have any EXIF data.")
        return image

def process_image(image_path):
    """Opens an image file and removes its EXIF data."""
    try:
        with Image.open(image_path) as image:
            print_exif_data(image)
            image_without_exif = remove_exif(image)
        
        # Define the new image path, check if it exists and modify it if necessary.
        directory, filename = os.path.split(image_path)
        base, ext = os.path.splitext(filename)
        new_image_path = os.path.join(directory, base + "_no_exif" + ext)

        if os.path.isfile(new_image_path):
            new_image_path = os.path.join(directory, "output_" + base + "_no_exif" + ext)

        image_without_exif.save(new_image_path)
        logging.info("EXIF data has been removed. The new image is saved as %s", new_image_path)

        with Image.open(new_image_path) as modified_image:
            logging.info("------ EXIF Data After Removal ------")
            print_exif_data(modified_image)

    except FileNotFoundError:
        logging.error("The file was not found. Please check the file path: %s", image_path)
    except PermissionError:
        logging.error("You do not have permission to access this file: %s", image_path)
    except IOError:
        logging.error("An error occurred while trying to open this file: %s", image_path)
    except Exception as e:
        logging.error("Unexpected error:", exc_info=True)

def find_and_process_images():
    """Finds all images in the current directory and its subdirectories, and removes their EXIF data."""
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
                image_path = os.path.join(dirpath, filename)
                process_image(image_path)

if __name__ == "__main__":
    find_and_process_images()

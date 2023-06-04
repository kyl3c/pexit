#!/usr/bin/env python3

import logging
import os
import sys
from PIL import Image, ExifTags

EXTENSIONS = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"]

run_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
log_filename = f"logfile_{run_date}.log"

logging.basicConfig(
    level=logging.INFO, 
    handlers=[
        logging.FileHandler(log_filename),  # write logs to file
        logging.StreamHandler(sys.stdout)  # write logs to standard out(CLI)
    ]
)

def pexit_exif_print(image):
    exif_data = image._getexif()
    if exif_data is not None:
        logging.info("~ EXIF present on " + image.filename)
        for tag, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            logging.info(f"{tag_name}: {value}")
    else:
        logging.info("! no EXIF data present on " + image.filename)

def pexit_exif_remove(image):
    if "exif" in image.info:
        image_without_exif = image._copy()
        return image_without_exif
    else:
        logging.info("! no EXIF data present on " + image)
        return image

def pexit_process_remove(image_path):
    try:
        with Image.open(image_path) as image:
            pexit_exif_print(image)
            image_without_exif = pexit_exif_remove(image)

        directory, filename = os.path.split(image_path) 
        base, ext = os.path.splitext(filename)
        new_image_path = os.path.join(directory, base + "_no_exif" + ext) # defines an image path

        if os.path.isfile(new_image_path): # checks if file path exists
            new_image_path = os.path.join(directory, "output_" + base + "_no_exif" + ext) # adjusts if so

        image_without_exif.save(new_image_path)
        logging.info("+ new image saved at " + new_image_path + '\n')

        with Image.open(new_image_path) as modified_image:
            logging.info(" — removed EXIF data from "+ new_image_path + '\n')
            pexit_exif_print(modified_image)

    except FileNotFoundError:
        logging.error("! file was not found, verify this file exists: " + image_path)
    except PermissionError:
        logging.error("! you do not have permission to access this file: " + image_path)
    except IOError:
        logging.error("! an error occurred trying to open this file: " + image_path)
    except Exception as e:
        logging.error("! unexpected error: ", exc_info=True)

def pexit_exif_discover():
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in EXTENSIONS):
                image_path = os.path.join(dirpath, filename)
                pexit_process_remove(image_path)

if __name__ == "__main__":
    pexit_exif_discover()

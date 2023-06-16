# Pexit - A Python Tool to Remove EXIF Data 

This script was written with the specific goal to recursively find and remove EXIF data.

Exchangeable image file format (EXIF) data contains metadata about images, including anything from the camera's aperature to the GPS cooridinates of where the photo was taken and more. Digital cameras, smartphones, and other systems use this info to present and utilize relevant information about a image. Though for lots of users, this info is not relevant and brings with it privacy concerns. This application will recursively locate such metadata within images in the current working directory and its subdirectories, prints the info to standard out for review, and removes the EXIF data.

<br/>

## Features

* Automated search for image files in a directory and its subdirectories
* Reveals existing EXIF data on images and provides verificationof removal through standard out
* Creates a new copy of the image without the EXIF data, preserving the existing file

<br/>

  | Supported File Types  | 
  | :----:        |    
  |    .jpg      |
  |    .jpeg      |
  |    .png      |
  |    .tif      |
  |    .tiff      |
  |    .bmp      |

<br/>

## Pre-requisites

* Python 3.8+ 

* Python Pillow (PIL) 

    ```python   
    pip install pillow
    ```

<br/>
  
## Installation

No installation is required for this script. Clone the repository into a target directory and run the Python script (pexit.py) 

<br/>

## Usage

When ran, the script processes all images in the current directory and its subdirectories with the supported file types

  ```python
  python pexit.py
  ```
    
<br/>

## Notes

* This script will preserve your original image by saving the new image as a separate file without the Exif data, adding the suffix '_no_exif,' to the original filename

* I don't trust Python's garbage cleanup and I won't make you either; image files are explicitly closed when they have finished processing

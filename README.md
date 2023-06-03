# Pexit - A Python Tool to Remove EXIF Data 

This script was written with the specific goal to recursively find and remove EXIF data.

Exchangeable image file format (EXIF) data contains metadata about images, including anything from the camera's aperature to the GPS cooridinates of where the photo was taken and more. This info is used by digital cameras and smartphones alike to present and utilize relevant information about a picture. Though most of the time, this info is not relevant. This application will recursively locate such metadata for images within in the current working directory and its subdirectories, print it out, and then remove the data.

<br/>

## Features

* Automated search for image files in a directory and its subdirectories
* Reveals existing EXIF data on images and provides verificationof removal through standard out
* Creates a new copy of the image without the EXIF data, preserving the existing file

<br/>

## Requirements

This application requires Python 3.8+ and the following Python libraries installed:

* PIL for image processing

You can install these requirements by running 
```python   
pip install -r requirements.txt.
```

<br/>

## Usage

To use this application, simply run the script from your command line from within the target directory:
```python
python pexit.py
```

<br/>
  
#### All images in the current directory and its subdirectories with these file types will be processed at run time:

  | Supported File Types  | 
  | :----:        |    
  |    .jpg      |
  |    .jpeg      |
  |    .png      |
  |    .tif      |
  |    .tiff      |
  |    .bmp      |

<br/>

## Notes

* This script will preserves your original image by saving the new image as a separate file without the Exif data, adding the suffix '_no_exif,' to the original filename

* I don't trust Python's garbage cleanup and I won't make you either; image files are explicitly closed when they have finished processing

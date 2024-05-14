This code was created with academic purposes.
It is part of a class project from the Technische Hochschule Ulm where students were prompted to test the viability of image recognition for catheter tip identification on fluoroscopy images.
The code simply converts the hdf5 file provided from the WEISS catheter dataset into .png image files.
The original approach of the Main.py found in the WEISS catheter dataset README file was not sufficient for the purposes of image annotation since it simply opened single images from the file.
The approach found here converts all the images found in the dataset(not the labels) to .png files in the same folder.

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:26:49 2020

@author: tcollazuol
"""

import os
import sys
import shutil
from tkinter import filedialog
from tkinter import *


# Have Tkinter open a file dialog window and get the path from user input
root = Tk()
root.directory = filedialog.askdirectory()

# Print the path to the console for verification.
print(root.directory)

# Set the path to the new folder. 
#TODO User input to set the destination folder.
path = root.directory
dst_foldername = "Renamed"
dst_path = os.path.join(path, dst_foldername)

# Check if the path exists. If it doesn't, create the folder.
if os.path.exists(dst_path):
    print ("Folder Already Exists")
else:
    os.makedirs(dst_path)

# create iterable 
i = 1

# Create a loop for all files in the folder(directory)
for item in os.listdir(path):
    # Check if the item selected is a file, not a folder
    if os.path.isfile(os.path.join(path, item)):
        # Check if the file ends with .jpg or .JPG, only work on .jpgs
        if not (item.endswith('.jpg') or item.endswith('.JPG')):
                continue 
        # Print the files found to the console.
        print('FILE INSIDE: ', item)
        # Create the new file name        
        itemName = "Photo No. " + str(i) + '.jpg'
        i += 1
        # Set file source directory
        file_src_dir = os.path.join(path, item)
        # Set destination source directory
        file_dest_dir = os.path.join(dst_path, itemName)
        # Copy the file from the source dir to the dest. with the new filename.
        shutil.copy(file_src_dir, file_dest_dir)
    
# Close the Tkinter winter.
root.destroy()

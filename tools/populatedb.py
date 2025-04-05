import sqlite3
import os
import glob

#Open database
conn = sqlite3.connect('../database.db')

# Insert an image
# Define the folder path where images are stored
image_folder = "../datasets/tigro"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "Bruses"))


# Define the folder path where images are stored
image_folder = "../datasets/osama-xa04t"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "Burns"))

# Commit the changes
conn.commit()

# Close the connection when done
conn.close()

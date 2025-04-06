import sqlite3
import os
import glob

#Open database
conn = sqlite3.connect('../database.db')

# Insert an image

# skinType table
# Define the folder path where images are stored
image_folder = "../datasets/normal"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "normal"))

# Define the folder path where images are stored
image_folder = "../datasets/acne"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "acne"))

# Define the folder path where images are stored
image_folder = "../datasets/antopicdermatitis"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "antopicdermatitis"))

# Define the folder path where images are stored
image_folder = "../datasets/bruise"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "bruise"))

# Define the folder path where images are stored
image_folder = "../datasets/chickenpox"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "chickenpox"))

# Define the folder path where images are stored
image_folder = "../datasets/eczema"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "eczema"))

# Define the folder path where images are stored
image_folder = "../datasets/firstdegburn"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "firstdegburn"))

# Define the folder path where images are stored
image_folder = "../datasets/herpes"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "herpes"))

# Define the folder path where images are stored
image_folder = "../datasets/hives"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "hives"))

# Define the folder path where images are stored
image_folder = "../datasets/impetigo"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "impetigo"))

# Define the folder path where images are stored
image_folder = "../datasets/melanoma"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "melanoma"))

# Define the folder path where images are stored
image_folder = "../datasets/monkeypox"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "monkeypox"))

# Define the folder path where images are stored
image_folder = "../datasets/pimple"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "pimple"))

# Define the folder path where images are stored
image_folder = "../datasets/psoriasis"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "psoriasis"))

# Define the folder path where images are stored
image_folder = "../datasets/scabies"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "scabies"))

# Define the folder path where images are stored
image_folder = "../datasets/seconddegburns"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "seconddegburns"))

# Define the folder path where images are stored
image_folder = "../datasets/skincancer"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "skincancer"))

# Define the folder path where images are stored
image_folder = "../datasets/thirddegburns"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "thirddegburns"))

# Define the folder path where images are stored
image_folder = "../datasets/vitiligo"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "vitiligo"))

# Define the folder path where images are stored
image_folder = "../datasets/warts"

# Get all image files with extensions .jpg, .png, .jpeg
image_files = glob.glob(os.path.join(image_folder, "*.jpg")) + \
              glob.glob(os.path.join(image_folder, "*.png")) + \
              glob.glob(os.path.join(image_folder, "*.jpeg"))

# Loop through each image file for every category
for image_path in image_files:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                    (image_data, "warts"))

# Commit the changes
conn.commit()

# Close the connection when done
conn.close()

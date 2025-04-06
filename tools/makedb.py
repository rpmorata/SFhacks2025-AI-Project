import sqlite3

#Open database
conn = sqlite3.connect('../database.db')

#Create table
# CREATE TABLE skinType (
#	id INT primary key,
#	image VARCHAR(100),
#	classification ENUM ('normal', 'acne', 'atopicdermatitis', 'bruise', 'chickenpox', 'eczema', 'firstdegburns', 'herpes', 'hives', 'impetigo', 'melanoma', 'monkeypox', 'pimple', 'psoriasis', 'scabies', 'seconddegburns', 'skincancer', 'thirddegburns', 'vitiligo', 'warts')
# )
conn.execute('''CREATE TABLE skinType 
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		image_data BLOB,  -- Store the actual binary image data
        classification TEXT CHECK(classification IN ('normal', 'acne', 'atopicdermatitis', 'bruise', 'chickenpox', 'eczema', 'firstdegburns', 'herpes', 'hives', 'impetigo', 'melanoma', 'monkeypox', 'pimple', 'psoriasis', 'scabies', 'seconddegburns', 'skincancer', 'thirddegburns', 'vitiligo', 'warts'))
		)''')

conn.close()


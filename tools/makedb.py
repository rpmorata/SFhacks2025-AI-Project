import sqlite3

#Open database
conn = sqlite3.connect('../database.db')

#Create table
# CREATE TABLE skinType (
#	id INT primary key,
#	image VARCHAR(100),
#	category ENUM ('Normal', 'Skin Disease', 'Bruses', 'Acne', 'Monkey Pox', 'Burns')
# )
conn.execute('''CREATE TABLE skinType 
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		image_data BLOB,  -- Store the actual binary image data
        classification TEXT CHECK(classification IN ('Normal', 'Skin Disease', 'Bruses', 'Acne', 'Monkey Pox', 'Burns'))
		)''')

conn.close()


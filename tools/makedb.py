import sqlite3

#Open database
conn = sqlite3.connect('../database.db')

#Create table
# CREATE TABLE skinType (
#	id INT primary key,
#	image VARCHAR(100),
#	classification ENUM ('Normal', 'Skin Disease', 'Bruses', 'Acne', 'Monkey Pox', 'Burns')
# )
conn.execute('''CREATE TABLE skinType 
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		image_data BLOB,  -- Store the actual binary image data
        classification TEXT CHECK(classification IN ('Normal', 'Skin Disease', 'Bruses', 'Acne', 'Monkey Pox', 'Burns'))
		)''')

#Create table
# CREATE TABLE skinType (
#	id INT primary key,
#	image_data BLOB, 
#	classification TEXT CHECK(classification IN ('White', 'Not White'))
# )
conn.execute('''CREATE TABLE whiteOrNot 
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		image_data BLOB,
        classification TEXT CHECK(classification IN ('White', 'Not White'))
		)''')

conn.close()


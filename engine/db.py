import csv
import sqlite3

con = sqlite3.connect('alexa.db')
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS website_commands(id integer PRIMARY KEY, name varchar(100), url varchar(100))"
# cursor.execute(query)

# query = "INSERT INTO website_commands(name,url) VALUES ('youtube','https://www.youtube.com')"
# cursor.execute(query)
# con.commit()

# system_commands

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(
#             ''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# 4. Insert Single contacts (Optional)
# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890')"
# cursor.execute(query)
# con.commit()

# query = 'karthik'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
#                ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

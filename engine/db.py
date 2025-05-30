import sqlite3

con = sqlite3.connect('alexa.db')
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS website_commands(id integer PRIMARY KEY, name varchar(100), url varchar(100))"
cursor.execute(query)

# query = "INSERT INTO website_commands(name,url) VALUES ('youtube','https://www.youtube.com')"
# cursor.execute(query)
# con.commit()

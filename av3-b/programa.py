import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="sakila",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(film_id), rating  from film GROUP BY rating;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


































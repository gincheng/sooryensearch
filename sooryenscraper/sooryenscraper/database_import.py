import pymysql
import json 

mydb = pymysql.connect(
  host="",
  user="",
  passwd="",
  database=""
)

with open("craigslist.json", "r") as read_file:
    data = json.load(read_file)
    # print(data)
    insertData = []
    for item in data: 
        insertData.append((item['name'],item['price'].replace("$",""),item['link']))

mycursor = mydb.cursor()

sql = "INSERT INTO items (name, price, link) VALUES (%s, %s ,%s)"
mycursor.executemany(sql, insertData)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


import mysql.connector

# insert , update, delete
ReadQuery="Select * from jobs"

try:
    con=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="hr")
    cursor=con.cursor()
    # cursor.execute(updateQuery)
    cursor.execute(ReadQuery)
    for row in cursor:
        print(row[0],row[1],row[2],row[3],end="       ")
    con.close()                             #---Connction Closed
except:
    print("Connection Failed")

print("Finished")

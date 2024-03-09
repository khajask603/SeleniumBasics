import mysql.connector

# insert , update, delete
insertQuery="insert into student values(104,'Kim')"
updateQuery="Update student set sname ='marry' where sid=104;"
deleteQuery="DELETE FROM STUDENT WHERE SID=104"

try:
    con=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="mydb")
    cursor=con.cursor()
    # cursor.execute("insert into student values(104,'Kim')")     #Executing Query Directly Through Cursour
    # cursor.execute(insertQuery)
    # cursor.execute(updateQuery)
    cursor.execute(deleteQuery)
    con.commit()
    con.close()
except:
    print("Connection Failed")

print("Finished")

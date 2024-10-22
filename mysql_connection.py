# DESCRIPTION: This file contains the optional functionality to connect the game to a MySQL database and insert records into the database. It also contains a function to display the leaderboard displaying scores of everyone who's played the game. Incorporate this file into the main.py game file to enable this functionality.

# To connect to MySQL database, install mysql-connector-python using pip
import mysql.connector

# Before game starts, get name of player (goes before game starts)
name = input('Enter name: ')
print()


# Database functions: (ensure to create a database named 'pygame' with a table named 'SCORES' with columns 'SNO', 'NAME', 'LEVEL', 'SCORE' in MySQL)
def insertrecord_mysql(name, level, FINAL_SCORE):
    try:
        mydb = mysql.connector.connect(host='localhost', user='username', passwd='password', database='pygame')                # Connect to the game database with proper credentials
        mycursor = mydb.cursor()
        mycursor.execute("SELECT MAX(SNO) FROM SCORES")
        myrecords = mycursor.fetchall()
        
        for x in myrecords:
            new_SNo = x[0] + 1

        myquery = "INSERT INTO SCORES VALUES(%s, %s, %s, %s)"
        mydata = (new_SNo, name, level, FINAL_SCORE)
        mycursor.execute(myquery, mydata)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mydb.close()

def leaderboard():
    check = input('Enter 0 to see leaderboard ')               # trigger to display leaderboard (currently CLI, can be changed to a button press in the game) 
    print()
    if check == '0':
        mydb = mysql.connector.connect(host='localhost', user='username', passwd='password', database='pygame')
        mycursor = mydb.cursor()
        mycursor.execute("SHOW COLUMNS FROM SCORES")
        mycolumns = mycursor.fetchall()
        for x in mycolumns:
            print(x[0], end=' ')
        print()
        mycursor.execute("SELECT * FROM SCORES ORDER BY SCORE DESC")
        myrecords = mycursor.fetchall()
        for y in myrecords:
            print(y)


# When game ends, handle database and leaderboard (goes after game ends)
insertrecord_mysql(name, level, FINAL_SCORE)                     # Insert record into database      # level and FINAL_SCORE are game variables
leaderboard()                                                    # Display leaderboard
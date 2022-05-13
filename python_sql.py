import psycopg2 as pg2
secret='pass'
#Connect with SQL database
conn=pg2.connect(database='dvdrental',user='postgres',password=secret) 
#Retrieve the Cursor as variable (Control structure enablin traverse over the records in a database. Iterator for SQL data retrieval.)
cur=conn.cursor()
# Executing SQL queries from Python
cur.execute('SELECT * FROM payment')
# Return row of data - returns the first row of data as a list of tuple items
cur.fetchone()
# Return row of data - returns the first 10 rows of data as a list of tuple items
cur.fetchmany(10)
# Return row of data - returns the all rows of data as a list of tuple items
cur.fetchall()
# Create a data variable
data=cur.fetchall(10)
# Tuple unpack a specific item
data[0]
# Closing connection
conn.close()
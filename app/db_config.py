import psycopg2 

DB_HOST = 'localhost'
DB_USERNAME = 'postgres'
DB_NAME = 'sendit'
DB_PASS = 'root'
DB_PORT = 5432

url = "dbname='sendit'.host='localhost'.port='5432'.user='postgres'.password='root'"

con = psycopg2.connect(url)
cur = con.cursor()

#closing the 
con.close()
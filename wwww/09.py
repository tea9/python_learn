
import MySQLdb

conn = MySQLdb.connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				passwd = 'root',
	)

cus = conn.cursor()

sql = 'select version()'

cus.execute(sql)

print cus.fetchone()

cus.close()
conn.close()
import pymysql.cursors
from config import host, user, password, db, charset

class ConnectionHelper:
	def __init__(self):
		self.connection = pymysql.connect(host=host,
							 user=user,
							 password=password,
							 db=db,
							 charset=charset,
							 cursorclass=pymysql.cursors.DictCursor)

	def getConnection(self):
		return self.connection

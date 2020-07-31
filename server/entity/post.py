from helpers.connection_helper import ConnectionHelper

class Post():
	def all():
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM `post`"
			cursor.execute(sql)
			result = cursor.fetchall()
			connection.close()
			return result

	def create(title, body):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO `post` (`title`, `body`) VALUES (%s, %s)"
			cursor.execute(sql, (title, body))
			connection.commit()
			sql = "SELECT * FROM `post` WHERE `id` = %s"
			cursor.execute(sql, (cursor.lastrowid))
			result = cursor.fetchone()
			connection.close()
			return result

	def getById(id):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM `post` WHERE `id` = %s"
			cursor.execute(sql, (id))
			result = cursor.fetchone()
			connection.close()
			return result

	def deleteById(id):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = " DELETE FROM `post` WHERE `id` = %s"
			cursor.execute(sql,(id))
			connection.commit()
			connection.close();
			return ({'message':'post removed'})

	def updateById(id,title,body):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "UPDATE `post` SET `title` = %s, `body` = %s WHERE `id` = %s"
			cursor.execute(sql,(title, body, id))
			connection.commit()
			connection.close()
			return ({'message': 'post updated'})




		
	
		
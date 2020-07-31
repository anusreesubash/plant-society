from flask_restful import Resource
from entity.post import Post
from flask import request

class PostController(Resource):
	def get(self, id):
		return Post.getById(id)

	def delete(self, id):
		return Post.deleteById(id)

	def put(self, id):
		data = request.get_json()
		title = data['title']
		body = data['body']
		return Post.updateById(id,title,body)

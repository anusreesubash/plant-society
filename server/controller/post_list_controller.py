from flask_restful import Resource
from flask import request
from entity.post import Post

class PostListController(Resource):
	def get(self):
		return Post.all()

	def post(self):
		data = request.get_json()
		title = data['title']
		body = data['body']
		return Post.create(title, body)
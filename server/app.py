from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controller.post_list_controller import PostListController
from controller.post_controller import PostController


app = Flask(__name__)
CORS(app)
api = Api(app) 

api.add_resource(PostListController, '/api/post')
api.add_resource(PostController, '/api/post/<id>')

app.run(port=5000, debug=True)
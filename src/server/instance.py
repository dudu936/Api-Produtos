from flask import Flask
from flask_restful import Api
from src.configs.settings import DEBUG

class Server:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def create_routes(self):
        pass
    
    def run(self):
        self.app.run(debug=DEBUG)

server = Server()
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

quote_put_args = reqparse.RequestParser()
quote_put_args.add_argument("author", type=str, help="name of author")
quote_put_args.add_argument("quote", type=str, help="quote of the author")

quotes = {}

class Quote(Resource):
    def get(self, quote_id):
        return quotes[quote_id]

    def put(self, quote_id):    
        return

api.add_resource(Quote, "/quote/<int:quote_id>")
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

quote_put_args = reqparse.RequestParser()
quote_put_args.add_argument("author", type=str, help="name of author", required=True)
quote_put_args.add_argument("quote", type=str, help="quote of the author", required=True)

quotes = {}

class Quote(Resource):
    def get(self, quote_id):
        return quotes[quote_id]

    def put(self, quote_id):
        args = quote_put_args.parse_args()
        quotes[quote_id] = args
        return quotes[quote_id], 201

api.add_resource(Quote, "/quote/<int:quote_id>")
if __name__ == "__main__":
    app.run(debug=True)
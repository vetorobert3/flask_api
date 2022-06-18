from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class QuoteModel(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(144), nullable=False)
    quote = db.Column(db.String(144), nullable=False)

    def __repr__(self):
        return f"Quote(author = {author}, quote = {quote})"

quote_put_args = reqparse.RequestParser()
quote_put_args.add_argument("author", type=str, help="name of author")
quote_put_args.add_argument("quote", type=str, help="quote of the author")

quotes = {}

def abort_if_quote_id_doesnt_exist(quote_id):
    if quote_id not in quotes:
        abort(404, message="Could not find quote...")

def abort_if_quote_exists(quote_id):
    if quote_id in quotes:
        abort(409, message="Quote already exists with that id...")

class Quote(Resource):
    def get(self, quote_id):
        abort_if_quote_id_doesnt_exist(quote_id)
        return quotes[quote_id]

    def put(self, quote_id):
        abort_if_quote_exists(quote_id)
        args = quote_put_args.parse_args()
        quotes[quote_id] = args
        return quotes[quote_id], 201

    def delete(self, quote_id):
        abort_if_quote_id_doesnt_exist(quote_id)
        del quotes[quote_id]
        return "", 204

api.add_resource(Quote, "/quote/<int:quote_id>")
if __name__ == "__main__":
    app.run(debug=True)
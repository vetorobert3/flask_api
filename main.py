from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
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
quote_put_args.add_argument("author", type=str, help="name of author", required=True)
quote_put_args.add_argument("quote", type=str, help="quote of the author", required=True)

quote_update_args = reqparse.RequestParser()
quote_update_args.add_argument("author", type=str, help="name of author")
quote_update_args.add_argument("quote", type=str, help="quote of the author")

resource_fields = {
    'id': fields.Integer,
    'author': fields.String,
    'quote': fields.String
}

class Quote(Resource):
    @marshal_with(resource_fields)
    def get(self, quote_id):
        result = QuoteModel.query.filter_by(id=quote_id).first()
        if not result:
            abort(404, message="Could not find quote with that id...")
        return result

    @marshal_with(resource_fields)
    def put(self, quote_id):
        args = quote_put_args.parse_args()
        result = QuoteModel.query.filter_by(id=quote_id).first()
        if result:
            abort(409, message="Quote id taken...")

        quote = QuoteModel(id=quote_id, author=args['author'], quote=args['quote']) 
        db.session.add(quote)
        db.session.commit()
        return quote, 201

    @marshal_with(resource_fields)
    def patch(self, quote_id):
        args = quote_update_args.parse_args()
        result = QuoteModel.query.filter_by(id=quote_id).first()
        if not result:
            abort(404, message="Quote doesn't exist, cannot update...")
        
        if args["author"]:
            result.author = args['author']
        if args["quote"]:
            result.quote = args["quote"]

        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def delete(self, quote_id):
        result = QuoteModel.query.filter_by(id=quote_id).first()
        if not result:
            abort(404, message="Could not find quote with that id...")
        if result:
            db.session.delete(result)
            db.session.commit()
        return "Quote has been deleted"

api.add_resource(Quote, "/quote/<int:quote_id>")
if __name__ == "__main__":
    app.run(debug=True)
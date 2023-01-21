from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

mylist = {}


@api.route('/<string:list_id>')
class List(Resource):
    def get(self, list_id):
        return {list_id: mylist[list_id]}

    def put(self, list_id):
        mylist[list_id] = request.form['data']
        return {list_id: mylist[list_id]}


if __name__ == '__main__':
    app.run(debug=True)

import wikipedia as wiki
from flask import Flask, jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

wiki.set_lang('en')

class Generate(Resource):

    def get(self):
        page = wiki.page(wiki.random(pages=1))
        return jsonify(title=page.title,images=page.images,summary=page.summary)

api.add_resource(Generate,'/getData')

if __name__ == '__main__':
    app.run()

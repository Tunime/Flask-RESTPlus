from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        myList=[1,2,3,4,5,6]
        return myList

if __name__ == '__main__':
    app.run(debug=True)
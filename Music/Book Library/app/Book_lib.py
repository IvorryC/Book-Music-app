from flask import Flask 
from flask_restful import Api
from flask_jwt import JWT
# its an API now
from security import authenticate, identity
from users import UserRegister 
from books import MT_Bookshelf, KT_Bookshelf, BookList

app = Flask(__name__)
app.secret_key = 'DontTestMe'
api = Api(app)

jwt = JWT(app, authenticate, identity) # Auth

api.add_resource(MT_Bookshelf, '/book/<string:name>')
api.add_resource(KT_Bookshelf, '/book/<string:name>')
api.add_resource(BookList, '/books')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
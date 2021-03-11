import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password 

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        curser = connection.curser()

        query = "SELECT * FROM users WHERE username=?"
        result = curser.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None 

        connection.close()
        return username

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        curser = connection.curser()

        query = "SELECT * FROM users WHERE id=?"
        result = curser.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user 

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
    type=str,
    required=True,
    help="You cannot leave this blank."
    )
    parser.add_argument('username', 
    type=str,
    required=True,
    help="You cannot leave this blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSER INTO users VALUE (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password'],))

        connection.commit()
        connection.close()

        return{"message": "User created successfully, welcome!"}, 201
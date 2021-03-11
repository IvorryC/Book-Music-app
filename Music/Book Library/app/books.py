import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required




class MT_Bookshelf(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pages',
    type=float,
    required=True,
    help="This field is blank... whoops."
    )
    
    @jwt_required()
    def get(self, name):
        book = self.find_by_name(name)
        if book:
            return book
        return {"message": 'Book not found'}, 200 if book else 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.curser()

        query = "SELECT * FROM books WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'book': {'name': row[0], 'pages': row[1]}}


    def post(self, name):
        if self.find_by_name(name):
                    return {"Message": "A book with the name '{}' already exists.".format(name)}, 400

        data = MT_Bookshelf.parser.parse_args()

        book = {'name': name, 'pages': data['pages']}
        
        try:
            self.insert(book)
        except:
            return {"message": "An error has eccurred inserting the book."}, 500
        return book, 201

    @classmethod
    def insert(cls, book):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO books VALUES (?, ?)"
        cursor.execute(query, (book['name'], book['pages']))

        connection.commit()
        connection.close()


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM books WHERE name=?"
        cursor.execute(query, name,)

        connection.commit()
        connection.close()

        return {'message': 'Book Deleted.'}

    def put(self, name):
        data = MT_Bookshelf.parse.parse_args()

        book = self.find_by_name(name)
        updated_book = {'name': name, 'price': data['price']}
        
        if book is None:
            try:
                self.insert(updated_book)
            except:
                return {"message": "An error occured inserting the book."}, 500
        else:
            try:
                self.update(updated_book)
            except:
                return {"message": "An error has occured updating the book."}
        return book
      
    
    @classmethod
    def update(cls, book):
        connection = sqlite3.connect('data.db')
        cursor = connection.curser()

        query = "UPDATE books SET pages=? WHERE name=?"
        cursor.execute(query, (book['pages'], book['name']))

        connection.commit()
        connection.close()


class KT_Bookshelf(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pages',
    type=float,
    required=True,
    help="This field is blank... whoops."
    )

    
    @jwt_required()
    def get(self, name):
        book = self.find_by_name(name)
        if book:
            return book
        return {"message": 'Book not found'}, 200 if book else 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.curser()

        query = "SELECT * FROM books WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'book': {'name': row[0], 'pages': row[1]}}


    def post(self, name):
        if self.find_by_name(name):
                    return {"Message": "A book with the name '{}' already exists.".format(name)}, 400

        data = KT_Bookshelf.parser.parse_args()

        book = {'name': name, 'pages': data['pages']}
        
        try:
            self.insert(book)
        except:
            return {"message": "An error has eccurred inserting the book."}, 500
        return book, 201

    @classmethod
    def insert(cls, book):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO books VALUES (?, ?)"
        cursor.execute(query, (book['name'], book['pages']))

        connection.commit()
        connection.close()


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM books WHERE name=?"
        cursor.execute(query, name,)

        connection.commit()
        connection.close()

        return {'message': 'Book Deleted.'}

    def put(self, name):
        data = KT_Bookshelf.parse.parse_args()

        book = self.find_by_name(name)
        updated_book = {'name': name, 'price': data['price']}
        
        if book is None:
            try:
                self.insert(updated_book)
            except:
                return {"message": "An error occured inserting the book."}, 500
        else:
            try:
                self.update(updated_book)
            except:
                return {"message": "An error has occured updating the book."}
        return book
      
    
    @classmethod
    def update(cls, book):
        connection = sqlite3.connect('data.db')
        cursor = connection.curser()

        query = "UPDATE books SET pages=? WHERE name=?"
        cursor.execute(query, (book['pages'], book['name']))

        connection.commit()
        connection.close()
    
    

class BookList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM books"
        result = cursor.execute(query)
        books = []
        for row in result:
            books.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {'books': books}
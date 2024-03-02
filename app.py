from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'}
]

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        return jsonify(books)
    elif request.method == 'POST':
        data = request.json
        new_book = {'id': len(books) + 1, 'title': data['title'], 'author': data['author']}
        books.append(new_book)
        return jsonify({'message': 'Book created successfully'})

@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    if request.method == 'GET':
        return jsonify(book)
    elif request.method == 'PUT':
        data = request.json
        book['title'] = data['title']
        book['author'] = data['author']
        return jsonify({'message': 'Book updated successfully'})
    elif request.method == 'DELETE':
        books.remove(book)
        return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, request, jsonify
from app.models import Library

# Initialize the Library instance
library = Library('app/database.json')

# Blueprint for adding a book
add_book_bp = Blueprint('add_book', __name__)
@add_book_bp.route('/books', methods=['POST'])

def add_book():
    data = request.json
    required_fields = ['title', 'author', 'published_year', 'isbn']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    library.add_book(data)
    return jsonify({'message': 'Book added successfully'}), 201

# Blueprint for listing books
list_books_bp = Blueprint('list_books', __name__)
@list_books_bp.route('/books', methods=['GET'])
def list_books():
    return jsonify(library.list_books())

# Blueprint for searching books
search_books_bp = Blueprint('search_books', __name__)
@search_books_bp.route('/books/search', methods=['GET'])
def search_books():
    filters = request.args.to_dict()
    return jsonify(library.search_books(filters))

# Blueprint for deleting a book
delete_book_bp = Blueprint('delete_book', __name__)
@delete_book_bp.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    if library.delete_book(isbn):
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'error': 'Book not found'}), 404

# Blueprint for updating a book
update_book_bp = Blueprint('update_book', __name__)
@update_book_bp.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    updates = request.json
    book = library.update_book(isbn, updates)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404
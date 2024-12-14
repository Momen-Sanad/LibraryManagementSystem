import json
from typing import List, Dict, Union

# Database management class

class Library:
    def __init__(self, db_path: str):
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.books = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):

            self.books = []
            with open(db_path, 'w') as f:
                json.dump(self.books, f, indent=4)


    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, book: Dict):
        self.books.append(book)
        self.save()

    def list_books(self) -> List[Dict]:
        return self.books

    def search_books(self, filters: Dict) -> List[Dict]:
        results = self.books
        for key, value in filters.items():
            results = [book for book in results if str(book.get(key)).lower() == str(value).lower()]
        return results

    def update_book(self, isbn: str, updates: Dict):
        for book in self.books:
            if book['isbn'] == isbn:
                book.update(updates)
                self.save()
                return book
        return None

    def delete_book(self, isbn: str) -> bool:
        for book in self.books:
            if book['isbn'] == isbn:
                self.books.remove(book)
                self.save()
                return True
        return False
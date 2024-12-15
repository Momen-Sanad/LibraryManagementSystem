# Library Management API

This project is a RESTful API for managing a library's books. It provides endpoints for adding, listing, searching, updating, and deleting books. The API is documented with Swagger and is dockerized for easy deployment.

---

## Features

- Add a new book with details such as title, author, published year, ISBN, and genre.
- List all books in the library.
- Search for books by author, published year, or genre.
- Update book details using its ISBN.
- Delete a book using its ISBN.
- Swagger API documentation for easy testing.

---

## Prerequisites

- [Docker](https://www.docker.com/) installed on your machine.
- [Postman](https://www.postman.com/) for testing the API (optional).

---

## Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/LibraryManagementAPI.git
   cd LibraryManagementAPI

2. **Build the Docker Image**

    docker build -t library-api .

3.  **Run the Docker Container**

    docker run -p 5000:5000 library-api

4. **Access the API**

    Base URL: http://localhost:5000
    Swagger Documentation: http://localhost:5000/api-docs


**API ENDPOINTS**

1. **Add a New Book**

    POST /books

    Request Body:

    {
    "title": "Book Title",
    "author": "Author Name",
    "publishedYear": 2023,
    "isbn": "1234567890123",
    "genre": "Fiction"
    }

2. **List All Books**

    GET /books

    Response:

    [
    {
        "title": "Book Title",
        "author": "Author Name",
        "publishedYear": 2023,
        "isbn": "1234567890123",
        "genre": "Fiction"
    }
    ]

3. **Search for Books**

    GET /books/search

    Query Parameters:

        author (optional)
        publishedYear (optional)
        genre (optional)

    Example: /books/search?author=Author Name&publishedYear=2023&genre=Fiction

4. **Update Book Details**

    PUT /books/{isbn}

    Request Body:

    {
    "title": "Updated Title",
    "author": "Updated Author",
    "publishedYear": 2024,
    "genre": "Non-Fiction"
    }

5. **Delete a Book**

    DELETE /books/{isbn}


**Testing the API**

    Using Postman
        Import the provided Postman collection file (LibraryAPI_Postman_Collection.json).
        Replace the {{base_url}} variable with your API's base URL.

    Using cURL
        Example for adding a new book:

        curl -X POST http://localhost:5000/books -H "Content-Type: application/json" -d '{
          "title": "Book Title",
          "author": "Author Name",
          "publishedYear": 2023,
          "isbn": "1234567890123",
          "genre": "Fiction"
        }'

**Swagger API Documentation**

    Visit http://localhost:5000/api-docs in your browser to view and interact with the API documentation.
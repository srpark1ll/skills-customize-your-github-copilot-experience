# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API with FastAPI to practice defining endpoints, validating request data, and managing resources with standard HTTP methods.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Create a FastAPI application and add a couple of simple routes to get familiar with endpoint functions and the interactive API documentation.

#### Requirements
Completed program should:

- Create a `main.py` file with a FastAPI application instance named `app`.
- Define a `GET /` route that returns a welcome message.
- Define a `GET /health` route that returns a JSON response indicating the API is healthy.
- Run the application with Uvicorn and confirm the routes appear in the `/docs` interface.

### 🛠️ Create and Read Resources

#### Description
Build endpoints for managing a collection of books, using a Pydantic model to validate incoming data and an in-memory list to store books.

#### Requirements
Completed program should:

- Define a `Book` model with required `title` and `author` fields.
- Implement `GET /books` to return the collection of books.
- Implement `POST /books` to validate and add a book, then return the created book.
- Implement `GET /books/{book_id}` to return one book or a `404` response when it does not exist.

### 🛠️ Update and Delete Resources

#### Description
Complete the books API by adding endpoints to update and remove a book by its ID.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update a book's title and author.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return a `404` response when an update or deletion targets a book that does not exist.
- Verify the create, read, update, and delete endpoints using the `/docs` interface.

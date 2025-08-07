# API Documentation

## Book Endpoints

The API provides a set of endpoints for managing `Book` resources. These endpoints are built using Django REST Framework's generic views, which streamline common CRUD operations.

### Permissions

All endpoints use the `IsAuthenticatedOrReadOnly` permission class.
-   **Read Operations (GET)**: Accessible to all users, authenticated or not.
-   **Write Operations (POST, PUT, PATCH, DELETE)**: Restricted to authenticated users only.

### Endpoints

#### `GET /api/books/`

-   **Description**: Retrieves a list of all book instances.
-   **Method**: `GET`
-   **Permissions**: Read-only access for all users.

#### `POST /api/books/`

-   **Description**: Creates a new book instance.
-   **Method**: `POST`
-   **Permissions**: Requires authentication.
-   **Request Body**: A JSON object containing the book data (e.g., `title`, `author`, `publication_date`).

#### `GET /api/books/<int:pk>/`

-   **Description**: Retrieves a single book instance by its ID.
-   **Method**: `GET`
-   **Permissions**: Read-only access for all users.
-   **URL Parameters**:
    -   `pk` (integer): The primary key of the book.

#### `PUT/PATCH /api/books/<int:pk>/`

-   **Description**: Updates a single book instance. `PUT` replaces the entire object, while `PATCH` performs a partial update.
-   **Method**: `PUT` or `PATCH`
-   **Permissions**: Requires authentication.
-   **URL Parameters**:
    -   `pk` (integer): The primary key of the book.
-   **Request Body**: A JSON object with the fields to be updated.

#### `DELETE /api/books/<int:pk>/`

-   **Description**: Deletes a single book instance.
-   **Method**: `DELETE`
-   **Permissions**: Requires authentication.
-   **URL Parameters**:
    -   `pk` (integer): The primary key of the book.
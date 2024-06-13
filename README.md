# Ice Cream Parlor Application

This is a simple Python application for managing an ice cream parlor cafe using SQLite.

## Features

- Manage seasonal flavor offerings
- Manage ingredient inventory
- Handle customer flavor suggestions and allergy concerns
- Maintain a cart of favorite products
- Search & filter offerings
- Add allergens

## Setup and Run

### Prerequisites

- Docker
- Python 3.9

### Steps to run the application

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd ice_cream_parlor
    ```

2. Initialize the database:
    ```sh
    python app/database.py
    ```

3. Run the application:
    ```sh
    python app/main.py
    ```

4. The application will be available at `http://127.0.0.1:5000`.

### Docker

1. Build the Docker image:
    ```sh
    docker build -t ice_cream_parlor .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:5000 ice_cream_parlor
    ```

### API Endpoints

- `GET /flavors` - Get all seasonal flavors
- `POST /flavors` - Add a new flavor
- `GET /cart` - Get all items in the cart
- `POST /cart` - Add an item to the cart
- `GET /allergens` - Get all allergens
- `POST /allergens` - Add a new allergen

## Testing

1. Add a flavor:
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"name":"Vanilla","description":"Classic vanilla flavor","availability":"Summer"}' http://127.0.0.1:5000/flavors.html
    ```

2. Get all flavors:
    ```sh
    curl http://127.0.0.1:5000/flavors
    ```

3. Add an item to the cart:
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"product_name":"Vanilla Ice Cream"}' http://127.0.0.1:5000/cart.html
    ```

4. Get all items in the cart:
    ```sh
    curl http://127.0.0.1:5000/cart
    ```

5. Add an allergen:
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"name":"Peanuts"}' http://127.0.0.1:5000/allergens.html
    
    ```

6. Get all allergens:
    ```sh
    curl http://127.0.0.1:5000/allergens
    ```

## License

This project is licensed under the MIT License.

# Movie Recommendations

## Dev Container

**If it asks you to choose a workspace, please choose "app/" as your Workspace.**

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/spacecupcake1/Modul347)

The Movie API is a web service built with FastAPI that allows users to perform CRUD (Create, Read, Update, Delete) operations on a collection of movies. It provides endpoints to manage movies, including creating new movies, retrieving movie details, updating existing movies, and deleting movies from the database.

## Features

- **Create Movie**: Add a new movie to the database by providing details such as title, director, year, and description.
- **Get Movie**: Retrieve details of a specific movie by its unique identifier.
- **Update Movie**: Update the details of an existing movie, such as its title, director, year, or description.
- **Delete Movie**: Remove a movie from the database using its unique identifier.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Docker**: A containerization platform for packaging, distributing, and running applications.

## Installation and Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/spacecupcake1/Modul347.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd movierec
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Docker Containers**:

    ```bash
    docker-compose up -d --build
    ```

    This will start the FastAPI application along with the MySQL database and PHPMyAdmin tool. You can access the application at `http://localhost:8000` by default, and PHPMyAdmin at `http://localhost:8085`.

## Example Usage

The `example_usage` function in `main.py` demonstrates how to use the repository functions to interact with the database. You can uncomment and modify the function as needed to test the CRUD operations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request on GitHub.
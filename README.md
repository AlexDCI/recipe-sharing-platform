# Project Name

This project is a web application built using Django and Django REST Framework.

## Requirements

The project requires the following dependencies:

- Django
- Django REST Framework
- python-decouple (used for managing environment variables)

## Installation

1. Clone the repository and navigate into the project directory.
2. Set up a Python virtual environment.
3. Install dependencies listed in the `requirements.txt` file.
4. Configure environment variables in a `.env` file. The `SECRET_KEY` and other sensitive settings should be stored in this file.
   - The `.env` file is not tracked by Git for security purposes.
5. Apply database migrations using Django's migration system.
6. Start the development server.

## Handling the SECRET_KEY

The `SECRET_KEY` is stored securely in a `.env` file using `python-decouple`. It is not hardcoded in the `settings.py` file to enhance security. Make sure to add the `.env` file to your `.gitignore` file so it is not tracked by version control.

## License

Include any licensing information for the project.

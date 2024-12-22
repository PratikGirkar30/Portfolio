from app import app  # Import the Flask app instance from the main app file
web: gunicorn app:app

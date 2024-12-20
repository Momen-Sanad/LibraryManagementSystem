from flask import Flask
from app import create_app  # Ensure correct import from __init__.py

# Initialize the Flask application
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

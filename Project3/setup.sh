#!/bin/bash

# Activate your virtual environment if you have one
# Uncomment and replace with your virtual environment's path if needed
# source /path/to/your/venv/bin/activate

echo "Installing Python packages for Flask web application..."

# Install Flask
pip install Flask

# Install Flask extensions and other useful packages
# SQLAlchemy for database management
pip install SQLAlchemy

# Flask-Migrate for handling SQLAlchemy database migrations
pip install Flask-Migrate

# Flask-Login for handling user sessions
pip install Flask-Login

# Flask-WTF for form handling
pip install Flask-WTF

# Requests for making HTTP requests
pip install requests

echo "Setup complete."

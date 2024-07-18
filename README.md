Weather Application 
Overview:
The weather application is a Flask-based web application designed to provide users with real-time weather information for any city. It leverages the OpenWeatherMap API to fetch current weather data such as temperature and weather description.

Key Features:
Flask Web Application: Allows users to input a city name and retrieves corresponding weather details.

OpenWeatherMap Integration: Utilizes the OpenWeatherMap API to fetch weather data based on user inputs.

Docker Containerization: Implements Docker for containerization, ensuring consistent deployment across different environments.

Jenkins Automation: Integrates Jenkins for CI/CD, automating the build, test, and deployment processes.

Usage:
Users input a city name via the web interface.

The application sends a request to the OpenWeatherMap API to fetch weather data for the specified city.

Weather information (temperature, weather description) is displayed to the user.

Implementation:
Flask Framework: Handles routing and requests, rendering HTML templates for user interaction.

Requests Module: Facilitates HTTP requests to the OpenWeatherMap API for data retrieval.

Dockerfile: Defines dependencies and instructions for building the application image.

Jenkins Pipeline: Orchestrates the CI/CD process, ensuring automated deployment and integration testing.
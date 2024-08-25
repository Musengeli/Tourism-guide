# Tourism Guide Application

## Overview

This project is a Tourism Guide application designed to provide users with information about various destinations around the world. The application allows users to view and compare destinations, search and filter destinations, and implement pagination for easy navigation.

## Features

- **Destination Information**: View detailed information about various destinations.
- **Comparison**: Compare destinations using UI elements such as score cards and graphs.
- **Search & Filter**: Quickly find and filter destinations.
- **Pagination**: Browse through destinations with pagination (10 destinations per page).

## API Endpoints

- **List Destinations**: [https://freetestapi.com/api/v1/destinations](https://freetestapi.com/api/v1/destinations)
- **Get Specific Destination**: [https://freetestapi.com/api/v1/destinations/1](https://freetestapi.com/api/v1/destinations/1)
- **Paginate Destinations**: [https://freetestapi.com/api/v1/destinations?limit=5](https://freetestapi.com/api/v1/destinations?limit=5)
- **Search Destinations**: [https://freetestapi.com/api/v1/destinations?search=[query]](https://freetestapi.com/api/v1/destinations?search=[query])
- **Sort Destinations**: [https://freetestapi.com/api/v1/destinations?sort=name&order=dec](https://freetestapi.com/api/v1/destinations?sort=name&order=dec)

## Prerequisites

- Python 3.9 or later
- Virtual Environment (recommended)
- Flask
- Flask-SQLAlchemy

## Running
python -m venv venv
venv\Scripts\activate
Install dependencies : pip install -r requirements.txt
Run the application : python main.py

## Running using docker
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
docker-compose up





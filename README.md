# NeoTour

NeoTour is a Django Rest Framework project for booking tours.

## Installation

1. Clone the repository:
https://github.com/Kilotas/NeobisTour.git

2. Navigate to the project directory:
cd NeoTour
3. Install dependencies:
pip install -r requirments.txt
4. Apply migrations:
python manage.py migrate
5. Run the development server:
python3 manage.py runserver

## Usage

- Access the admin panel at http://localhost:8000/admin/ to manage tours, categories, reviews, and bookings.
- Use the API endpoints at http://localhost:8000/api/ to interact with the application programmatically.

## API Endpoints

- `/api/tours/`: Get a list of all tours or create a new tour.
- `/api/tours/{id}/`: Get details of a specific tour, update, or delete it.
- `/api/categories/`: Get a list of all categories or create a new category.
- `/api/categories/{id}/`: Get details of a specific category, update, or delete it.
- `/api/reviews/`: Get a list of all reviews or create a new review.
- `/api/reviews/{id}/`: Get details of a specific review, update, or delete it.
- `/api/bookings/`: Get a list of all bookings or create a new booking.
- `/api/bookings/{id}/`: Get details of a specific booking, update, or delete it.

## Authentication

- Use the built-in Django Rest Framework authentication endpoints at http://localhost:8000/api-auth/ for user authentication.

## API Schema and Documentation

- `/api/schema/`: Get the OpenAPI schema for the API.
- `/api/docs/`: Get the Swagger documentation for the API.

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.


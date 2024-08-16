# Movie Listing API

## Project Overview

The goal of this capstone project is to develop a movie listing API using FastAPI. This API will provide functionalities to list movies, view detailed information about them, rate them, and add comments. The application is secured using JWT (JSON Web Tokens) to ensure that only the user who listed a movie can update or delete it. The application will be hosted on a cloud platform.

## Requirements

- **Language & Framework:** Python using FastAPI
- **Authentication:** JWT for securing endpoints
- **Database:** Any SQL or NoSQL database
- **Testing:** Include unit tests for the API endpoints
- **Documentation:** API documentation using OpenAPI/Swagger
- **Logging:** Log important details of your application
- **Deployment:** Deploy your application on a cloud server of your choice

## Features

### User Authentication

- **User Registration:** Allows new users to create an account.
- **User Login:** Authenticates users and provides a JWT token.
- **JWT Token Generation:** Securely generates tokens for authenticated access.

### Movie Listing

- **View a Movie:** Publicly accessible endpoint to view details of a specific movie.
- **Add a Movie:** Authenticated endpoint to add a new movie to the listing.
- **View All Movies:** Publicly accessible endpoint to view all listed movies.
- **Edit a Movie:** Allows only the user who listed the movie to update it.
- **Delete a Movie:** Allows only the user who listed the movie to delete it.

### Movie Rating

- **Rate a Movie:** Authenticated endpoint to rate a movie.
- **Get Ratings for a Movie:** Publicly accessible endpoint to view ratings for a movie.

### Comments

- **Add a Comment to a Movie:** Authenticated endpoint to add a comment to a movie.
- **View Comments for a Movie:** Publicly accessible endpoint to view all comments for a movie.
- **Add a Reply to a Comment:** Authenticated endpoint to add nested comments or replies to an existing comment.


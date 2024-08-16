The goal of this capstone project is to develop a movie listing API using FastAPI. The API will allow users to perform various operations related to movies, including listing, viewing, rating, and commenting on movies. The application will be secured using JWT (JSON Web Tokens), ensuring that only the user who listed a movie can edit or delete it. The application is designed to be hosted on a cloud platform.

Features
User Authentication:
User Registration: Users can sign up for an account.
User Login: Users can log in with their credentials.
JWT Token Generation: After logging in, users receive a JWT token for authenticating subsequent requests.
Movie Listing:
View All Movies: Public access to view a list of all movies.
View a Movie: Public access to view the details of a specific movie.
Add a Movie: Authenticated users can add a new movie to the list.
Edit a Movie: Only the user who listed a movie can edit it.
Delete a Movie: Only the user who listed a movie can delete it.
Movie Rating:
Rate a Movie: Authenticated users can rate movies.
View Movie Ratings: Public access to view ratings for a specific movie.
Comments:
Add a Comment to a Movie: Authenticated users can comment on movies.
View Comments for a Movie: Public access to view comments on a specific movie.
Add a Comment to a Comment (Nested Comments): Authenticated users can reply to existing comments, creating nested comments.
Requirements
Language & Framework: Python using FastAPI
Authentication: JWT for securing endpoints
Database: Any SQL or NoSQL database
Testing: Unit tests for API endpoints
Documentation: API documentation using OpenAPI/Swagger
Logging: Log important details of the application
Deployment: Deploy the application on a cloud server of your choice
Project Structure
/app: Contains the FastAPI application code.
/app/models: Defines the database models.
/app/schemas: Defines the Pydantic models used for data validation.
/app/crud: Contains the CRUD (Create, Read, Update, Delete) operations.
/app/auth: Handles authentication and authorization logic.
/app/routers: Contains the API routes for different endpoints.
/tests: Unit tests for the application.
/requirements.txt: Lists the dependencies required for the project.
/README.md: Provides an overview and instructions for the project
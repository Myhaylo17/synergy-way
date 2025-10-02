SynergyWay is a full-stack web application that integrates a Django backend with a React frontend. 
The project is designed to demonstrate clean architecture, modular development, and modern deployment practices using Docker. 
It is structured to support scalability, maintainability, and separation of concerns between the client and server.
The backend is built with Django and Django REST Framework, providing a robust API layer for data exchange. 
It includes modular apps, environment-based configuration, and follows best practices for RESTful design. The backend handles business logic, 
database interactions, and serves as the core of the application’s functionality.
The frontend is developed using React, organized into src and public directories. 
It communicates with the Django API via HTTP requests, rendering dynamic content and providing a responsive user interface. React components are structured for reusability and clarity, and the project uses npm for dependency management and build automation.
Both frontend and backend are containerized using Docker. The project includes a docker-compose.yml file that orchestrates services, 
allowing for easy local development and deployment. Each service runs in its own container, ensuring isolation and consistency across environments.
Environment variables are managed through .env files, keeping sensitive data out of the codebase. The project also includes
a requirements.txt for Python dependencies and a package.json for JavaScript packages.

The directory structure is clean and intuitive, with separate folders for frontend and backend logic. 
The backend resides in the testtask folder, while the frontend lives in the frontend folder. 
This separation allows developers to work independently on each layer while maintaining integration through API calls.
The application is ideal for demonstrating microservice architecture principles, API-first development, and frontend-backend decoupling.
It can be extended with additional features, such as authentication, database models, and advanced UI components.


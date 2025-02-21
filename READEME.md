## Container-Based Web Application for Super Bowl Article Aggregation

This project is a container-based web application for aggregating Super Bowl articles. It consists of a client-side application built with Next.js and a server-side application built with Flask.

### Prerequisites

- Docker
- Docker Compose

### Setup Instructions

1.  **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd superBowl
    ```

2.  **Set your GNEWS API key:**

    ```sh
    GNEWS=<your-gnews-api-key>
    ```

    docker-compose up --build
    Access the Applications:

    `Client application: http://localhost:3000`

    `Server application: http://localhost:5000`

**Project Structure**

    - client: Contains the Next.js client application.
    - server: Contains the Flask server application.
    - docker-compose.yml: Docker Compose configuration file.

**Client Application**
The client application is built with Next.js and uses Tailwind CSS for styling.

**Development**

- To start the client application in development mode:

  ```bash
      cd apps/client
      npm install
      npm run dev
  ```

**Development**

- To start the server application in development mode:
  ```bash
  cd apps/server
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  flask run
  ```

**Database Migrations**

- To manage database migrations, use Flask-Migrate:

```bash
    cd apps/server
    flask db init
    flask db migrate
    flask db upgrade
```

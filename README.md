# InstagramRedesignApp


# Instagram Clone - Creative Ideas Platform

A full-stack social media platform for sharing creative ideas, built with FastAPI, Turborepo React, and AWS.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker (optional)

### Local Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd instagram-clone

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```
## Run the application
#### Backend: (Terminal 1)
```bash
cd backend
```
```bash
uvicorn apps.server.main:app --reload
```

#### Frontend: (Terminal 2)
```bash
cd frontend
```
```bash
pnpm start
```




## Running Migrations
This application uses Alembic to run migrations to a Prisma PostgreSQL database.

__[Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)__

1. Make a revision/migration version
   
   ```bash
   alembic revision --autogenerate -m "Type Message"
   ```
2. Push Changes
   
    ```bash
    alembic upgrade head
    ```

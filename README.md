# InstagramRedesignApp


# Instagram Clone - Creative Ideas Platform

A full-stack social media platform for sharing creative ideas, built with FastAPI, React, and AWS.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker (optional)

### Local Development
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

# Run the application
# Terminal 1 - Backend
cd backend
uvicorn app.main:app --reload

# Terminal 2 - Frontend  
cd frontend
npm start

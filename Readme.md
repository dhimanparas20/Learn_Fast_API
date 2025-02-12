# 🚀 FastAPI Demo Project

This is a fully functional **FastAPI** demo project that covers essential features like authentication, database integration, background tasks, WebSockets, and more.

## 🔥 Features
✅ Class-Based Views (CBVs)  
✅ RESTful Routes (`GET`, `POST`, `PUT`, `DELETE`)  
✅ SQLAlchemy ORM & Alembic Migrations  
✅ JWT Authentication  
✅ Middleware for Logging  
✅ Background Tasks  
✅ WebSockets Support  
✅ Pydantic for Data Validation  
✅ Automatic API Documentation (Swagger & ReDoc)  
✅ CORS Handling  
✅ Asynchronous Request Handling  

---

## 📂 Project Structure
```
fastapi_demo/
│── main.py                 # Entry point for FastAPI app
│── config.py               # Configuration settings
│── database.py             # Database connection setup
│── models.py               # SQLAlchemy models
│── schemas.py              # Pydantic schemas for request/response
│── dependencies.py         # Dependency injection setup
│── routers/
│   │── auth.py             # Authentication routes (Register/Login)
│   │── users.py            # User CRUD operations
│── middleware.py           # Middleware for logging requests
│── background_tasks.py     # Background task example
│── utils.py                # WebSocket manager
│── requirements.txt        # Required dependencies
│── alembic/                # Alembic migrations
```

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/dhimanparas20/Learn_Fast_API
cd Learn_Fast_API
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🛠️ Database Setup

### **1️⃣ Run Alembic Migrations**
```sh
alembic upgrade head
```
This will create the database tables.

---

## ▶️ Running the FastAPI Application

Start the server with:
```sh
uvicorn main:app --reload
```
🚀 The API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**  

---

## 📄 API Documentation
FastAPI automatically generates interactive API docs:

📌 **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
📌 **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## 🧪 Testing the API

### **1️⃣ Register a User**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/auth/register' \
-H 'Content-Type: application/json' \
-d '{"username": "testuser", "email": "test@example.com", "password": "testpassword"}'
```

### **2️⃣ Login and Get JWT Token**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/auth/login' \
-H 'Content-Type: application/json' \
-d '{"username": "testuser", "password": "testpassword"}'
```

### **3️⃣ Get Users (Requires JWT Token)**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/users/' \
-H 'Authorization: Bearer YOUR_JWT_TOKEN'
```
Replace `YOUR_JWT_TOKEN` with the token received from login.

---

## 🔍 Running Tests

1️⃣ **Install Pytest & HTTPX**
```sh
pip install pytest httpx
```

2️⃣ **Run Tests**
```sh
pytest test_main.py
```

---

## 🎯 Background Tasks Example
Trigger an **email send task** in the background:
```sh
curl -X 'POST' 'http://127.0.0.1:8000/tasks/send-email' \
-H 'Content-Type: application/json' \
-d '{"email": "user@example.com", "message": "Hello from FastAPI!"}'
```

---

## 🔄 WebSockets Test

Connect to the WebSocket:
```python
import asyncio
import websockets

async def test_websocket():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
        await websocket.send("Hello Server!")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(test_websocket())
```

---

## 🛠️ Deployment

To deploy with **Gunicorn**:
```sh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

For **Docker Deployment**:
1️⃣ **Create a `Dockerfile`**
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
2️⃣ **Build & Run**
```sh
docker build -t fastapi-demo .
docker run -p 8000:8000 fastapi-demo
```

---

## 📜 License
This project is **MIT licensed**.

---

## ✨ Contributing
Pull requests are welcome! Feel free to open an issue for discussions.

---
### 🚀 **Happy Coding with FastAPI!** 🚀
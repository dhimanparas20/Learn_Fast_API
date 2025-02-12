from fastapi import FastAPI
from routers import auth, users
import background_tasks
from middleware import log_requests

app = FastAPI(title="FastAPI Demo")

app.middleware("http")(log_requests)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(background_tasks.router)

@app.get("/")
async def root():
    return {"message": "FastAPI is awesome!"}

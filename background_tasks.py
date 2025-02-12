from fastapi import BackgroundTasks, APIRouter

router = APIRouter(prefix="/tasks", tags=["Background Tasks"])

def send_email(email: str, message: str):
    print(f"Sending email to {email} with message: {message}")

@router.post("/send-email")
async def trigger_email(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"message": "Email will be sent in the background"}

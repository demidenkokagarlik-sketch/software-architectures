from fastapi import FastAPI, HTTPException

app = FastAPI(title="Users Service")

USERS = {
    1: {"id": 1, "email": "user1@example.com"},
    2: {"id": 2, "email": "user2@example.com"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
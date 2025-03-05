import uuid
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(
    title="MLOPS Tarea2",
    description="MLOPS Tarea2",
    version="0.0.1",
)

users_db = {
        "70": {
            "name": "Guissell",
            "email": "<g@gmail",
        }
    }

@app.get("/get-users/{user_id}", tags=["get-user"])
async def get_user(user_id: str):
    try:
        user = users_db[user_id]
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"user, {user['name']}, with email {user['email']}"
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
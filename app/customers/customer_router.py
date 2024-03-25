from fastapi import APIRouter

router = APIRouter()

@router.get("", status_code=200)
async def customer():
    return {
        "id": "1",
        "full_name": "John Doe"
    }
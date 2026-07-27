from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.statistics_chart_service import buat_data_chart


router = APIRouter(
    prefix="/statistics-chart",
    tags=["Statistics Chart"],
)


class ChartRequest(BaseModel):
    data: list[dict]


@router.post("/")
def generate_statistics_chart(request: ChartRequest):
    try:
        return {
            "success": True,
            "chart_data": buat_data_chart(request.data),
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Gagal membuat data chart: {error}",
        )
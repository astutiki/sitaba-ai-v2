from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Pesan pertanyaan dari pengguna"
    )


class LoginRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Username pengguna"
    )

    password: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Password pengguna"
    )


class ExportRequest(BaseModel):
    format: str = Field(
        ...,
        description="Format export: pdf atau jpg"
    )
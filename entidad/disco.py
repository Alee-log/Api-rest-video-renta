from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# Clase Discos
class Discos(BaseModel):
    codigo: str = Field(..., min_length=8, max_length=8, description="Código de identificación única del artículo")
    name: str = Field(..., min_length=8, max_length=64, description="Título o nombre de la película")
    sinopsis: str = Field(..., min_length=8, max_length=256, description="Sinopsis de la película")
    director: str = Field(..., min_length=8, max_length=64, description="Nombre del director")
    duracion: int = Field(..., ge=1, le=300, description="Duración de la película en minutos")
    tamaño: int = Field(..., ge=1, le=5000, description="Tamaño de la película en MB")
    precio_venta: int = Field(..., ge=100, le=500, description="Precio venta de la película en digital")
    precio_renta: int = Field(..., ge=50, le=70, description="Precio renta de la película")

    class Config:
        json_schema_extra = {
            "example": {
                "codigo": "cod-100",
                "name": "Lilo y Stitch",
                "sinopsis": "Una niña solitaria llamada Lilo adopta a Stitch un revoltoso perro alienígena",
                "director": "Dean DeBlois",
                "duracion": 85,
                "tamaño": 1500,
                "precio_venta": 400,
                "precio_renta": 70
            }
        }
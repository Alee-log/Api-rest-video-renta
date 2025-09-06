from typing import Optional
from pip._internal.utils import datetime
from pydantic import BaseModel, EmailStr, Field

class Video(BaseModel):
    codigo: str = Field(..., min_length=8, max_length=8, description="Código de identificación única del artículo")
    titulo: str = Field(..., min_length=1, max_length=100, description="Título o nombre de la película")
    artistas: list[str] = Field(..., description="Lista de artistas principales")
    clasificacion: str = Field(..., description="Clasificación del video (PG-13, R, etc.)")
    genero: str = Field(..., description="Género del video (Música, Acción, Drama, etc.)")
    portada: Optional[str] = Field(None, description="URL de la portada del video")
    sinopsis: str = Field(..., min_length=10, max_length=500, description="Sinopsis de la película")
    director: str = Field(..., min_length=1, max_length=100, description="Nombre del director")
    duracion: int = Field(..., ge=1, le=300, description="Duración de la película en minutos")
    tamanio_mb: int = Field(..., ge=100, le=5000, description="Tamaño del video en MB")
    precio_venta: float = Field(..., ge=0, description="Precio de venta del video")
    precio_alquiler: float = Field(..., ge=0, description="Precio de alquiler del video")
    fecha_agregado: datetime = Field(default_factory=datetime.now, description="Fecha de agregado al catálogo")

    class Config:
        json_schema_extra = {
            "example": {
                "codigo": "VID-1001",
                "titulo": "Lilo y Stitch",
                "artistas": ["Daveigh Chase", "Chris Sanders", "Tia Carrere"],
                "clasificacion": "PG",
                "genero": "Animación",
                "portada": "https://ejemplo.com/lilo-stitch.jpg",
                "sinopsis": "Una niña solitaria llamada Lilo adopta a Stitch, un revoltoso perro alienígena",
                "director": "Dean DeBlois, Chris Sanders",
                "duracion": 85,
                "tamanio_mb": 1500,
                "precio_venta": 300,
                "precio_alquiler": 150
            }
        }
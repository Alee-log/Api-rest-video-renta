from pip._internal.utils import datetime
from pydantic import BaseModel, EmailStr, Field
# Clase Usuario
class Usuario(BaseModel):
    id: int = Field(..., description="ID único del usuario")
    nombre: str = Field(..., min_length=1, max_length=50, description="Nombre del usuario")
    apellido: str = Field(..., min_length=1, max_length=50, description="Apellido del usuario")
    email: EmailStr = Field(..., description="Correo electrónico del usuario")
    password: str = Field(..., min_length=8, description="Contraseña del usuario (mínimo 8 caracteres)")
    pregunta_validacion: str = Field(..., description="Pregunta de validación para recuperación")
    respuesta_validacion: str = Field(..., description="Respuesta de validación")
    fecha_registro: datetime = Field(default_factory= datetime.now, description="Fecha de registro del usuario")
    activo: bool = Field(default=True, description="Estado de la cuenta del usuario")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "María",
                "apellido": "González",
                "email": "maria.gonzalez@email.com",
                "password": "passwordSegura123",
                "pregunta_validacion": "¿Cuál es el nombre de tu primera mascota?",
                "respuesta_validacion": "Firulais",
                "fecha_registro": "2023-10-15T14:22:00",
                "activo": True
            }
        }




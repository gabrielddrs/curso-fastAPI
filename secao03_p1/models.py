from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')

        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras')
    
        return value
    
    @validator('aulas')
    def validar_aulas(cls, value):
        
        if value < 10:
           raise ValueError('O número de aulas deve ser maior ou igual 10')

        return value

    @validator('horas')
    def validar_horas(cls, value):
        
        if value < 10:
            raise ValueError('A quantidade de horas deve ser maior ou igual 10')

        return value

cursos =[
    Curso(id=1, titulo="APIs Modernas e Assícronas com Python", aulas=71, horas=16),
    Curso(id=2, titulo="Visao Computacional: O Guia Completo", aulas=239, horas=25)
]


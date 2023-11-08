from typing import Optional, List, Any, Dict
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response, Path, Depends
from time import sleep
from models import Curso, cursos

def fake_db():
    try:
        print("Abrindo conexão com o banco de dados")
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados')
        sleep(1)

#Inicializando o APP
app = FastAPI(
    title="API de Cursos",
    version='0.0.1',
    description='Estudo de funcionamento de uma API'
)

#Endpoint para buscar todos os cursos
@app.get(
    '/cursos', 
    description="Retorna todos os cursos cadastrados ou retorna um dicionário vazio", 
    summary="Retorna todos os cursos",
    response_model=List[Curso],
    response_description='Cursos encontrados com sucesso'
)
async def get_cursos(db: Any=Depends(fake_db)):
    return cursos

#Endpoint para buscar um curso específico
@app.get(
    '/cursos/{curso_id}',
    description="Retorna um curso em específico ou retorna uma exceção HTTP 404",
    summary="Retornando UM curso",
    response_model=Curso,
    response_description="Curso encontrado com sucesso"
)
#Função com PATH parameters
async def get_curso(curso_id: int, db: Any=Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado. Tente outro curso")

#Endpoint para inserir um curso
@app.post(
    '/cursos', 
    status_code=status.HTTP_201_CREATED,
    description="Faz a inserção de um curso ou retorna um erro de body",
    summary="Inserindo UM curso",
    response_model=Curso,
    response_description="Curso criado com sucesso"
)
async def post_curso(curso: Curso, db: Any=Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso

#Endpoint para atualizar um curso
@app.put(
    '/cursos/{curso_id}',
    description="Atualiza um curso existente ou retorna uma exceção HTTP 404",
    summary="Atualiza UM curso",
    response_model=Curso,
    response_description="Curso atualizado com sucesso"
)
async def put_curso(curso_id: int, curso: Curso, db: Any=Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existe curso com este ID. Tente outro")

#Endpoint para deletar um curso   
@app.delete(
    '/cursos/{curso_id}',
    description="Deleta um curso ou retorna uma exceção HTTP 404",
    summary="Deleta UM curso",
    response_model=Curso,
    response_description="Curso deletado com sucesso"
)
async def delete_curso(curso_id: int, db: Any=Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso {curso_id} não existente. Tente outro.")



#Função para rodar o servidor
if __name__ == '__main__':
    import uvicorn

    #Rodando o servidor
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)


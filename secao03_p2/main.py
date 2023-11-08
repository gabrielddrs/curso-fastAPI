from fastapi import FastAPI
from routes import curso_router
from routes import usuario_router

app = FastAPI()
#Incluindo as rotas
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])


#Função para rodar o servidor
if __name__ == '__main__':
    import uvicorn

    #Rodando o servidor
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

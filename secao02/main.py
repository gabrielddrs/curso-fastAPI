from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def msg():
    return {"Mensagem": "Olá, bem-vindo"}






if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)

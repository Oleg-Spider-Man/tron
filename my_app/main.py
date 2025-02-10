import uvicorn
from fastapi import FastAPI
from my_app.routers import tron

app = FastAPI(summary="здесь можно написать краткое описание приложения")

app.include_router(tron.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

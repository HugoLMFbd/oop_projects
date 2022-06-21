import uvicorn

from fastapi import FastAPI
from routes import rusty_bikes_routes

app = FastAPI()  # has to be in the global scope.
app.include_router(rusty_bikes_routes)  # hast to be in the global scope.
if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True, host='127.0.0.1', port=8002)

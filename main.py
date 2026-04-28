from fastapi import FastAPI
from routes import users_routes
from db.conn import create_db

app = FastAPI()

create_db()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(users_routes.router)
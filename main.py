from fastapi import FastAPI
from routes import users_routes, tenants_routes, loans_routes, tasks_routes
from db.conn import create_db

app = FastAPI()

create_db()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(tenants_routes.router)
app.include_router(users_routes.router)
app.include_router(tasks_routes.router)
app.include_router(loans_routes.router)
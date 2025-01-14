from fastapi import FastAPI
from routes.routes_ia import ia_routes

app = FastAPI()
app.include_router(ia_routes)

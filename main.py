from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models.CEO import CEOS, CEOSchema


app = FastAPI ()

origins = [
    "http://localhost/*",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return{"message": "root route"}

@app.get('/ceos')
def get_ceos():
    ceos = session.query(CEOS)
    return ceos.all()

@app.post('/create/ceos')
async def create_ceos(ceo_data: CEOSchema):
    ceo= CEOS(Name=ceo_data.Name, Slug=ceo_data.Slug, Year_Served=ceo_data.Year_Served)
    session.add(ceo)
    session.commit()
    return {"CEO added": ceo.id}

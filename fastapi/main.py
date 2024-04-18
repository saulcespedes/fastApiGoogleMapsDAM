from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import mysql.connector

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rutes"
)
cursor = db.cursor()

# Definición del modelo Pydantic para la ruta
class Ruta(BaseModel):
    alumne: str
    descripcio: str
    latitud: float
    longitud: float

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Ruta para crear una nueva ruta
@app.post("/rutes/saulcespedes/")
async def create_ruta(ruta: Ruta):
    query = "INSERT INTO ruta (alumne, descripcio, latitud, longitud) VALUES (%s, %s, %s, %s)"
    values = (ruta.alumne, ruta.descripcio, ruta.latitud, ruta.longitud)
    cursor.execute(query, values)
    db.commit()
    return {"message": "Ruta creada exitosamente"}

# Ruta para obtener todas las rutas
@app.get("/rutes/saulcespedes/", response_model=List[Ruta])
async def get_rutas():
    query = "SELECT * FROM ruta"
    cursor.execute(query)
    result = cursor.fetchall()
    rutas = [{"alumne": row[1], "descripcio": row[2], "latitud": row[3], "longitud": row[4]} for row in result]
    return rutas


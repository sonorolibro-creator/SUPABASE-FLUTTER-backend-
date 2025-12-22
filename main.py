from fastapi import FastAPI
from supabase import create_client

# Creamos nuestra app
app = FastAPI()

# Conectamos con Supabase
supabase = create_client(
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY"
)

# Ruta para pedir datos
@app.get("/clientes")
def obtener_cfdis():
    respuesta = supabase.table("clientes").select("*").execute()
    return respuesta.data

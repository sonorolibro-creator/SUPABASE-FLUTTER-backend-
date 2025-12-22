import os
from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/clientes")
def obtener_clientes():
    data = supabase.table("clientes").select("*").execute()
    return data.data

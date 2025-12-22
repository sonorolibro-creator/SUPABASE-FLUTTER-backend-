import os
from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/cfdis")
def obtener_cfdis():
    data = supabase.table("cfdis").select("*").execute()
    return data.data

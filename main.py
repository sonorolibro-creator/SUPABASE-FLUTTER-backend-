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


@app.get("/cfdis/count")
def contar_cfdis(rfc: str):
    response = (
        supabase
        .table("cfdi_xml")
        .select("*", count="exact")
        .or_(f"rfc_emisor.eq.{rfc},rfc_receptor.eq.{rfc}")
        .execute()
    )

    return {
        "rfc": rfc,
        "total": response.count
    }


@app.get("/cfdis/count")
def contar_emitidos(rfc: str):
    response = (
        supabase
        .table("cfdi_xml")
        .select("*", count="exact")
        .eq(f"rfc_emisor",rfc)
        .execute()
    )

    return {
        "rfc": rfc,
        "total": response.count
    }
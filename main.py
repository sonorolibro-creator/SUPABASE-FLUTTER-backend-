import os
from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/clientes/resumen")
def obtener_clientes_resumen():
    return supabase.rpc("clientes_resumen").execute().data



@router.get("/clientes/{rfc}/dashboard/anual/{year}")
def dashboard_anual(rfc: str, year: int):
    try:
        res = supabase.rpc(
          "dashboard_anual",
            {
                "p_rfc": rfc,
                "p_year": year
            }
        ).execute()
        print(res.data)  # 👈 ESTO ES CLAVE
      

        return res.data or {}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/clientes/{rfc}/dashboard/mensual/{year}/{month}")
def dashboard_mensual(rfc: str, year: int, month: int):
    try:
        res = supabase.rpc(
            "rpc_dashboard_resumen_mensual",
            {
                "p_rfc": rfc,
                "p_year": year,
                "p_month": month
            }
        ).execute()

        return res.data or {}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


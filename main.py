from fastapi import FastAPI, HTTPException
from dashboard import get_dashboard
from dashboard import get_dashboard_mensual

app = FastAPI()

@app.get("/dashboard/cfdi")
def dashboard_cfdi(
    cliente_rfc: str,
    year: int,
    month: int | None = None
):
    try:
        return get_dashboard(cliente_rfc, year, month)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        



@app.get("/dashboard/cfdi/mensual")
def dashboard_cfdi_mensual(cliente_rfc: str, year: int):
    try:
        data = get_dashboard_mensual(cliente_rfc, year)
        return data
    except Exception as e:
        print("🔥 ERROR DASHBOARD MENSUAL:", e)
        raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI, HTTPException
from dashboard import get_dashboard

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
